import os

import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from textwrap import dedent

from clan_members_rank import ClanMembersRanker


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
                '.env file is missing or {} has not been defined in the .env file'.format(env_var)
            )


def main():
    setup_tokens()

    clan_members_ranker = ClanMembersRanker()
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
        invalid_cmd_reply = 'Please provide a clan tag. E.g.\n`!membercardsranked 9GULPJ9L`'
        if len(args) == 0:
            await ctx.send(invalid_cmd_reply)
            return
        clan_tag = args[0]

        async with ctx.typing():
            # TODO: might want some try catch before sending result in case API requests fail or something...
            print("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = clan_members_ranker.get_clan_cards_rank(clan_tag)
            print("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked))

    # Command specifically for AUSCLAN so they don't have to remember commands / clan_tag
    @bot.command()
    async def ausclan(ctx):
        async with ctx.typing():
            # TODO: might want some try catch before sending result in case API requests fail or something...
            print("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = clan_members_ranker.get_clan_cards_rank("9GULPJ9L")
            print("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked))

    def create_clan_members_ranked_embed(clan_info, clan_members_ranked):
        n = 20  # Number of players to show
        top_n = clan_members_ranked[:n]

        embed = discord.Embed(
            description=dedent('''
                Players ranked by number of cards they have at each level.
                Comparison start at level 13 card count. Showing the top {} players.
                Note that for clan wars 2.0 there can only be 15 players adding cards
                for boat defenses.
            '''.format(n)),
            colour=discord.Colour.blue()
        )

        embed.set_author(
            name=clan_info['name'],
            icon_url='https://icon-library.net//images/clash-royale-icon/clash-royale-icon-8.jpg'
        )

        rank_values = '\n'.join([str(i) for i in range(1, n + 1)])
        name_values = '\n'.join([m['name'] for m in top_n])

        card_level_counts = [member['card_level_counts'] for member in top_n]
        card_count_values = '\n'.join(['{:3},{:3},{:3}'.format(m[13], m[12], m[11]) for m in card_level_counts])

        embed.add_field(name='Rank', value=rank_values, inline=True)
        embed.add_field(name='Name', value=name_values, inline=True)
        embed.add_field(name='# of Level 13, 12, 11 cards', value=card_count_values, inline=True)

        return embed

    bot.run(os.getenv('DISCORD_BOT_TOKEN'))


if __name__ == '__main__':
    main()
