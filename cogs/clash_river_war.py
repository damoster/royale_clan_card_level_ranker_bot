import discord
from discord.ext import commands
from textwrap import dedent
from common import schemas
import logging
from typing import Dict

from royale_api_website_scraper import RoyaleApiWebsiteScraper
from clash_royale_service import ClashRoyaleService
from common.schemas import PlayerActivity, MAX_DISCORD_ENBED


def create_clan_members_ranked_embed(clan_info, clan_members_ranked, card_type_arg='all'):
    n = 20  # Number of players to show
    top_n = clan_members_ranked[:n]

    embed = discord.Embed(
        description=dedent('''
            Players ranked by number of cards they have at each level. Comparison start at level 14 card count.
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
        rank_text_row = '` {:2d} ` | ` ({:2d}, {:2d}), {:2d}, {:2d} ` | **{}**'.format(
            idx + 1, mc[14], mc[13], mc[12], mc[11], member['name']
        )
        rank_values.append(rank_text_row)
    field_name = '**Rank** | **# of lvl (14, 13), 12, 11** | **Player Name**'
    embed.add_field(name=field_name, value='\n'.join(rank_values), inline=False)

    return embed


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

def clan_river_race_history_embed(clan_players_war_history: Dict[str, PlayerActivity]):
    embed = discord.Embed(
        description=dedent('''
            Clan River Race History
        '''.format()),
        colour=discord.Colour.green()
    )
    # columns = 'War Active | Elder Worthy | Name | Role | Level | Fame History | Boat Attack History | Average Fame'
    # row_values = []
    # for player_tag in clan_players_war_history:
    #     player = clan_players_war_history[player_tag]
    #     row_val = '` {} `|` {} `|` {} `|` {} `|` {} `|` {} `|` {} `|` {} '.format(
    #         player.war_active, player.elder_worthy, player.name, player.role , player.exp_level , player.fame_hist, player.boat_attacks_hist, player.avg_fame
    #     )
    #     row_values.append(row_val)
    # columns = '**WarActive** | **ElderWorthy** | **AvgFame** | **Name** | **Role**'
    # row_promote = []
    # row_demote = []
    # row_final = []
    # for player_tag in clan_players_war_history:
    #     player = clan_players_war_history[player_tag]
    #     row_val = '` {:^1} ` | ` {:^1} ` | ` {} ` | ` {:>} ` | **{:>}**'.format(
    #         'Y' if player.war_active else 'N',
    #         'Y' if player.elder_worthy else 'N',
    #         player.avg_fame,
    #         player.role,
    #         player.name
    #     )
    #     if player.war_active and player.elder_worthy and player.role == 'member':
    #         row_promote.append(row_val)
    #     elif not player.war_active:
    #         row_demote.append(row_val)

    columns = '**WarActive** | **ElderWorthy** | **FameHistory** | **Name**'
    row_promote = []
    row_demote = []
    row_final = []
    for player_tag in clan_players_war_history:
        player = clan_players_war_history[player_tag]
        row_val = '` {:^1} ` | ` {:^1} ` | ` {} ` | ` {:>} `'.format(
            'Y' if player.war_active else 'N',
            'Y' if player.elder_worthy else 'N',
            [ i if isinstance(i, int) else '' for i in player.fame_hist ],
            player.name
        )
        if player.war_active and player.elder_worthy and player.role == 'member':
            row_promote.append(row_val)
        elif not player.war_active:
            row_demote.append(row_val)
    
    row_final = ['**TO PROMOTE**'] + row_promote + ['**TO DEMOTE**'] + row_demote
    row_final = '\n'.join(row_final)
    if len(row_final) >= MAX_DISCORD_ENBED:
        row_final = row_final[:MAX_DISCORD_ENBED]
    embed.add_field(name=columns, value=row_final, inline=False)
    return embed


class ClashRiverWar(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.clash_royale_service = ClashRoyaleService()
        self.royale_api_website_scraper = RoyaleApiWebsiteScraper()

    async def fetch_ranked_members(self, ctx, clan_tag, card_type_arg='all'):
        async with ctx.typing():
            logging.info("Started fetch ranked members processing...")
            clan_info, clan_members_ranked = self.clash_royale_service.get_clan_cards_rank(
                clan_tag, card_type_arg)
            logging.info("Completed fetch ranked members processing")

        await ctx.send(embed=create_clan_members_ranked_embed(clan_info, clan_members_ranked, card_type_arg))

    async def card_type_check(self, ctx, card_type):
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

    @commands.command(name="membercardsranked", pass_context=True)
    async def membercardsranked(self, ctx, *args):
        card_type_arg = 'all'
        if len(args) == 0:
            invalid_cmd_reply = 'Please provide a clan tag. E.g.\n`!membercardsranked 9GULPJ9L`'
            await ctx.send(invalid_cmd_reply)
            return
        elif len(args) == 2:
            card_type_arg = args[1].lower().rstrip('s')
            check_result = await self.card_type_check(ctx, card_type_arg)
            if check_result is not True:
                return
        clan_tag = args[0]

        await self.fetch_ranked_members(ctx, clan_tag, card_type_arg)

    @commands.command(name="ausclan", pass_context=True)
    async def ausclan(self, ctx, *args):
        card_type_arg = 'all'
        if len(args) == 1:
            card_type_arg = args[0].lower().rstrip('s')
            check_result = await self.card_type_check(ctx, card_type_arg)
            if check_result is not True:
                return

        await self.fetch_ranked_members(ctx, '9GULPJ9L', card_type_arg)

    @commands.command(name="boatattack", pass_context=True)
    async def boatattack(self, ctx, clan_tag):
        async with ctx.typing():
            clan_info, war_partitipation_table = self.royale_api_website_scraper.get_war_participation_table(clan_tag)
            embed = boat_attackers_embed(war_partitipation_table, clan_info)
        await ctx.send(embed=embed)

    @commands.command(name="ausclanboat", pass_context=True)
    async def ausclanboat(self, ctx):
        await self.boatattack(ctx, '9GULPJ9L')

    @commands.command(name="playersclanwar", pass_context=True)
    async def playersclanwar(self, ctx, clan_tag: str, past_weeks=4):
        clan_players_war_history = self.clash_royale_service.clan_river_race_history(clan_tag, past_weeks)
        embed = clan_river_race_history_embed(clan_players_war_history)
        await ctx.send(embed=embed)

    @commands.command(name="ausclanwar", pass_context=True)
    async def playersclanwar(self, ctx, past_weeks=4):
        async with ctx.typing():
            logging.info("Fetching Clan River Race History")
            clan_players_war_history = self.clash_royale_service.clan_river_race_history('9GULPJ9L', past_weeks)
            logging.info("Completed Fetching Clan River Race History")
        embed = clan_river_race_history_embed(clan_players_war_history)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ClashRiverWar(client))
