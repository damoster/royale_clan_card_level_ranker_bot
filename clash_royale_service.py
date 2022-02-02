import copy
from functools import cmp_to_key
from multiprocessing import Pool
from typing import Dict, Tuple, Any

from clash_royale_client import ClashRoyaleClient
from common.schemas import CARD_TYPE_ID_PREFIX, MAX_CARD_LEVEL, PlayerActivity, MIN_FAME_WEEK


# NOTE: we want the highest level to come first (sort descending)
def card_count_comparator(count1, count2):
    if count1 < count2:
        return 1
    elif count1 > count2:
        return -1
    else:
        return 0


def compare_card_levels(p1, p2):
    compare_result = 0
    card_level = MAX_CARD_LEVEL
    while compare_result == 0 and card_level > 0:
        # Not many players have a lot of level 14 cards yet, but it has a hugh weighting if we don't compare them by group level 13 and 14 cards together
        if card_level == MAX_CARD_LEVEL:
            p1_card_count = p1['card_level_counts'][card_level] + p1['card_level_counts'][card_level - 1]
            p2_card_count = p2['card_level_counts'][card_level] + p2['card_level_counts'][card_level - 1]
            card_level -= 2
        else:
            p1_card_count = p1['card_level_counts'][card_level]
            p2_card_count = p2['card_level_counts'][card_level]
            card_level -= 1
        compare_result = card_count_comparator(p1_card_count, p2_card_count)
    return compare_result


def compute_war_active(fame_hist: list) -> bool:
    war_active = True
    for week in fame_hist:
        if week is None:
            continue
        elif week < MIN_FAME_WEEK:
            war_active = False
            break
    return war_active

def compute_elder_worthy(fame_hist: list) -> bool:
    elder_worthy = True
    for week in fame_hist:
        if week is None or week < MIN_FAME_WEEK:
            elder_worthy = False
            break
    return elder_worthy

def compute_average_fame(fame_hist: list) -> int:
    average_fame = -1
    result = [fame for fame in fame_hist if fame is not None]
    if len(result) > 0:
        average_fame = sum(result) / len(result)
    return average_fame

class ClashRoyaleService:
    def __init__(self):
        # Using pool size of 50 since that is the player limit in a clan
        self.pool_size = 50  # Using for I/O bound task (API requests)
        self.clash_royale_client = ClashRoyaleClient()

    '''
    Clan Ranker Functions
    '''

    def get_card_level_counts(self, player_cards, card_type_filter='all'):
        # card_type_filter check
        valid_arguments = CARD_TYPE_ID_PREFIX.values()
        if card_type_filter not in valid_arguments and card_type_filter not in 'all':
            raise ValueError(
                "function must have valid card types: 'all' (defualt), 'troop', 'building', or 'spell'"
            )
        card_level_counts = {i: 0 for i in range(1, MAX_CARD_LEVEL + 1)}

        for card in player_cards:
            # At the beginning of time, maxLevel of legendaries used to be 5.
            # While the UI has updated that to 14, the data still has it relative to that maximum.
            card_level = MAX_CARD_LEVEL - (card['maxLevel'] - card['level'])
            card_type = CARD_TYPE_ID_PREFIX[str(card['id'])[:2]]
            if card_type_filter == 'all' or card_type == card_type_filter:
                card_level_counts[card_level] += 1

        return card_level_counts

    def get_player_info(self, player_tag):
        # Debugging
        # print('Getting player info for {}'.format(player_tag))
        # This endpoint takes around 1s per request
        return self.clash_royale_client.get_player_info(player_tag)

    def get_all_player_info(self, members_list):
        # Parallise API calls to getting player info async
        with Pool(processes=self.pool_size) as pool:
            members_tags = [member['tag'] for member in members_list]
            members_info = pool.map(self.get_player_info, members_tags)

        return members_info

    def sort_list_by_card_level(self, member_cards_ranked):
        sorted_list = copy.deepcopy(member_cards_ranked)
        return sorted(sorted_list, key=cmp_to_key(compare_card_levels))

    # pre-condition: clan_tag should not have # and all caps
    def get_clan_cards_rank(self, clan_tag, card_type_filter='all'):
        clan_info = self.clash_royale_client.get_clan_info(clan_tag)
        members_list = clan_info['memberList']
        members_info = self.get_all_player_info(members_list)

        member_cards_ranked = []
        for member in members_info:
            member_card_levels = {
                'tag': member['tag'],
                'name': member['name'],
                'card_level_counts': self.get_card_level_counts(member['cards'], card_type_filter)
            }
            member_cards_ranked.append(member_card_levels)
            # debugging
            # print(member_card_levels)

        # Rank members then return results
        member_cards_ranked = self.sort_list_by_card_level(member_cards_ranked)

        return clan_info, member_cards_ranked
    '''
    River Race Player Activity History Functions
    '''
    def clan_river_race_history(self, clan_tag: str, past_weeks: int = 4) -> Tuple[Dict[str, Any], Dict[str, PlayerActivity]]:
        clan_players_war_history = {}
        clan_info = self.clash_royale_client.get_clan_info(clan_tag)
        members_list = clan_info['memberList']
        for member in members_list:
            clan_players_war_history[member['tag']] = PlayerActivity(
                tag = member['tag'],
                name = member['name'],
                role = member['role'],
                exp_level = member['expLevel'],
                fame_hist = [None]* past_weeks,
                boat_attacks_hist = [None]* past_weeks
            )
        return clan_info, self.past_weeks_clan_war(clan_players_war_history, clan_tag, past_weeks)

    def past_weeks_clan_war(self, clan_players_war_history: Dict[str, PlayerActivity], clan_tag: str, past_weeks: int = 4) -> Dict[str, PlayerActivity]:
        client_race_log_api_response = self.clash_royale_client.get_river_race_log(clan_tag)
        grouped_clan_wars = client_race_log_api_response['items'][:past_weeks]
        current_week = 0
        # First loop splits the clan wars into specific week
        for clan_war in grouped_clan_wars:
            # Second loop identifies the clan within the clan war
            for standing in clan_war['standings']:
                clan = standing['clan']
                if clan_tag.upper() in clan['tag']:
                    # Third Grab all the participants from the list and store it into the output object
                    for participant in clan['participants']:
                        if participant['tag'] in clan_players_war_history:
                            clan_players_war_history[participant['tag']].fame_hist[current_week] = participant['fame']
                            clan_players_war_history[participant['tag']].boat_attacks_hist[current_week] = participant['boatAttacks']
                    break
            current_week += 1
        # Computing War active, elder worthy, and average fame
        for player_tag in clan_players_war_history:
            player = clan_players_war_history[player_tag]
            player.war_active = compute_war_active(player.fame_hist)
            player.elder_worthy = compute_elder_worthy(player.fame_hist)
            player.avg_fame = compute_average_fame(player.fame_hist)
        return clan_players_war_history