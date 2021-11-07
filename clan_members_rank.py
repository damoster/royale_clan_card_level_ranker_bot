import copy
from functools import cmp_to_key
from multiprocessing import Pool

from clash_royale_client import ClashRoyaleClient
from common.schemas import CARD_TYPE_ID_PREFIX, MAX_CARD_LEVEL


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


class ClanMembersRanker:
    def __init__(self):
        # Using pool size of 50 since that is the player limit in a clan
        self.pool_size = 50  # Using for I/O bound task (API requests)
        self.clash_royale_client = ClashRoyaleClient()

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
