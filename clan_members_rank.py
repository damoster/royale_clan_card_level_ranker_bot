from clash_royale_client import ClashRoyaleClient

from time import sleep
from functools import cmp_to_key

TEST_CLAN_MEMBERS_RESPONSE = { "items": [
       {
         "tag":"#9VGQ89LJY",
         "name":"krudda",
         "role":"coLeader",
         "lastSeen":"20210617T092404.000Z",
         "expLevel":13,
         "trophies":4131,
         "arena":{
            "id":54000011,
            "name":"Arena 12"
         },
         "clanRank":45,
         "previousClanRank":45,
         "donations":688,
         "donationsReceived":360,
         "clanChestPoints":0
      },
      {
         "tag":"#GGY22GCV9",
         "name":"Totally a noob",
         "role":"member",
         "lastSeen":"20210614T051550.000Z",
         "expLevel":8,
         "trophies":3362,
         "arena":{
            "id":54000007,
            "name":"Arena 10"
         },
         "clanRank":46,
         "previousClanRank":47,
         "donations":0,
         "donationsReceived":40,
         "clanChestPoints":0
      },
      {
         "tag":"#UG2P2YJ",
         "name":"Dringsta",
         "role":"member",
         "lastSeen":"20210617T115825.000Z",
         "expLevel":10,
         "trophies":3290,
         "arena":{
            "id":54000007,
            "name":"Arena 10"
         },
         "clanRank":47,
         "previousClanRank":48,
         "donations":167,
         "donationsReceived":80,
         "clanChestPoints":0
      }
   ],
   "paging":{
      "cursors":{
         
      }
   }
}

TEST_PLAYER_RESPONSE = {'tag': '#8VUG0GQRY', 'name': 'joseph', 'expLevel': 13, 'trophies': 5501, 'bestTrophies': 5889, 'wins': 4022, 'losses': 2970, 'battleCount': 10229, 'threeCrownWins': 1922, 'challengeCardsWon': 3674, 'challengeMaxWins': 12, 'tournamentCardsWon': 0, 'tournamentBattleCount': 444, 'role': 'elder', 'donations': 68, 'donationsReceived': 160, 'totalDonations': 23439, 'warDayWins': 153, 'clanCardsCollected': 400381, 'clan': {'tag': '#9GULPJ9L', 'name': 'AUSCLAN', 'badgeId': 16000025}, 'arena': {'id': 54000013, 'name': 'Challenger II'}, 'leagueStatistics': {'currentSeason': {'trophies': 5501, 'bestTrophies': 5501}, 'previousSeason': {'id': '2021-05', 'trophies': 5671, 'bestTrophies': 5802}, 'bestSeason': {'id': '2020-02', 'trophies': 5757}}, 'badges': [{'name': '1000Wins', 'progress': 4022}, {'name': 'Played1Year', 'progress': 1388}, {'name': 'Played2Years', 'progress': 1388}, {'name': 'Played3Years', 'progress': 1388}, {'name': 'TopLeague', 'progress': 5889}, {'name': 'ClanWarWins', 'level': 3, 'maxLevel': 3, 'progress': 153}], 'achievements': [{'name': 'Team Player', 'stars': 3, 'value': 10, 'target': 1, 'info': 'Join a Clan', 'completionInfo': None}, {'name': 'Friend in Need', 'stars': 3, 'value': 23439, 'target': 2500, 'info': 'Donate 2500 cards', 'completionInfo': None}, {'name': 'Road to Glory', 'stars': 3, 'value': 18, 'target': 6, 'info': 'Reach Arena 6', 'completionInfo': None}, {'name': 'Gatherer', 'stars': 3, 'value': 103, 'target': 40, 'info': 'Collect 40 cards', 'completionInfo': None}, {'name': 'TV Royale', 'stars': 3, 'value': 1, 'target': 1, 'info': 'Watch a TV Royale Replay', 'completionInfo': None}, {'name': 'Tournament Rewards', 'stars': 0, 'value': 0, 'target': 1000, 'info': 'Win 1000 cards from tournaments', 'completionInfo': None}, {'name': 'Tournament Host', 'stars': 0, 'value': 0, 'target': 1, 'info': 'Create and finish one tournament', 'completionInfo': None}, {'name': 'Tournament Player', 'stars': 3, 'value': 5, 'target': 1, 'info': 'Join a tournament', 'completionInfo': None}, {'name': 'Challenge Streak', 'stars': 3, 'value': 20, 'target': 12, 'info': 'Get 12 wins in a single Challenge', 'completionInfo': None}, {'name': 'Practice with Friends', 'stars': 3, 'value': 22, 'target': 10, 'info': 'Win 10 Friendly Battles', 'completionInfo': None}, {'name': 'Special Challenge', 'stars': 3, 'value': 247, 'target': 5, 'info': 'Participate in 5 unique Special Event Challenges', 'completionInfo': None}, {'name': 'Friend in Need II', 'stars': 2, 'value': 23439, 'target': 25000, 'info': 'Donate 25000 cards', 'completionInfo': None}], 'cards': [{'name': 'Elixir Collector', 'id': 27000007, 'level': 8, 'maxLevel': 11, 'count': 934, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/BGLo3Grsp81c72EpxLLk-Sofk3VY56zahnUNOv3JcT0.png'}}, {'name': 'Inferno Tower', 'id': 27000003, 'level': 9, 'maxLevel': 11, 'count': 509, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png'}}, {'name': 'Barbarians', 'id': 26000008, 'level': 10, 'maxLevel': 13, 'count': 5687, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/TvJsuu2S4yhyk1jVYUAQwdKOnW4U77KuWWOTPOWnwfI.png'}}, {'name': 'Bowler', 'id': 26000034, 'level': 5, 'maxLevel': 8, 'count': 110, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/SU4qFXmbQXWjvASxVI6z9IJuTYolx4A0MKK90sTIE88.png'}}, {'name': 'Royal Giant', 'id': 26000024, 'level': 12, 'maxLevel': 13, 'count': 4670, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/mnlRaNtmfpQx2e6mp70sLd0ND-pKPF70Cf87_agEKg4.png'}}, {'name': 'Giant Skeleton', 'id': 26000020, 'level': 6, 'maxLevel': 8, 'count': 96, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/0p0gd0XaVRu1Hb1iSG1hTYbz2AN6aEiZnhaAib5O8Z8.png'}}, {'name': 'Mini P.E.K.K.A', 'id': 26000018, 'level': 10, 'maxLevel': 11, 'count': 113, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png'}}, {'name': 'Night Witch', 'id': 26000048, 'level': 4, 'maxLevel': 5, 'count': 20, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/NpCrXDEDBBJgNv9QrBAcJmmMFbS7pe3KCY8xJ5VB18A.png'}}, {'name': 'Skeleton Army', 'id': 26000012, 'level': 6, 'maxLevel': 8, 'count': 92, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png'}}, {'name': 'Tornado', 'id': 28000012, 'level': 6, 'maxLevel': 8, 'count': 61, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/QJB-QK1QJHdw4hjpAwVSyZBozc2ZWAR9pQ-SMUyKaT0.png'}}], 'currentFavouriteCard': {'name': 'Golem', 'id': 26000009, 'maxLevel': 8, 'iconUrls': {'medium': 'https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png'}}, 'starPoints': 5352}

# NOTE: we want the highest level to come first (sort descending)
def compare_card_count(count1, count2):
    if count1 < count2:
        return 1
    elif count1 > count2:
        return -1
    else: 
        return 0

def compare_card_levels(p1, p2):
    compare_result = 0
    card_level = 13
    # while compare_result == 0 and card_level > 10: # TODO uncomment for testing data
    while compare_result == 0 and card_level > 0:
        p1_card_count = p1['member_card_levels'][card_level]
        p2_card_count = p2['member_card_levels'][card_level]
        compare_result = compare_card_count(p1_card_count, p2_card_count)
        card_level -= 1
    return compare_result

class ClanMembersRanker:
    def __init__(self):
        self.clash_royale_client = ClashRoyaleClient()

    # pre-condition: clan_tag should not have # and all caps
    def getClanCardsRank(self, clan_tag):
        members_list = self.clash_royale_client.getClanMembers(clan_tag)['items']
        # members_list = TEST_CLAN_MEMBERS_RESPONSE['items']
        member_cards_ranked = []

        for member in members_list:
            # break # TODO: Skipping this for now
            player_tag_minus_hash = member['tag'].replace('#','')
            
            # TODO: split into card types, e.g.
            # member_card_levels = { 13: { 'totalCount': 'spellCount': x, 'buildingCount': y, 'troopCount': z }, etc. }
            member_card_levels = { i: 0 for i in range(1, 14) }

            member_details = self.clash_royale_client.getPlayerInfo(player_tag_minus_hash)
            # member_details = TEST_PLAYER_RESPONSE
            member_cards = member_details['cards']

            for card in member_cards:
                # At the beginning of time, maxLevel of legendaries used to be 5. While the UI has updated that to 13, the data still has it relative to that maximum.
                card_level = 13 - (card['maxLevel'] - card['level'])
                member_card_levels[card_level] += 1
        
            # Get subset of levels to show

            member_cards_ranked.append(
                {
                    'tag': member['tag'],
                    'name': member['name'],
                    'member_card_levels': member_card_levels
                }
            )

            #debugging
            print({
                    'tag': member['tag'],
                    'name': member['name'],
                    'member_card_levels': member_card_levels
                })
            # Sleep 1 milliseconds before next request (don't wanna get rate limited lol...or maybe it already rate limits....)
            sleep(0.001)

        # # Faking some data
        # member_card_levels = [
        #     { 'tag': 'nice', 'name':'joseph', 'member_card_levels': {13: 12, 12: 4, 11:2} },
        #     { 'tag': 'nice', 'name':'david', 'member_card_levels': {13: 22, 12: 4, 11:2} },
        #     { 'tag': 'nice', 'name':'phong', 'member_card_levels': {13: 12, 12: 4, 11:52} }
        # ]

        # Rank members then return results
        member_cards_ranked.sort(key=cmp_to_key(compare_card_levels))

        # print(member_cards_ranked)
        return member_cards_ranked

    # def testGet(self):
    #     return self.clash_royale_client.getPlayerInfo('8VUG0GQRY')

# test = ClanMembersRanker()
# test.getClanCardsRank('#9GULPJ9L')
