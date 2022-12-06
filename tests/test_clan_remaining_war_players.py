
import pytest
import unittest
from mockito import when
from clash_royale_service import ClashRoyaleService
from tests.resources import clash_royale_client_currentriverrace, clash_royale_client_responses


class TestClanRemainingWarPlayers(unittest.TestCase):
    def test_clan_players_remaining_war_attacks(self):
        service = ClashRoyaleService()
        clan_tag = "#9GULPJ9L"

        # Mock API responses and certain function calls
        when(service.clash_royale_client).get_current_river_race(clan_tag).thenReturn(
            clash_royale_client_currentriverrace.CURRENT_RIVER_RACE_API_RESPONSE
        )
        when(service.clash_royale_client).get_clan_info(clan_tag).thenReturn(
            clash_royale_client_responses.CLAN_INFO_API_RESPONSE
        )

        all_current_war_players_output = service.clan_players_remaining_war_attacks(clan_tag)
        # Note 1: there are three players participated in the war, one of them completed all attacks and hence the name is not listed
        # Note 2: two players have not completed all the war attacks, hence there are two entries in the list
        player_1 = all_current_war_players_output[0]
        player_2 = all_current_war_players_output[1]
        self.assertEqual(len(all_current_war_players_output),2)
        self.assertTrue(player_1.decks_used_today == 3)
        self.assertTrue(player_2.decks_used_today == 2)
        self.assertTrue(player_1.decks_used_today >= player_2.decks_used_today)