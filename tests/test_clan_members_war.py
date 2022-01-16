import unittest
from mockito import when

from tests.resources import clash_royale_client_riverracelog
from clan_members_war import ClanMembersWar, past_weeks_clan_war

class TestRiverRaceLog(unittest.TestCase):
    def test_river_race(self):
        clan_members_war = ClanMembersWar()
        clan_tag = "#9GULPJ9L"
        # Mock API responses and certain function calls
        when(clan_members_war.clash_royale_client).get_river_race_log(clan_tag).thenReturn(
            clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE
        )
        clan_war_history = past_weeks_clan_war(clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE, clan_tag)
if __name__ == '__main__':
    unittest.main()
    