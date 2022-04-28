import discord
from discord.ext import commands
from textwrap import dedent
from common import schemas
import logging
from typing import Dict

from royale_api_website_scraper import RoyaleApiWebsiteScraper
from clash_royale_service import ClashRoyaleService
from common.schemas import PlayerActivity, MAX_DISCORD_EMBED


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

def clan_river_race_history_embed(clan_info: Dict, clan_players_war_history: Dict[str, PlayerActivity]):
    embed = discord.Embed(
        description=dedent('''
            **ElderWorthy** means player obtains minimum of 1200 fame per week over past 4 weeks. 
            Doing 3/4 war days and losing all of them. i.e. 1200 = 3 days x 4 decks x 100 fame per non-boat-attack-loss.
            Order of the **FameHistory** - First item is fame from 1 week ago, then 2, 3, 4.
        '''.format()),
        colour=discord.Colour.green()
    )

    embed.set_author(
        name=clan_info['name'],
        icon_url='https://static.wikia.nocookie.net/clashroyale/images/9/9f/War_Shield.png/revision/latest/scale-to-width-down/250?cb=20180425130200'
    )

    columns = '**WarActive** | **ElderWorthy** | **FameHistory** | **Name** | **Role**'
    row_promote = []
    row_demote = []
    final_str = []
    for player_tag in clan_players_war_history:
        player = clan_players_war_history[player_tag]
        row_val = '` {:^1} ` | ` {:^1} ` | ` {} ` | {:>} | {}'.format(
            'Y' if player.war_active else 'N',
            'Y' if player.elder_worthy else 'N',
            ",".join(["{:^4}".format(x) if isinstance(x, int) else '_' for x in player.fame_hist]),
            player.name,
            player.role
        )
        if player.war_active and player.elder_worthy and player.role == 'member':
            row_promote.append(row_val)
        elif not player.war_active:
            row_demote.append(row_val)
    
    final_str = ['**PROMOTE**'] + row_promote + ['**DEMOTE/KICK**'] + row_demote
    final_str = '\n'.join(final_str)
    logging.info("embedded content length is: " + str(len(final_str)))
    if len(final_str) >= MAX_DISCORD_EMBED:
        warn_msg = "\nNote: Final output has been truncated due to exceeding limit 1024"
        final_str = final_str[:(MAX_DISCORD_EMBED-len(warn_msg))] + warn_msg
    embed.add_field(name=columns, value=final_str, inline=False)
    return embed

def remaining_war_embed(all_clan_attacks):
    embed = discord.Embed(
        description=dedent('''
            Put Description Here
        '''.format()),
        colour=discord.Colour.green()
    )
    columns = '**Clan**|**Medals**|**Fame**|**Participated**|**DecksRemaining**|**PlayersRemaining**'
    row_val = []
    for clan_attacks in all_clan_attacks:
        row_val.append('`{:^15}`|`{:^5}`|`{:^6}`|`{:^6}`|`{:^9}`|`{:^10}`'.format(
            clan_attacks.name,
            clan_attacks.medals,
            clan_attacks.fame,
            str(clan_attacks.participated) + '/50',
            str(clan_attacks.decks_remaining) + ' decks',
            str(clan_attacks.players_remaining) + ' players'
        ))
    row_val = '\n'.join(row_val)
    embed.add_field(name=columns, value=row_val, inline=False)
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

    @commands.command(name="ausclanwar", pass_context=True)
    async def ausclanwar(self, ctx, past_weeks=4):
        async with ctx.typing():
            clan_info, clan_players_war_history = self.clash_royale_service.clan_river_race_history('9GULPJ9L', past_weeks)
        embed = clan_river_race_history_embed(clan_info, clan_players_war_history)
        await ctx.send(embed=embed)

    @commands.command(name="riverwar", pass_context=True)
    async def riverwar(self, ctx, clan_tag: str, past_weeks=4):
        async with ctx.typing():
            clan_info, clan_players_war_history = self.clash_royale_service.clan_river_race_history(clan_tag, past_weeks)
        embed = clan_river_race_history_embed(clan_info, clan_players_war_history)
        await ctx.send(embed=embed)

    @commands.command(name="ausclanremaining", pass_context=True)
    async def ausclanRemainingWarAttacks(self, ctx):
        async with ctx.typing():
            all_clan_attacks = self.clash_royale_service.clan_remaining_war_attacks('9GULPJ9L')
        embed = remaining_war_embed(all_clan_attacks)
        await ctx.send(embed=embed)

    @commands.command(name="clanremaining", pass_context=True)
    async def clanRemainingWarAttacks(self, ctx, clan_tag: str):
        async with ctx.typing():
            all_clan_attacks = self.clash_royale_service.clan_remaining_war_attacks(clan_tag)
        embed = remaining_war_embed(all_clan_attacks)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ClashRiverWar(client))
