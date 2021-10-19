import os

import discord
import logging
import traceback
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from textwrap import dedent

from clan_members_rank import ClanMembersRanker
from common import schemas
from royale_api_website_scraper import RoyaleApiWebsiteScraper

from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

def setup_tokens():
    expected_env_vars = [
        'DISCORD_BOT_TOKEN',
        'ROYALE_API_KEY'
    ]
    # Refresh environment variables since load_dotenv doesn't override them if already set
    for env_var in expected_env_vars:
        if os.getenv(env_var) is not None:
            del os.environ[env_var]
            logging.info('Refreshed environment variable: {}'.format(env_var))

    # Load environment variables saved in .env file
    load_dotenv()
    for env_var in expected_env_vars:
        if os.getenv(env_var) is None:
            raise ValueError(
                '.env file is missing or {} has not been defined in the .env file'.format(
                    env_var)
            )


def setup_logging(logging_level=logging.WARNING):
    # Create logging folder path if doesn't exist
    logging_directory = "./logs/"
    if not os.path.exists(logging_directory):
        os.makedirs(logging_directory)

    logFormatter = logging.Formatter(
        "%(asctime)s - [%(threadName)s] - [%(levelname)s] - [%(name)s] - %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging_level)
    # TimedRotating FileHandler
    timedRotatingFileHandler = TimedRotatingFileHandler(
        logging_directory + 'system-logs-{:%Y-%m-%d}.log'.format(datetime.now()), when="w0", interval=1)
    timedRotatingFileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(timedRotatingFileHandler)
    # Writes logs to sys.sterr
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)


def main():
    setup_tokens()

    # To enable logging on INFO level, logging_level=logging.INFO. Default is ERROR
    setup_logging(logging_level=logging.INFO)
    clan_members_ranker = ClanMembersRanker()
    royale_api_website_scraper = RoyaleApiWebsiteScraper()
    activity = discord.Game(name="!bothelp")
    bot = Bot("!", activity=activity)

    @bot.event
    async def on_ready():
        print(f'Bot is up and ready. We have logged in as {bot.user}')
        logging.info(f'Bot is up and ready. We have logged in as {bot.user}')

    @bot.event
    async def on_command_error(ctx, exc: Exception):
        if isinstance(exc, commands.CommandNotFound):
            # store as info log so we know what people are trying to type into the bot
            logging.info(exc)
            return  # Return because we don't want to log an error for every command not found
        else:
            message = "Oh no! Something went wrong while running the command!"
            # if there are errors not handled above, raise the error and log it
            error = getattr(exc, 'original', exc)
            lines = ''.join(traceback.format_exception(
                error.__class__, error, error.__traceback__))
            logging.error(lines)

        await ctx.send(embed=discord.Embed(
            description=message,
            colour=discord.Colour.red()
        ))
        # Saw some tutorials which want to delete messages about failure after 5 seconds, do we want this?
        # await ctx.send(message, delete_after=5)
        # await ctx.message.delete(delay=5)

    # Discord bot commands
    @bot.command()
    async def bothelp(ctx):
        async with ctx.typing():
            embed = discord.Embed(
                description=dedent('''
                This bot provides a variety of useful commands to help with clan management.
                '''),
                colour=discord.Colour.purple()
            )
            url = 'https://royaleapi.com/clan/9GULPJ9L/war/race'
            ausclan_cmds = [
                f'[!ausclan [filter]]({url}) - Shows clan members ranked by number of high level cards they have. [filter] '
                'can be one of \'all\', \'troop\', \'spell\' or \'building\'. Defaults to \'all\' if not specified',
                f'[!ausclanboat]({url}) - Lists clan members who attacked enemy boats this week.',
            ]
            generic_cmds = [
                f'[!bothelp]({url}) - Shows this help message about available commands.',
                f'[!membercardsranked [clan_tag] [filter]]({url}) - Does same thing as `!ausclan` but '
                'for the specific [clan_tag] instead.',
                f'[!boatattack [clan_tag]]({url}) - Does same thing as `!ausclanboat` but for the specific [clan_tag] instead.'
            ]
            embed.add_field(name='Ausclan commands', value='\n'.join(ausclan_cmds), inline=False)
            embed.add_field(name='Other commands', value='\n'.join(generic_cmds), inline=False)
        await ctx.send(embed=embed)

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
        async with ctx.typing():
            logging.info("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = clan_members_ranker.get_clan_cards_rank(
                clan_tag, card_type_arg)
            logging.info("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked, card_type_arg))

    async def card_type_check(ctx, card_type):
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
            clan_info, war_partitipation_table = royale_api_website_scraper.get_war_participation_table(clan_tag)
            embed = boat_attackers_embed(war_partitipation_table, clan_info)
        await ctx.send(embed=embed)

    @bot.command()
    async def ausclanboat(ctx):
        await boatattack(ctx, '9GULPJ9L')

    def boat_attackers_embed(boat_attackers, clan_info):
        if len(boat_attackers) == 0:
            description = 'There are no clan members who attacked enemy boats this week.'
            colour = discord.Colour.blue()
        else:
            description = f'**{len(boat_attackers)}** player(s) attacked enemy boats this week.'
            colour = discord.Colour.orange()

        embed = discord.Embed(description=description, colour=colour)
        embed.set_author(name=clan_info['name'], icon_url=clan_info['logo_url'])

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
