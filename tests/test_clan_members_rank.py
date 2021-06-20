import unittest
from mockito import when

from clan_members_rank import ClanMembersRanker, card_count_comparator, compare_card_levels
from tests.resources import clash_royale_client_responses

# This test data here is setup so that ranking cards from highest to lowest should give player3, player1 then player 2
player1 = {
    'tag': '#PL4Y3R1',
    'name': 'player1',
    'card_level_counts': {13: 17, 12: 28, 11: 11, 10: 4, 9: 1, 8: 2, 7: 8, 6: 0, 5: 0, 4: 0, 3: 0, 2: 9, 1: 0}
}
player2 = {
    'tag': '#PL4Y3R2',
    'name': 'player2',
    'card_level_counts': {13: 17, 12: 28, 11: 11, 10: 4, 9: 1, 8: 2, 7: 8, 6: 0, 5: 0, 4: 0, 3: 0, 2: 7, 1: 0}
}
player3 = {
    'tag': '#PL4Y3R3',
    'name': 'player3',
    'card_level_counts': {13: 30, 12: 8, 11: 32, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
}
player4 = {
    'tag': '#PL4Y3R4',
    'name': 'player4',
    'card_level_counts': {13: 30, 12: 8, 11: 32, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
}


class TestClanMembersRanker(unittest.TestCase):

    def test_card_count_comparator(self):
        # Since descending, result should be positive if a < b
        self.assertTrue(card_count_comparator(4, 7) > 0)
        self.assertTrue(card_count_comparator(12, 7) < 0)
        self.assertTrue(card_count_comparator(12, 12) == 0)

    def test_compare_card_levels(self):
        # player1 should be ranked higher than player2
        self.assertTrue(compare_card_levels(player1, player2) < 0)
        # player3 should be ranked higher than player2
        self.assertTrue(compare_card_levels(player3, player2) < 0)
        # player1 should be ranked lower than player3
        self.assertTrue(compare_card_levels(player1, player3) > 0)
        # player3 and player4 should have the same rank
        self.assertTrue(compare_card_levels(player3, player4) == 0)

    def test_get_card_level_counts(self):
        # given
        expected_card_level_counts = {1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1, 8: 2, 9: 6, 10: 27, 11: 28, 12: 24, 13: 12}
        player_cards = clash_royale_client_responses.PLAYER_2_RESPONSE['cards']

        # when
        clanMembersRanker = ClanMembersRanker()
        card_level_counts = clanMembersRanker.get_card_level_counts(player_cards)

        # then
        self.assertEqual(card_level_counts, expected_card_level_counts)

    def test_get_clan_cards_rank(self):
        clanMembersRanker = ClanMembersRanker()
        clan_tag = "#S0M3CL4N"

        # Mock API responses and certain function calls
        when(clanMembersRanker.clash_royale_client).get_clan_members(clan_tag).thenReturn(
            clash_royale_client_responses.CLAN_MEMBERS_API_RESPONSE
        )
        when(clanMembersRanker).get_player_info('#YV9GU2VG').thenReturn(
            clash_royale_client_responses.PLAYER_1_RESPONSE
        )
        when(clanMembersRanker).get_player_info('#8VUG0GQRY').thenReturn(
            clash_royale_client_responses.PLAYER_2_RESPONSE
        )
        when(clanMembersRanker).get_player_info('#LYJVYUUUR').thenReturn(
            clash_royale_client_responses.PLAYER_3_RESPONSE
        )

        # Expected sort order (in terms of card counts is player3, player1, player2)
        member_cards_ranked = clanMembersRanker.get_clan_cards_rank(clan_tag)
        self.assertEqual([m['tag'] for m in member_cards_ranked], ['#LYJVYUUUR', '#YV9GU2VG', '#8VUG0GQRY'])


if __name__ == '__main__':
    unittest.main()
