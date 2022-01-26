from dataclasses import dataclass

# Numbers represent the prefix of the id of the cards.
# i.e. 26000037 is a Inferno Dragon, 27000007 is Elixir Collector, 28000000 is fireball
CARD_TYPE_ID_PREFIX = {'26': 'troop', '27': 'building', '28': 'spell'}
MAX_CARD_LEVEL = 14

# Data Clases
@dataclass
class player_historical_activity:
    tag: str
    name: str
    fame_hist: list
    boat_attacks_hist: list
    deck_used_hist: list