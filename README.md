# Clash Royale Clan Member Ranker Discord bot

Discord bot which ranks members in a specific clan according to how many cards of a certain level they have. Comparison starts from number of level 13 cards they have. If it's a tie, card count of the next card level lower is used (e.g. level 12 card count) and so on. This is useful for deciding order of players for boat defenses in clan wars 2.0

## Discord commands available

`!membercardsranked [clan_tag]` - returns list of clan members ranked by their card levels
- where `clan_tag` does not include #. e.g. `!membercardsranked 9GULPJ9L`
- `clan_tag` can be upper or lower case

`!ausclan` - does the same thing as `!membercardsranked 9GULPJ9L`. Mostly likely just used by this clan anyway.

`!boatattack [clan_tag]` - returns list of clan members that attacked other's boat
- where `clan_tag` does not include #. e.g. `!membercardsranked 9GULPJ9L`
- `clan_tag` can be upper or lower case
`!ausclanboat` - does the same thing as `!boatattack 9GULPJ9L`. Mostly likely just used by this clan anyway.

## Requirements
Python3+

## How to Run Bot

1. Setup/Switch to a virtual environment (for `venv` see google's [venv guide](https://cloud.google.com/python/docs/setup#linux_1)). Then install dependencies as so:
    ```shell
    pip3 install -r requirements.txt
    ```
    OR using the Makefile
    ```
    make init
    ```
2. Create a `.env` file in the same folder as this project. The environment variables you will putting in it are:
    ```python
    DISCORD_BOT_TOKEN=<discord-bot-token>
    ROYALE_API_KEY=<clash-royale-api-token>
    ```
3. Create a Discord Bot Account. Can follow steps to do that from this [freeCodeCamp discord bot tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/). Once the bot has been created. Copy the token and replace `<discord-bot-token>` in the `.env` file with the token.
4. Invite your bot to the server. Instructions on how to do so is in "How to Invite Your Bot to Join a Server" of the [freeCodeCamp discord bot tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
5. Create a [clash royale developer account](https://developer.clashroyale.com/). 
    1. Get an API key (when setting one up, it'll ask you to specify the exact IP address where you'll be sending requests from). Please read Note below 2.
    2. Copy the token and replace `<clash-royale-api-token>` in the `.env` file with the token.
    
    Note: We have migrated the clash royal url from https://api.clashroyale.com/v1 to https://proxy.royaleapi.dev/v1 due to the dynamic ip setting from ISP for household ip address. To address this issue, when getting an API key, set the IP address as "128.128.128.128". 
6. Start the bot on your system/server with:
    ```
    python3 main.py
    ```
    OR using the Makefile
    ```
    make run
    ```

## Running tests
```
pytest
```
OR using the Makefile
```
make test
```

## References
Helpful links used during development
- https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
- https://developer.clashroyale.com/#/documentation 
