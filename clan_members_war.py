from clash_royale_client import ClashRoyaleClient

def past_weeks_clan_war(race_log_api_response, clan_tag, past_weeks = 4):
    ''' Response api has the following schema:
        items []
            seasonid
            sectionIndex
            standings []
                rank
                clan
                    tag
                    name
                    participants [dict]
                        tag
                        name
                        fame
                        boatAttacks
                        decksUsed
        Logic:
            - loop through the top 4 items to get the past 4 weeks

    ''' 
    clan_wars = [item for index, item in enumerate(race_log_api_response['items']) if index < past_weeks]
    past_war_counter = 0
    clan_participants = []
    for clan_war in clan_wars:
        for standing in clan_war['standings']:
            clan = standing['clan']
            if clan['tag'] == clan_tag:
                clan_participants.append(clan)

    return clan_participants


class ClanMembersWar:
    def __init__(self):
        self.clash_royale_client = ClashRoyaleClient()
    
    def get_river_race_log(self, clan_tag):
        return True