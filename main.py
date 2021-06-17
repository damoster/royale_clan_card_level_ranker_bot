import discord
import os
from dotenv import load_dotenv

from clash_royale_client import ClashRoyaleClient # fix this later with better import practises

load_dotenv()

client = discord.Client()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
print(DISCORD_BOT_TOKEN)
c = ClashRoyaleClient()

@client.event
async def on_ready():
    print('We have logging in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!noticeme'):
        await message.channel.send('Hello there!')


# client.run(DISCORD_BOT_TOKEN)

# Dependencies
# python-dotenv
# discord.py

# Ausclan tag
#9GULPJ9L

# TODO:
# - test passing argument from discord bot (after taking input, should then upper case it) 
# - test responding with csv
# nice to have
# - test responding with pretty list
# - have arguments to specify include troops only (exclude buildings/spells)

# Set up steps
# 0. Must use python3
# 1. setup env (TODO use pipenv or something to make it easier)
# 2. make an application with a discord bot. Get the TOKEN for the bot
# 3. make an account on https://developer.clashroyale.com/ and get a ROYALE_API_KEY 