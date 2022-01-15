import unittest
from mockito import when

from tests.resources import clash_royale_client_riverracelog
from clan_members_war import ClanMembersWar, get_river_race_log

class TestRiverRaceLog(unittest.TestCase):
    def test_river_race(self):
        clan_members_war = ClanMembersWar()
        when(clan_members_war.get_river_race_log).thenReturn(
            clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE
        )

if __name__ == '__main__':
    unittest.main()
    