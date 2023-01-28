
import pytest
import unittest
from mockito import when
from clash_royale_service import ClashRoyaleService
from tests.resources import clash_royale_client_currentriverrace, clash_royale_client_responses


class TestClanRemainingWarAttacks(object):

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
            {"tag": "A", "name": "player_A", "decksUsedToday": 1},
            {"tag": "B", "name": "player_B", "decksUsedToday": 2},
            {"tag": "C", "name": "player_C", "decksUsedToday": 4},
            # Suppose this player D left the clan
            {"tag": "D", "name": "player_D", "decksUsedToday": 4},
            # Suppose player E left the clan but did 1 war attack
            {"tag": "E", "name": "player_E", "decksUsedToday": 1}
        ]
        members_list = [
            {"tag": "B", "lastSeen": "20221206T202149.000Z"},
            {"tag": "A", "lastSeen": "20221206T202149.000Z"},
            {"tag": "C", "lastSeen": "20221206T202149.000Z"}
        ]

        players_remaining = service._get_players_remaining(participants, members_list)
        # Includes player A,B, and E
        assert len(players_remaining) == 3
        players_remaining = service._get_players_remaining(participants, members_list, True)
        # Only Includes player A and B as E is out of the clan (excluded from the third argument in_clan)
        assert len(players_remaining) == 2

    @pytest.mark.parametrize(
        "members_list, expected_decks_remaining",
        [
            # Test 1 - All players are in clan and used some number of decks
            (
                [
                    {"tag": "B"},
                    {"tag": "A"},
                    {"tag": "C"},
                    {"tag": "D"},
                    {"tag": "E"}
                ],
                191
            ),
            # Test 2 - Since D left, deckUsedToday for player D is 4 -> (200 - (1+2+4+4))
            (
                [
                    {"tag": "B"},
                    {"tag": "A"},
                    {"tag": "C"}
                ],
                189
            ),
            # Test 3 - Since E left and not used any decks, decks remaining is -> (200 - (1+2+4+2))
            (
                [
                    {"tag": "A"},
                    {"tag": "B"},
                    {"tag": "C"},
                    {"tag": "D"}
                ],
                191
            )
        ]
    )
    def test_get_decks_remaining(self, members_list, expected_decks_remaining):
        service = ClashRoyaleService()
        participants = [
            {"tag": "A", "decksUsedToday": 1},
            {"tag": "B", "decksUsedToday": 2},
            {"tag": "C", "decksUsedToday": 4},
            {"tag": "D", "decksUsedToday": 2},
            {"tag": "E", "decksUsedToday": 0}
        ]
        assert service._get_decks_remaining(
            participants, members_list) == expected_decks_remaining

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

        # Note: Commented these mock responses out because it is replaced with the multi-processing function on _get_all_clan_info. A python multi-processing bug
        # # MOCK CLAN INFO RESPONSE FOR PERU CB
        # when(service.clash_royale_client).get_clan_info(other_clan_tag["PERU CB"]).thenReturn(
        #     clash_royale_client_responses.PER_CLAN_INFO_API_RESPONSE
        # )
        # # MOCK CLAN INFO RESPONSE FOR A Lithuania
        # when(service.clash_royale_client).get_clan_info(other_clan_tag["A Lithuania"]).thenReturn(
        #     clash_royale_client_responses.LIT_CLAN_INFO_API_RESPONSE
        # )
        # # MOCK CLAN INFO RESPONSE FOR Red Hot Chile
        # when(service.clash_royale_client).get_clan_info(other_clan_tag["Red Hot Chile"]).thenReturn(
        #     clash_royale_client_responses.RED_CLAN_INFO_API_RESPONSE
        # )
        # # MOCK CLAN INFO RESPONSE FOR Royal Crusade
        # when(service.clash_royale_client).get_clan_info(other_clan_tag["Royal Crusade"]).thenReturn(
        #     clash_royale_client_responses.ROY_CLAN_INFO_API_RESPONSE
        # )
        # # MOCK CLAN INFO RESPONSE FOR AUSCLAN
        # when(service.clash_royale_client).get_clan_info(clan_tag).thenReturn(
        #     clash_royale_client_responses.CLAN_INFO_API_RESPONSE
        # )

        when(service)._get_all_clan_info(['#P8UGJRGY', '#UQ8VVR', '#PR2U99V', '#2ULLJPUC', '#9GULPJ9L']).thenReturn(
            [
                clash_royale_client_responses.PER_CLAN_INFO_API_RESPONSE,
                clash_royale_client_responses.LIT_CLAN_INFO_API_RESPONSE,
                clash_royale_client_responses.RED_CLAN_INFO_API_RESPONSE,
                clash_royale_client_responses.ROY_CLAN_INFO_API_RESPONSE,
                clash_royale_client_responses.CLAN_INFO_API_RESPONSE
            ]
        )

        all_clan_attacks = service.clan_players_unfinished_war_attacks(clan_tag)

        # Test Cases 1 - Ausclan
        # All 3 players partipated, 191 decks remaining (200 - (4+3+2)), 2 players remaining
        organised_all_clan_attacks = {
            clan_attacks.tag: clan_attacks for clan_attacks in all_clan_attacks}
        assert organised_all_clan_attacks[other_clan_tag["AUSCLAN"]
                                          ].participated == 3
        assert organised_all_clan_attacks[other_clan_tag["AUSCLAN"]
                                          ].decks_remaining == 191
        assert organised_all_clan_attacks[other_clan_tag["AUSCLAN"]
                                          ].players_remaining == 2

        # Test Cases 2 - PERU CB
        # All 3 players partipated (one left the clan doing 2 attacks), 189 decks remaining (200 - (4+4+3)), 1 player remaining
        assert organised_all_clan_attacks[other_clan_tag["PERU CB"]
                                          ].participated == 3
        assert organised_all_clan_attacks[other_clan_tag["PERU CB"]
                                          ].decks_remaining == 189
        assert organised_all_clan_attacks[other_clan_tag["PERU CB"]
                                          ].players_remaining == 1

        # Test Cases 3 - A Lithuania
        # 2 players partipated, 193 decks remaining (200 - (4+3)), 2 players remaining
        assert organised_all_clan_attacks[other_clan_tag["A Lithuania"]
                                          ].participated == 2
        assert organised_all_clan_attacks[other_clan_tag["A Lithuania"]
                                          ].decks_remaining == 193
        assert organised_all_clan_attacks[other_clan_tag["A Lithuania"]
                                          ].players_remaining == 2

        # Test Case 4 - Red Hot Chile
        # 2 players participated (one left clan doing 0 attacks), 193 decks remaining (200 - (4+3)), 1 player remaining
        assert organised_all_clan_attacks[other_clan_tag["Red Hot Chile"]
                                          ].participated == 2
        assert organised_all_clan_attacks[other_clan_tag["Red Hot Chile"]
                                          ].decks_remaining == 193
        assert organised_all_clan_attacks[other_clan_tag["Red Hot Chile"]
                                          ].players_remaining == 1

        # Test Case 5 - Testing the sorting order based on the medals decending
        sorted_list = [
            clan_attacks.medals for clan_attacks in all_clan_attacks]
        for i in range(len(sorted_list) - 1):
            if sorted_list[i] < sorted_list[i+1]:
                assert False
