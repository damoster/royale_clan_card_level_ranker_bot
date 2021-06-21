import os

import asyncio
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
from textwrap import dedent

from clan_members_rank import ClanMembersRanker
from common import schemas


def main():
    # Refresh environment variables
    try:
        del os.environ['DISCORD_BOT_TOKEN']
        del os.environ['ROYALE_API_KEY']
    except Exception:
        print("No environment variables to clear")

    load_dotenv()

    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    clan_members_ranker = ClanMembersRanker()

    bot = Bot("!")

    @bot.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(bot))

    # Discord bot commands
    @bot.command()
    async def marco(ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await ctx.send('Polo! Bot is up and running!')

    @bot.command()
    async def membercardsranked(ctx, *args):
        invalid_cmd_reply = 'Please provide a clan tag. E.g.\n`!membercardsranked 9GULPJ9L`'
        card_type_arg = 'all'
        if len(args) == 0:
            await ctx.send(invalid_cmd_reply)
            return
        elif len(args) == 2:
            card_type_arg = args[1].rstrip('s')
            valid_arguments = schemas.CARD_TYPE_ID_PREFIX.values()
            if card_type_arg not in valid_arguments:
                raise TypeError('Third argument is not in scope')
        clan_tag = args[0]

        async with ctx.typing():
            # TODO: might want some try catch before sending result in case API requests fail or something...
            print("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = clan_members_ranker.get_clan_cards_rank(
                clan_tag, card_type_arg)
            print("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked))

    # Command specifically for AUSCLAN so they don't have to remember commands / clan_tag
    @ bot.command()
    async def ausclan(ctx):
        async with ctx.typing():
            # TODO: might want some try catch before sending result in case API requests fail or something...
            print("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = clan_members_ranker.get_clan_cards_rank(
                "9GULPJ9L")
            print("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked))

    def create_clan_members_ranked_embed(clan_info, clan_members_ranked):
        n = 20  # Number of players to show
        top_n = clan_members_ranked[:n]

        # TODO: Add a field or update description to indicate what filter is being used, bold it using markdown e.g. **filter_type**
        embed = discord.Embed(
            description=dedent('''
                Players ranked by number of cards they have at each level.
                Comparison start at level 13 card count. Showing the top **{}** players.
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
        card_count_values = '\n'.join(['{:3},{:3},{:3}'.format(
            m[13], m[12], m[11]) for m in card_level_counts])

        embed.add_field(name='Rank', value=rank_values, inline=True)
        embed.add_field(name='Name', value=name_values, inline=True)
        embed.add_field(name='# of Level 13, 12, 11 cards',
                        value=card_count_values, inline=True)

        return embed

    bot.run(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    main()
