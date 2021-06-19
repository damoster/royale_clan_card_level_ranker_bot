import os
import discord
import asyncio
from discord.ext.commands import Bot
from dotenv import load_dotenv

from clan_members_rank import ClanMembersRanker

load_dotenv()

client = discord.Client()
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
    if len(args) == 0:
        await ctx.send(invalid_cmd_reply)
        return
    clan_tag = args[0]

    # TODO: Why does the bot stop typing so quickly (seems there's a 10 second limit)? Function below hasn't finish completing yet and it finishes typing
    async with ctx.typing():
        # TODO: might want some try catch before sending result in case API requests fail or something...
        print("Started fetch ranked members processing...")
        clan_members_ranked = clan_members_ranker.get_clan_cards_rank(clan_tag)
        print("Completed fetch ranked members processing")
        await asyncio.sleep(15)

    await ctx.send(pretty_clan_members_ranked_output(clan_members_ranked))

def pretty_clan_members_ranked_output(clan_members_ranked):
    final_output = 'Rank|           Name          |   tag    | # lvl13 | # lvl12 | # lvl11'
    final_output += '\n{}+{}+{}+{}+{}+{}'.format('-'*4, '-'*25, '-'*10, '-'*9, '-'*9, '-'*9)
    # Only print top 20 members (Can only have 15 boat defenses anyway)
    for idx, member in enumerate(clan_members_ranked[:20]):
        n13 = member['card_level_counts'][13]
        n12 = member['card_level_counts'][12]
        n11 = member['card_level_counts'][11]
        output_line = '{:^4}|{:^25}|{:^10}|{:^9}|{:^9}|{:^9}'.format(idx + 1, member['name'], member['tag'], n13, n12, n11)
        final_output += '\n' + output_line
    return final_output

bot.run(DISCORD_BOT_TOKEN)

# TODO:
# nice to have
# - Fix file/project layout
# - Add a makefile?
# - pylint
# - test responding with pretty list
# - Make discord bot typing animation or something while request is processing
# - have arguments to specify include troops only (exclude buildings/spells)
    # - to do this, would need a dictionary storing 
# - Store the result or somehow cache things to make less responses? (we're being rate limited....or reuse connection somehow hmmmmmm)
    # - Could have an SQLite db to store for just out clan (update it once every 10/30mins?) and that way results would be returned instantly almost