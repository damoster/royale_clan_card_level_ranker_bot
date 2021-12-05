import os
import logging
from dotenv import load_dotenv

from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from discord_bot import DiscordBot

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
    bot = DiscordBot()
    bot.run()
    

if __name__ == '__main__':
    main()
