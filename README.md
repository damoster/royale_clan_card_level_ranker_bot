# Clash Royale Clan Member Ranker Discord bot

Discord bot which ranks members in a specific clan according to how many cards of a certain level they have. Comparison starts from number of level 13 cards they have. If it's a tie, card count of the next card level lower is used (e.g. level 12 card count) and so on. This is useful for deciding order of players for boat defenses in clan wars 2.0

## Discord commands available
`!marco` - returns a message reply from bot to indicate it's running and connected properly

`!membercardsranked [clan_tag]` - returns list of clan members ranked by their card levels
- where `clan_tag` does not include #. e.g. `!membercardsranked 9GULPJ9L`
- `clan_tag` can be upper or lower case

## Requirements
Python3+

## How to Run Bot

1. Setup/Switch to a virtual environment (see google's [venv guide](https://cloud.google.com/python/docs/setup#linux_1)). Then install dependencies as so:
    ```shell
    pip3 install -r requirements.txt
    ```
2. Create a `.env` file in the same folder as this project. The environment variables you will putting in it are:
    ```python
    DISCORD_BOT_TOKEN=<discord-bot-token>
    ROYALE_API_KEY=<clash-royale-api-token>
    ```
3. Create a Discord Bot Account. Can follow steps to do that from this [freeCodeCamp discord bot tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/). Once the bot has been created. Copy the token and replace `<discord-bot-token>` in the `.env` file with the token.
4. Invite your bot to the server. Instructions on how to do so is in "How to Invite Your Bot to Join a Server" of the [freeCodeCamp discord bot tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
5. Create a [clash royale developer account](https://developer.clashroyale.com/). Get an API key (when setting one up, it'll ask you to specify the exact IP address where you'll be sending requests from). Copy the token and replace `<clash-royale-api-token>` in the `.env` file with the token.
6. Start the bot on your system/server with:
    ```
    python3 main.py
    ```

## Running tests
```
python3 -m unittest
```

## References
Helpful links used during development
- https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
- https://developer.clashroyale.com/#/documentation 
