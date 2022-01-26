import unittest
from mockito import when

from tests.resources import clash_royale_client_riverracelog, clash_royale_client_responses
from clash_royale_service import ClashRoyaleService
from common.schemas import PlayerActivity

# Test Data here
mock_clan_players_war_history = {
    '#8VUG0GQRY': PlayerActivity(tag='#8VUG0GQRY', name='joseph', role='elder', exp_level=13, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]), 
    '#LYJVYUUUR': PlayerActivity(tag='#LYJVYUUUR', name='ZEPOL 1244', role='coLeader', exp_level=13, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]),
    '#SOMENOBDY': PlayerActivity(tag='#SOMENOBDY', name='NOBODY', role='member', exp_level=10, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]),
    '#2YR9QLQUU': PlayerActivity(tag='#2YR9QLQUU', name='~Jules~', role='leader', exp_level=14, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None]),
    '#Q0QP02V2Q': PlayerActivity(tag='#Q0QP02V2Q', name='Nacho', role='coLeader', exp_level=14, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None])
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
        # Testing for the length returned. Should be 5 players returned
        self.assertEqual(len(clan_players_war_history), 5)

        ''' Test cases
            Joseph - fully active
            Zepol - did all 4 weeks of war, but one is < 1200
            None - didn't do any war
            Jules - joined half way, some of the weeks are none
            Nacho - joined 3 weeks ago and performed poor
        '''
        joseph_activity = PlayerActivity(tag='#8VUG0GQRY', name='joseph', role='elder', exp_level=13, fame_hist=[2650, 2800, 2500, 3100], boat_attacks_hist=[0, 0, 0, 0], war_active=True, elder_worthy=True, avg_fame=2762.5)
        zepol_activity = PlayerActivity(tag='#LYJVYUUUR', name='ZEPOL 1244', role='coLeader', exp_level=13, fame_hist=[2800, 1100, 2250, 3100], boat_attacks_hist=[0, 0, 0, 0], war_active=False, elder_worthy=False, avg_fame=2312.5)
        none_activity = PlayerActivity(tag='#SOMENOBDY', name='NOBODY', role='member', exp_level=10, fame_hist=[None, None, None, None], boat_attacks_hist=[None, None, None, None], war_active=True, elder_worthy=False, avg_fame=-1)
        jules_activity = PlayerActivity(tag='#2YR9QLQUU', name='~Jules~', role='leader', exp_level=14, fame_hist=[2750, 2400, None, None], boat_attacks_hist=[0, 0, None, None], war_active=True, elder_worthy=False, avg_fame=2575.0)
        nacho_activity = PlayerActivity(tag='#Q0QP02V2Q', name='Nacho', role='coLeader', exp_level=14, fame_hist=[800, 2100, 1000, None], boat_attacks_hist=[0, 0, 0, None], war_active=False, elder_worthy=False, avg_fame=1300.0)

        self.assertEqual(clan_players_war_history['#8VUG0GQRY'], joseph_activity)
        self.assertEqual(clan_players_war_history['#LYJVYUUUR'], zepol_activity)
        self.assertEqual(clan_players_war_history['#SOMENOBDY'], none_activity)
        self.assertEqual(clan_players_war_history['#2YR9QLQUU'], jules_activity)
        self.assertEqual(clan_players_war_history['#Q0QP02V2Q'], nacho_activity)

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

        # Testing if three players is returned based on get clan info
        clan_players_war_history = clan_members_war.clan_river_race_history(clan_tag)
        self.assertEqual(len(clan_players_war_history), 3)

        # Testing for changing the past week to longer period i.e. 8
        clan_players_war_history = clan_members_war.clan_river_race_history(clan_tag, 8)
        self.assertEqual(len(clan_players_war_history['#8VUG0GQRY'].fame_hist), 8)

if __name__ == '__main__':
    unittest.main()
