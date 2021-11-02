import unittest
from mockito import when

from clan_members_rank import ClanMembersRanker, card_count_comparator, compare_card_levels
from tests.resources import clash_royale_client_responses

# This test data here is setup so that ranking cards from highest to lowest should give player3, player1 then player 2
player1 = {
    'tag': '#PL4Y3R1',
    'name': 'player1',
    'card_level_counts': {14: 3, 13: 17, 12: 28, 11: 11, 10: 4, 9: 1, 8: 2, 7: 8, 6: 0, 5: 0, 4: 0, 3: 0, 2: 9, 1: 0}
}
player2 = {
    'tag': '#PL4Y3R2',
    'name': 'player2',
    'card_level_counts': {14: 3, 13: 17, 12: 28, 11: 11, 10: 4, 9: 1, 8: 2, 7: 8, 6: 0, 5: 0, 4: 0, 3: 0, 2: 7, 1: 0}
}
player3 = {
    'tag': '#PL4Y3R3',
    'name': 'player3',
    'card_level_counts': {14: 5, 13: 30, 12: 8, 11: 32, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
}
player4 = {
    'tag': '#PL4Y3R4',
    'name': 'player4',
    'card_level_counts': {14: 5, 13: 30, 12: 8, 11: 32, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
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
        expected_card_level_counts = {
            1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 1, 8: 2, 9: 4, 10: 26, 11: 18, 12: 19, 13: 32, 14: 0}
        filtered_troop_expected_card_level_counts = {
            1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0, 7: 1, 8: 1, 9: 2, 10: 16, 11: 13, 12: 14, 13: 23, 14: 0}
        filtered_spell_expected_card_level_counts = {
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 3, 11: 3, 12: 4, 13: 7, 14: 0}
        filtered_building_expected_card_level_counts = {
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 7, 11: 2, 12: 1, 13: 2, 14: 0}

        filtered_troop_expected_card_level_counts_p3 = {
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 2, 12: 10, 13: 58, 14: 4}
        filtered_spell_expected_card_level_counts_p3 = {
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 3, 13: 13, 14: 3}

        player_2_cards = clash_royale_client_responses.PLAYER_2_RESPONSE['cards']
        player_3_cards = clash_royale_client_responses.PLAYER_3_RESPONSE['cards']
        # when
        clan_members_rank = ClanMembersRanker()

        # 1. No filter test
        card_level_counts = clan_members_rank.get_card_level_counts(
            player_2_cards)
        # then
        self.assertEqual(card_level_counts, expected_card_level_counts)

        # 2. Troop filter test
        card_level_counts = clan_members_rank.get_card_level_counts(
            player_2_cards, 'troop')
        # then
        self.assertEqual(card_level_counts,
                         filtered_troop_expected_card_level_counts)

        # 3. Spell filter test
        card_level_counts = clan_members_rank.get_card_level_counts(
            player_2_cards, 'spell')
        # then
        self.assertEqual(card_level_counts,
                         filtered_spell_expected_card_level_counts)

        # 4. Building filter test
        card_level_counts = clan_members_rank.get_card_level_counts(
            player_2_cards, 'building')
        # then
        self.assertEqual(card_level_counts,
                         filtered_building_expected_card_level_counts)

        # 5. Invalid filter test
        with self.assertRaises(ValueError) as context:
            card_level_counts = clan_members_rank.get_card_level_counts(
                player_2_cards, 'randomString')
            self.assertTrue(
                "function must have valid card types: 'all' (defualt), 'troop', 'building', or 'spell'"
                in context.exception)

        # Reason to test out on Player 1 is to check the correctness of the ranking for test_get_clan_cards_rank assertion
        # 6. Player 1 troop test
        card_level_counts = clan_members_rank.get_card_level_counts(
            player_3_cards, 'troop')
        # then
        self.assertEqual(card_level_counts,
                         filtered_troop_expected_card_level_counts_p3)
        # 7. Player 1 spell test
        card_level_counts = clan_members_rank.get_card_level_counts(
            player_3_cards, 'spell')
        # then
        self.assertEqual(card_level_counts,
                         filtered_spell_expected_card_level_counts_p3)

    def test_get_clan_cards_rank(self):
        clan_members_rank = ClanMembersRanker()
        clan_tag = "#S0M3CL4N"

        # Mock API responses and certain function calls
        when(clan_members_rank.clash_royale_client).get_clan_info(clan_tag).thenReturn(
            clash_royale_client_responses.CLAN_INFO_API_RESPONSE
        )
        when(clan_members_rank).get_all_player_info(
            clash_royale_client_responses.CLAN_INFO_API_RESPONSE['memberList']
        ).thenReturn(
            [
                clash_royale_client_responses.PLAYER_1_RESPONSE,
                clash_royale_client_responses.PLAYER_2_RESPONSE,
                clash_royale_client_responses.PLAYER_3_RESPONSE
            ]
        )

        # 1. Expected sort order (in terms of card counts is player3, player1, player2)
        clan_info, member_cards_ranked = clan_members_rank.get_clan_cards_rank(
            clan_tag)
        self.assertEqual(
            clan_info, clash_royale_client_responses.CLAN_INFO_API_RESPONSE)
        self.assertEqual([m['tag'] for m in member_cards_ranked], [
                         '#LYJVYUUUR', '#YV9GU2VG', '#8VUG0GQRY'])

        # 2. Card Type Filter Test with 'troop' - Expected sort order (in terms of card counts is player1, player2, player3)
        clan_info, member_cards_ranked = clan_members_rank.get_clan_cards_rank(
            clan_tag, 'troop')
        self.assertEqual([m['tag'] for m in member_cards_ranked], [
                         '#LYJVYUUUR', '#YV9GU2VG', '#8VUG0GQRY'])

        # 3. Card Type Filter Test with 'spell' - Expected sort order (in terms of card counts is player1, player2, player3)
        clan_info, member_cards_ranked = clan_members_rank.get_clan_cards_rank(
            clan_tag, card_type_filter='spell')
        self.assertEqual([m['tag'] for m in member_cards_ranked], [
                         '#LYJVYUUUR', '#8VUG0GQRY', '#YV9GU2VG'])

        # 4. Card Type Filter Test with 'building' - Expected sort order (in terms of card counts is player1, player2, player3)
        clan_info, member_cards_ranked = clan_members_rank.get_clan_cards_rank(
            clan_tag, card_type_filter='building')
        self.assertEqual([m['tag'] for m in member_cards_ranked], [
                         '#LYJVYUUUR', '#8VUG0GQRY', '#YV9GU2VG'])

        # 5. Card Type Filter Test with Invalid input
        with self.assertRaises(ValueError) as context:
            clan_info, member_cards_ranked = clan_members_rank.get_clan_cards_rank(
                clan_tag, card_type_filter='randomstring')
            self.assertTrue(
                'function must have valid card types: all (defualt), troops, buildings, or spells' in context.exception)


if __name__ == '__main__':
    unittest.main()
