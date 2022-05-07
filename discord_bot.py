import os
import discord
import traceback
import logging
from discord.ext import commands


def load_cogs(client):
    for cog in [file.split(".")[0] for file in os.listdir("cogs") if file.endswith(".py")]:
        try:
            if cog != "__init__":
                client.load_extension(f"cogs.{cog}")
        except Exception as exc:
            logging.error(exc)


def get_stack_trace_str(exc: Exception):
    error = getattr(exc, 'original', exc)
    lines = ''.join(traceback.format_exception(
        error.__class__, error, error.__traceback__))
    return lines


class DiscordBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix, activity=discord.Game(name="!bothelp"))

    async def on_ready(self):
        # Loading the Cogs command from the cogs folder
        load_cogs(self)
        print(f'Bot is up and ready. We have logged in as {self.user}')
        logging.info(f'Bot is up and ready. We have logged in as {self.user}')

    async def on_command_error(self, ctx, exc: Exception):
        if isinstance(exc, commands.CommandNotFound):
            # store as info log so we know what people are trying to type into the bot
            logging.info(exc)
            # Prompts the user to use bothelp command to help them with the right command
            message = f"{exc}. Please use !bothelp command for supported commands"
        elif isinstance(exc, commands.MissingRequiredArgument):
            message = "Command used is missing required argument"
            logging.warn(get_stack_trace_str(exc))
        else:
            message = "Oh no! Something went wrong while running the command!"
            # if there are errors not handled above, raise the error and log it
            logging.error(get_stack_trace_str(exc))

        await ctx.send(embed=discord.Embed(
            description=message,
            colour=discord.Colour.red()
        ))
        # Saw some tutorials which want to delete messages about failure after 5 seconds, do we want this?
        # await ctx.send(message, delete_after=5)
        # await ctx.message.delete(delay=5)


if __name__ == "__main__":
    client = DiscordBot(command_prefix=["!"])
    client.run(os.getenv('DISCORD_BOT_TOKEN'))
