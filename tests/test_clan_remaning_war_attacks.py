

import unittest
import unittest
from clash_royale_service import ClashRoyaleService


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
