from dataclasses import dataclass

# Numbers represent the prefix of the id of the cards.
# i.e. 26000037 is a Inferno Dragon, 27000007 is Elixir Collector, 28000000 is fireball
CARD_TYPE_ID_PREFIX = {'26': 'troop', '27': 'building', '28': 'spell'}
MAX_CARD_LEVEL = 14

# Minimum fame week required for someone to be active. i.e. used 4 decks 3 times = 12 battles. 12 * 100 = 1200 fame. 
MIN_FAME_WEEK = 1200

@dataclass
class PlayerActivity:
    '''
        A player has a "WarActiveWeek" for a specific week if:
            - Have done at least 3 of 4 war days per week (i.e. used 4 decks 3 times = 12 battles. 
            - At a minimum if they lose every battle that's NOT a boat attack, that would be 12 * 100 = 1200 fame. 
            - Use fame instead of decksUsed since can only get fame on war days, whereas decksUsed include practise days.
        1. war_active is defined as: 
            - Every week while in the clan, they had "WarActiveWeek"s.
            - E.g. 3,4 weeks ago they weren't in clan. Then 2 weeks ago they joined. [2000, 1500, None, None]
        2. elder_worthy is defined as: 
            4 weeks straight of "WarActiveWeek"s.
    '''
    tag: str
    name: str
    role: str
    exp_level: int
    fame_hist: list
    boat_attacks_hist: list
    war_active: bool = False
    elder_worthy: bool = False
    avg_fame: int = -1