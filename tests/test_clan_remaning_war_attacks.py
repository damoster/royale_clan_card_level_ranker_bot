
import unittest
from mockito import when
from clash_royale_service import ClashRoyaleService
from resources import clash_royale_client_currentriverrace, clash_royale_client_responses


class TestClanRemainingWarAttacks(unittest.TestCase):

    def test_get_participated(self):
        service = ClashRoyaleService()
        participants = [
            {"decksUsedToday": 3},
            {"decksUsedToday": 4},
            {"decksUsedToday": 0},
            {"decksUsedToday": 1}
        ]
        assert service._get_participated(participants) == 3

    def test_get_participated_no_participants(self):
        service = ClashRoyaleService()
        participants = [
            {"decksUsedToday": 0},
            {"decksUsedToday": 0},
            {"decksUsedToday": 0},
            {"decksUsedToday": 0}
        ]
        assert service._get_participated(participants) == 0

    def test_get_players_remaining(self):
        service = ClashRoyaleService()
        participants = [
            {"tag": "A", "decksUsedToday": 1},
            {"tag": "B", "decksUsedToday": 2},
            {"tag": "C", "decksUsedToday": 4},
            # Suppose this player D left the clan
            {"tag": "D", "decksUsedToday": 4}
        ]
        members_list = [
            {"tag": "B"},
            {"tag": "A"},
            {"tag": "C"}
        ]
        assert service._get_players_remaining(participants, members_list) == 2
    
    def test_clan_remaining_war_attacks(self):
        service = ClashRoyaleService()
        clan_tag = "#9GULPJ9L"
        other_clan_tag = {
            "PERU CB": "#P8UGJRGY",
            "A Lithuania": "#UQ8VVR",
            "Red Hot Chile": "#PR2U99V",
            "Royal Crusade": "#2ULLJPUC",
            "AUSCLAN": "#9GULPJ9L"
        }
        # Mock API responses and certain function calls
        when(service.clash_royale_client).get_current_river_race(clan_tag).thenReturn(
            clash_royale_client_currentriverrace.CURRENT_RIVER_RACE_API_RESPONSE
        )
        # MOCK CLAN INFO RESPONSE FOR PERU CB
        when(service.clash_royale_client).get_clan_info(other_clan_tag["PERU CB"]).thenReturn(
            clash_royale_client_responses.PER_CLAN_INFO_API_RESPONSE
        )
        # MOCK CLAN INFO RESPONSE FOR A Lithuania
        when(service.clash_royale_client).get_clan_info(other_clan_tag["A Lithuania"]).thenReturn(
            clash_royale_client_responses.LIT_CLAN_INFO_API_RESPONSE
        )
        # MOCK CLAN INFO RESPONSE FOR Red Hot Chile
        when(service.clash_royale_client).get_clan_info(other_clan_tag["Red Hot Chile"]).thenReturn(
            clash_royale_client_responses.RED_CLAN_INFO_API_RESPONSE
        )
        # MOCK CLAN INFO RESPONSE FOR Royal Crusade
        when(service.clash_royale_client).get_clan_info(other_clan_tag["Royal Crusade"]).thenReturn(
            clash_royale_client_responses.ROY_CLAN_INFO_API_RESPONSE
        )
        # MOCK CLAN INFO RESPONSE FOR AUSCLAN
        when(service.clash_royale_client).get_clan_info(clan_tag).thenReturn(
            clash_royale_client_responses.CLAN_INFO_API_RESPONSE
        )

        service.clan_remaining_war_attacks(clan_tag)


        
        assert 1 == 1
