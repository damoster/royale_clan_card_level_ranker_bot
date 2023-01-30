import discord
from discord.ext import commands
from textwrap import dedent


class BasicInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="bothelp", pass_context=True)
    async def bothelp(self, ctx):
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
                f'[!ausclanwar [weeks]]({url}) - Shows the war peformance of the players in x amount of weeks. Defaults to 4 weeks if not specified',
                f'[!ausclanremaining]({url}) - Shows the remaining war attacks & remaining players count for the current river race',
                f'[!ausclanremainingplayers]({url}) - Shows all players within the clan and players who left the clan who has not completed all war attacks. Add "exclude" argument to exclude players out of the clan'
            ]
            generic_cmds = [
                f'[!bothelp]({url}) - Shows this help message about available commands.',
                f'[!membercardsranked [clan_tag] [filter]]({url}) - Does same thing as `!ausclan` but '
                'for the specific [clan_tag] instead.',
                f'[!boatattack [clan_tag]]({url}) - Does same thing as `!ausclanboat` but for the specific [clan_tag] instead.',
                f'[!riverwar [clan_tag] [weeks]]({url}) - Does same thing as `!ausclanwar` but for the specific [clan_tag] instead.',
                f'[!clanremaining [clan_tag]]({url}) - Does same thing as `!ausclanremaining` but for the specific [clan_tag] instead.',
                f'[!clanremainingplayers]({url}) - Does same thing as `!ausclanremainingplayers` but for the specific [clan_tag] instead.'
            ]
            embed.add_field(name='Ausclan commands', value='\n'.join(ausclan_cmds), inline=False)
            embed.add_field(name='Other commands', value='\n'.join(generic_cmds), inline=False)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(BasicInfo(client))
