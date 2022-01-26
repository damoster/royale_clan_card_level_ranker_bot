import unittest
from mockito import when

from tests.resources import clash_royale_client_riverracelog, clash_royale_client_responses
from clash_royale_service import ClashRoyaleService
from common.schemas import PlayerActivity

# Test Data here
mock_clan_players_war_history = {
    '#YV9GU2VG': PlayerActivity(tag='#YV9GU2VG', name='Goku', role='member', exp_level=13, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]), 
    '#8VUG0GQRY': PlayerActivity(tag='#8VUG0GQRY', name='joseph', role='elder', exp_level=13, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]), 
    '#LYJVYUUUR': PlayerActivity(tag='#LYJVYUUUR', name='ZEPOL 1244', role='coLeader', exp_level=13, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]),
    '#SOMENOBDY': PlayerActivity(tag='#SOMENOBDY', name='NOBODY', role='member', exp_level=10, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None])
}

class TestRiverRaceLog(unittest.TestCase):
    def test_past_weeks_clan_war(self):
        clan_members_war = ClashRoyaleService()
        clan_tag = "#9GULPJ9L"
        # Mock API responses and certain function calls
        when(clan_members_war.clash_royale_client).get_river_race_log(clan_tag).thenReturn(
            clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE
        )

        clan_players_war_history = clan_members_war.past_weeks_clan_war(mock_clan_players_war_history, clan_tag)
        # Testing for the length returned. Should be 4 players returned
        self.assertEqual(len(clan_players_war_history), 4)

        # Testing if fame_hist is updated for Joseph, Zepol, and Someone Who hasnt done War
        # (TODO) compare object rather than specific value
        # Test cases
        # Joseph - fully active
        # Zepol - did all 4 weeks of war, but one is < 1200
        # None - didn't do any war
        # Jules - joined half way, some of the weeks are none
        joseph_activity = PlayerActivity(tag='#8VUG0GQRY', name='joseph', role='elder', exp_level=13, fame_hist=[2650, 2800, 2500, 3100], boat_attacks_hist=[None, None, None, None], war_active=True)
        zepol_activity = PlayerActivity(tag='#LYJVYUUUR', name='ZEPOL 1244', role='coLeader', exp_level=13, fame_hist=[2800, 2200, 2250, 3100], boat_attacks_hist=[None, None, None, None], war_active=False)
        none_activity = PlayerActivity(tag='#SOMENOBDY', name='NOBODY', role='member', exp_level=10, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None], war_active=False)
        self.assertEqual(clan_players_war_history['#8VUG0GQRY'], joseph_activity)
        self.assertEqual(clan_players_war_history['#LYJVYUUUR'], zepol_activity)
        self.assertEqual(clan_players_war_history['#SOMENOBDY'], none_activity)

        # (TODO) Add test cases for Users who joined 2 weeks ago and did nothing

    def test_clan_river_race_history(self):
        clan_members_war = ClashRoyaleService()
        clan_tag = "#9GULPJ9L"

        # Mock API responses and certain function calls
        when(clan_members_war.clash_royale_client).get_clan_info(clan_tag).thenReturn(
            clash_royale_client_responses.CLAN_INFO_API_RESPONSE
        )
        when(clan_members_war.clash_royale_client).get_river_race_log(clan_tag).thenReturn(
            clash_royale_client_riverracelog.RIVER_RACE_LOG_API_RESPONSE
        )

        clan_players_war_history = clan_members_war.clan_river_race_history(clan_tag)
        self.assertEqual(len(clan_players_war_history), 3)
        self.assertEqual(clan_players_war_history['#8VUG0GQRY'].fame_hist, [2650, 2800, 2500, 3100])
        self.assertEqual(clan_players_war_history['#LYJVYUUUR'].fame_hist, [2800, 2200, 2250, 3100])

        # Testing for changing the past week to longer period i.e. 8
        clan_players_war_history = clan_members_war.clan_river_race_history(clan_tag, 8)
        self.assertEqual(len(clan_players_war_history['#8VUG0GQRY'].fame_hist), 8)
        pass

if __name__ == '__main__':
    unittest.main()
