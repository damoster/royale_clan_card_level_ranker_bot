import unittest
from mockito import when

from tests.resources import clash_royale_client_riverracelog, clash_royale_client_responses
from clash_royale_service import ClashRoyaleService

class TestRiverRaceLog(unittest.TestCase):
    def test_past_weeks_clan_war(self):
        clan_members_war = ClashRoyaleService()
        clan_tag = "#9GULPJ9L"
        # Mock API responses and certain function calls
        when(clan_members_war.clash_royale_client).get_river_race_log(clan_tag).thenReturn(
            clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE
        )

        players_war_history = clan_members_war.past_weeks_clan_war(clan_tag)
        # Testing for the length returned. Should be 4 (weeks) of war history returned
        self.assertEqual(len(players_war_history), 90)
        pass
    def test_clan_river_race_history(self):
        clan_members_war = ClashRoyaleService()
        clan_tag = "#9GULPJ9L"

        # Mock API responses and certain function calls
        when(clan_members_war.clash_royale_client).get_river_race_log(clan_tag).thenReturn(
            clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE
        )
        when(clan_members_war.clash_royale_client).get_clan_info(clan_tag).thenReturn(
            clash_royale_client_responses.CLAN_INFO_API_RESPONSE
        )

        clan_war_history = clan_members_war.clan_river_race_history(clan_tag)
        pass

if __name__ == '__main__':
    unittest.main()
    