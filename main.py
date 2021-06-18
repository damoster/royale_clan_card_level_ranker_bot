import discord
import os
from dotenv import load_dotenv

# from clash_royale_client import ClashRoyaleClient # fix this later with better import practises
from clan_members_rank import ClanMembersRanker

load_dotenv()

client = discord.Client()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
clan_members_ranker = ClanMembersRanker()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!marco'):
        await message.channel.send('Polo! Hello there! Bot is up and running')

    invalid_cmd_reply = 'Please provide a clan tag. E.g.\n`!membercardsranked 9GULPJ9L`'
    if msg.startswith('!membercardsranked'):
        split_msg = msg.split('!membercardsranked ',1)
        
        if len(split_msg) == 1:
            await message.channel.send(invalid_cmd_reply)
            return

        clan_tag = split_msg[1].upper()
        if clan_tag == '':
            await message.channel.send(invalid_cmd_reply)
            return

        # TODO: might want some try catch before sending result
        print("Started fetch ranked members processing...")
        clan_members_ranked = clan_members_ranker.getClanCardsRank(clan_tag)
        print("Completed fetch ranked members processing")
        await message.channel.send(pretty_clan_members_ranked_output(clan_members_ranked))

def pretty_clan_members_ranked_output(clan_members_ranked):
    final_output = '      Name     |   tag    | # lvl13 | # lvl12 | # lvl11'
    final_output += '\n-------------------------------------------------------'
    # Only print top 15 members
    for member in clan_members_ranked[:15]:
        n13 = member['member_card_levels'][13]
        n12 = member['member_card_levels'][12]
        n11 = member['member_card_levels'][11]
        output_line = '{:^15}|{:^10}|{:^9}|{:^9}|{:^9}'.format(member['name'], member['tag'], n13, n12, n11)
        final_output += '\n' + output_line
    return final_output

client.run(DISCORD_BOT_TOKEN)

# Dependencies
# python-dotenv
# discord.py

# Ausclan tag
#9GULPJ9L

# TODO:
# nice to have
# - Fix file/project layour
# - pipenv/readme/setup
# - test responding with pretty list
# - have arguments to specify include troops only (exclude buildings/spells)
    # - to do this, would need a dictionary storing 
# - Make discord bot typing animation or something while request is processing
# - Store the result or somehow cache things to make less responses? (we're being rate limited....or reuse connection somehow hmmmmmm)

# Tutorials followed:
# https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
# https://developer.clashroyale.com/#/documentation 

# Set up steps
# 0. Must use python3
# 1. setup env (TODO use pipenv or something to make it easier)
# 2. make an application with a discord bot. Get the TOKEN for the bot
# 3. make an account on https://developer.clashroyale.com/ and get a ROYALE_API_KEY 