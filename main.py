import os

import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from textwrap import dedent

from clan_members_rank import ClanMembersRanker
from common import schemas
from royale_api_website_scraper import RoyaleApiWebsiteScraper


def setup_tokens():
    expected_env_vars = [
        'DISCORD_BOT_TOKEN',
        'ROYALE_API_KEY'
    ]
    # Refresh environment variables since load_dotenv doesn't override them if already set
    for env_var in expected_env_vars:
        if os.getenv(env_var) is not None:
            del os.environ[env_var]
            print('Refreshed environment variable: {}'.format(env_var))

    # Load environment variables saved in .env file
    load_dotenv()
    for env_var in expected_env_vars:
        if os.getenv(env_var) is None:
            raise ValueError(
                '.env file is missing or {} has not been defined in the .env file'.format(
                    env_var)
            )


def main():
    setup_tokens()

    clan_members_ranker = ClanMembersRanker()
    royale_api_website_scraper = RoyaleApiWebsiteScraper()
    bot = Bot("!")

    @bot.event
    async def on_ready():
        print('Bot is up and ready. We have logged in as {0.user}'.format(bot))

    @bot.event
    async def on_command_error(ctx, error):
        # Change print statement to logging instead later on
        print(error)
        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        else:
            message = "Oh no! Something went wrong while running the command!"

        await ctx.send(embed=discord.Embed(
            description=message,
            colour=discord.Colour.red()
        ))
        # Saw some tutorials which want to delete messages about failure after 5 seconds, do we want this?
        # await ctx.send(message, delete_after=5)
        # await ctx.message.delete(delay=5)

    # Discord bot commands
    @bot.command()
    async def marco(ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send('Polo! Bot is up and running!')

    @bot.command()
    async def membercardsranked(ctx, *args):
        card_type_arg = 'all'
        if len(args) == 0:
            invalid_cmd_reply = 'Please provide a clan tag. E.g.\n`!membercardsranked 9GULPJ9L`'
            await ctx.send(invalid_cmd_reply)
            return
        elif len(args) == 2:
            card_type_arg = args[1].lower().rstrip('s')
            check_result = await card_type_check(ctx, card_type_arg)
            if check_result is not True:
                return
        clan_tag = args[0]

        await fetch_ranked_members(ctx, clan_tag, card_type_arg)

    @ bot.command()
    async def ausclan(ctx, *args):
        card_type_arg = 'all'
        if len(args) == 1:
            card_type_arg = args[0].lower().rstrip('s')
            check_result = await card_type_check(ctx, card_type_arg)
            if check_result is not True:
                return

        await fetch_ranked_members(ctx, '9GULPJ9L', card_type_arg)

    async def fetch_ranked_members(ctx, clan_tag, card_type_arg='all'):
        print("we here lads")
        async with ctx.typing():
            print("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = clan_members_ranker.get_clan_cards_rank(
                clan_tag, card_type_arg)
            print("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked, card_type_arg))

    async def card_type_check(ctx, card_type):
        print("nani")
        valid_arguments = schemas.CARD_TYPE_ID_PREFIX.values()
        if card_type not in valid_arguments:
            message = 'Card Filter parameter is not in scope, please provide correct card filter: troops, spells, or buildings'
            await ctx.send(embed=discord.Embed(
                description=message,
                colour=discord.Colour.red()
            ))
            return False
        else:
            return True

    @bot.command()
    async def boatattack(ctx, clan_tag):
        async with ctx.typing():
            embed = boat_attackers_embed(
                royale_api_website_scraper.get_war_participation_table(clan_tag),
                'Unknown'  # TODO could get clan name from webscraper
            )
        await ctx.send(embed=embed)

    @bot.command()
    async def ausclanboat(ctx):
        async with ctx.typing():
            embed = boat_attackers_embed(
                royale_api_website_scraper.get_war_participation_table('9GULPJ9L'),
                'AUSCLAN'
            )
        await ctx.send(embed=embed)

    def boat_attackers_embed(boat_attackers, clan_name):
        if len(boat_attackers) == 0:
            description = 'There are no clan members who attacked enemy boats this week.'
        else:
            description = f'**{len(boat_attackers)}** player(s) who attacked enemy boats this week.'
        embed = discord.Embed(description=description, colour=discord.Colour.blue())

        embed.set_author(
            name=clan_name,
            icon_url='https://icon-library.net//images/clash-royale-icon/clash-royale-icon-8.jpg'
        )

        if len(boat_attackers) != 0:
            columns = 'Boat attacks | Medals | Name'
            row_values = []
            for p in boat_attackers:
                row_val = '`     {:^2}    `|`  {:^4} `| {}'.format(
                    p[5], p[6], p[1]
                )
                row_values.append(row_val)
            embed.add_field(name=columns, value='\n'.join(row_values), inline=False)

        return embed

    def create_clan_members_ranked_embed(clan_info, clan_members_ranked, card_type_arg='all'):
        n = 20  # Number of players to show
        top_n = clan_members_ranked[:n]

        embed = discord.Embed(
            description=dedent('''
                Players ranked by number of cards they have at each level. Comparison start at level 13 card count.
                Showing the top **{}** players.
                Card Count Filter Type: **{}**
            '''.format(n, card_type_arg)),
            colour=discord.Colour.blue()
        )

        embed.set_author(
            name=clan_info['name'],
            icon_url='https://icon-library.net//images/clash-royale-icon/clash-royale-icon-8.jpg'
        )

        rank_values = []
        for idx, member in enumerate(top_n):
            mc = member['card_level_counts']
            rank_text_row = '` {:2d} ` | `  {:2d}, {:2d}, {:2d}  ` | **{}**'.format(
                idx + 1, mc[13], mc[12], mc[11], member['name']
            )
            rank_values.append(rank_text_row)
        field_name = '**Rank** | **# of lvl 13, 12, 11** | **Player Name**'
        embed.add_field(name=field_name, value='\n'.join(rank_values), inline=False)

        return embed

    bot.run(os.getenv('DISCORD_BOT_TOKEN'))


if __name__ == '__main__':
    main()
