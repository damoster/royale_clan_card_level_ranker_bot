from clash_royale_client import ClashRoyaleClient

from time import sleep
from functools import cmp_to_key

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
    card_level = 13
    while compare_result == 0 and card_level > 0:
        p1_card_count = p1['card_level_counts'][card_level]
        p2_card_count = p2['card_level_counts'][card_level]
        compare_result = card_count_comparator(p1_card_count, p2_card_count)
        card_level -= 1
    return compare_result

class ClanMembersRanker:
    def __init__(self):
        self.clash_royale_client = ClashRoyaleClient()

    def get_card_level_counts(self, player_tag):
        member_details = self.clash_royale_client.get_player_info(player_tag)
        member_cards = member_details['cards']

        # TODO: split into card types, e.g.
        # card_level_counts = { 13: { 'totalCount': 'spellCount': x, 'buildingCount': y, 'troopCount': z }, etc. }
        card_level_counts = { i: 0 for i in range(1, 14) }

        for card in member_cards:
            # At the beginning of time, maxLevel of legendaries used to be 5. While the UI has updated that to 13, the data still has it relative to that maximum.
            card_level = 13 - (card['maxLevel'] - card['level'])
            card_level_counts[card_level] += 1

        return card_level_counts

    # pre-condition: clan_tag should not have # and all caps
    def get_clan_cards_rank(self, clan_tag):
        members_list = self.clash_royale_client.get_clan_members(clan_tag)['items']
        member_cards_ranked = []

        for member in members_list:
            member_card_levels = {
                'tag': member['tag'],
                'name': member['name'],
                # 'card_level_counts': card_level_counts
                'card_level_counts': self.get_card_level_counts(member['tag'])
            }
            member_cards_ranked.append(member_card_levels)
            #debugging
            print(member_card_levels)

            # Sleep 1 milliseconds before next request (don't wanna get rate limited lol...or maybe it already rate limits....)
            sleep(0.001)

        # Rank members then return results
        member_cards_ranked.sort(key=cmp_to_key(compare_card_levels))

        return member_cards_ranked

