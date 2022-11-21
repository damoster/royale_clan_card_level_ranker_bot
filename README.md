# Clash Royale Clan Member Ranker Discord bot

Discord bot which ranks members in a specific clan according to how many cards of a certain level they have. Comparison starts from number of level 14 cards they have. If it's a tie, card count of the next card level lower is used (e.g. level 12 card count) and so on. This is useful for deciding order of players for boat defenses in clan wars 2.0

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
    1. Get an API key (when setting one up, it'll ask you to specify the exact IP address where you'll be sending requests from).
        > **Note:** If you plan to run the bot from a location which has dynamic IP addresses (such as running a bot from a household residentional IP address), when creating a key, set the allowed IP address as "45.79.218.79". (It used to be "128.128.128.128". For the latest news regarding this solution see https://docs.royaleapi.com/#/proxy)
    2. Copy the token and replace `<clash-royale-api-token>` in the `.env` file with the token.
    
    
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

## Running with Docker
```
docker-compose up

or

docker build -t clash-bot .

docker run clash-bot

docker run -d --restart unless-stopped clash-bot
```
## References
Helpful links used during development
- https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
- https://developer.clashroyale.com/#/documentation 
- Discord COGS tutorial - https://www.youtube.com/watch?v=mWLtUhY1kqg&list=PLYtUtBE908CsROaXFxwENoOM_D5HtAeWi&index=2&ab_channel=synopNode%28%29
