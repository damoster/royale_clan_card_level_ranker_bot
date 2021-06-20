# These test response based off schemas from https://developer.clashroyale.com/#/documentation

CLAN_INFO_API_RESPONSE = {
  "tag": "#9GULPJ9L",
  "name": "AUSCLAN",
  "type": "open",
  "description": """
    During battles days, do wars ASAP. Do all attacks within 22hrs of war reset.
    Chat if you can't or be kicked! RoyaleApi.com
    """,
  "badgeId": 16000025,
  "clanScore": 53290,
  "clanWarTrophies": 2310,
  "location": {
    "id": 57000021,
    "name": "Australia",
    "isCountry": True,
    "countryCode": "AU"
  },
  "requiredTrophies": 5000,
  "donationsPerWeek": 18072,
  "clanChestStatus": "inactive",
  "clanChestLevel": 1,
  "clanChestMaxLevel": 0,
  "members": 50,
  "memberList": [
    {
      "tag": "#YV9GU2VG",
      "name": "Goku",
      "role": "member",
      "lastSeen": "20210617T113925.000Z",
      "expLevel": 13,
      "trophies": 5495,
      "arena": {
        "id": 54000013,
        "name": "Challenger II"
      },
      "clanRank": 5,
      "previousClanRank": 7,
      "donations": 36,
      "donationsReceived": 160,
      "clanChestPoints": 0
    },
    {
      "tag": "#8VUG0GQRY",
      "name": "joseph",
      "role": "elder",
      "lastSeen": "20210617T122354.000Z",
      "expLevel": 13,
      "trophies": 5501,
      "arena": {
        "id": 54000013,
        "name": "Challenger II"
      },
      "clanRank": 4,
      "previousClanRank": 5,
      "donations": 68,
      "donationsReceived": 160,
      "clanChestPoints": 0
    },
    {
      "tag": "#LYJVYUUUR",
      "name": "ZEPOL 1244",
      "role": "coLeader",
      "lastSeen": "20210617T123313.000Z",
      "expLevel": 13,
      "trophies": 5563,
      "arena": {
        "id": 54000013,
        "name": "Challenger II"
      },
      "clanRank": 2,
      "previousClanRank": 1,
      "donations": 632,
      "donationsReceived": 360,
      "clanChestPoints": 0
    }
  ]
}

PLAYER_1_RESPONSE = {
  "tag": "#YV9GU2VG",
  "name": "Goku",
  "expLevel": 13,
  "trophies": 5362,
  "bestTrophies": 5981,
  "wins": 8204,
  "losses": 7615,
  "battleCount": 18066,
  "threeCrownWins": 4299,
  "challengeCardsWon": 5238,
  "challengeMaxWins": 10,
  "tournamentCardsWon": 95,
  "tournamentBattleCount": 433,
  "role": "member",
  "donations": 92,
  "donationsReceived": 280,
  "totalDonations": 99343,
  "warDayWins": 159,
  "clanCardsCollected": 451542,
  "clan": {
    "tag": "#9GULPJ9L",
    "name": "AUSCLAN",
    "badgeId": 16000025
  },
  "arena": {
    "id": 54000013,
    "name": "Challenger II"
  },
  "leagueStatistics": {
    "currentSeason": {
      "trophies": 5362,
      "bestTrophies": 5495
    },
    "previousSeason": {
      "id": "2021-05",
      "trophies": 5832,
      "bestTrophies": 5832
    },
    "bestSeason": {
      "id": "2021-05",
      "trophies": 5832
    }
  },
  "badges": [
    {
      "name": "1000Wins",
      "progress": 8204
    },
    {
      "name": "Played1Year",
      "progress": 1921
    },
    {
      "name": "Played2Years",
      "progress": 1921
    },
    {
      "name": "Played3Years",
      "progress": 1921
    },
    {
      "name": "TopLeague",
      "progress": 5981
    },
    {
      "name": "ClanWarWins",
      "level": 3,
      "maxLevel": 3,
      "progress": 159
    },
    {
      "name": "Played4Years",
      "progress": 1921
    },
    {
      "name": "Played5Years",
      "progress": 1921
    }
  ],
  "achievements": [
    {
      "name": "Team Player",
      "stars": 3,
      "value": 11,
      "target": 1,
      "info": "Join a Clan",
      "completionInfo": None
    },
    {
      "name": "Friend in Need",
      "stars": 3,
      "value": 99343,
      "target": 2500,
      "info": "Donate 2500 cards",
      "completionInfo": None
    },
    {
      "name": "Road to Glory",
      "stars": 3,
      "value": 18,
      "target": 6,
      "info": "Reach Arena 6",
      "completionInfo": None
    },
    {
      "name": "Gatherer",
      "stars": 3,
      "value": 102,
      "target": 40,
      "info": "Collect 40 cards",
      "completionInfo": None
    },
    {
      "name": "TV Royale",
      "stars": 3,
      "value": 1,
      "target": 1,
      "info": "Watch a TV Royale Replay",
      "completionInfo": None
    },
    {
      "name": "Tournament Rewards",
      "stars": 0,
      "value": 95,
      "target": 1000,
      "info": "Win 1000 cards from tournaments",
      "completionInfo": None
    },
    {
      "name": "Tournament Host",
      "stars": 1,
      "value": 1,
      "target": 10,
      "info": "Create and finish 10 tournaments",
      "completionInfo": None
    },
    {
      "name": "Tournament Player",
      "stars": 3,
      "value": 19,
      "target": 1,
      "info": "Join a tournament",
      "completionInfo": None
    },
    {
      "name": "Challenge Streak",
      "stars": 3,
      "value": 20,
      "target": 12,
      "info": "Get 12 wins in a single Challenge",
      "completionInfo": None
    },
    {
      "name": "Practice with Friends",
      "stars": 3,
      "value": 120,
      "target": 10,
      "info": "Win 10 Friendly Battles",
      "completionInfo": None
    },
    {
      "name": "Special Challenge",
      "stars": 3,
      "value": 276,
      "target": 5,
      "info": "Participate in 5 unique Special Event Challenges",
      "completionInfo": None
    },
    {
      "name": "Friend in Need II",
      "stars": 3,
      "value": 99343,
      "target": 25000,
      "info": "Donate 25000 cards",
      "completionInfo": None
    }
  ],
  "cards": [
    {
      "name": "Battle Healer",
      "id": 26000068,
      "level": 5,
      "maxLevel": 11,
      "count": 1344,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/KdwXcoigS2Kg-cgA7BJJIANbUJG6SNgjetRQ-MegZ08.png"
      }
    },
    {
      "name": "Wizard",
      "id": 26000017,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Mej7vnv4H_3p_8qPs_N6_GKahy6HDr7pU7i9eTHS84U.png"
      }
    },
    {
      "name": "Inferno Dragon",
      "id": 26000037,
      "level": 3,
      "maxLevel": 5,
      "count": 5,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/y5HDbKtTbWG6En6TGWU0xoVIGs1-iQpIP4HC-VM7u8A.png"
      }
    },
    {
      "name": "Electro Wizard",
      "id": 26000042,
      "level": 3,
      "maxLevel": 5,
      "count": 8,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/RsFaHgB3w6vXsTjXdPr3x8l_GbV9TbOUCvIx07prbrQ.png"
      }
    },
    {
      "name": "Spear Goblins",
      "id": 26000019,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/FSDFotjaXidI4ku_WFpVCTWS1hKGnFh1sxX0lxM43_E.png"
      }
    },
    {
      "name": "Sparky",
      "id": 26000033,
      "level": 4,
      "maxLevel": 5,
      "count": 3,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/2GKMkBrArZXgQxf2ygFjDs4VvGYPbx8F6Lj_68iVhIM.png"
      }
    },
    {
      "name": "Freeze",
      "id": 28000005,
      "level": 2,
      "maxLevel": 8,
      "count": 127,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/I1M20_Zs_p_BS1NaNIVQjuMJkYI_1-ePtwYZahn0JXQ.png"
      }
    },
    {
      "name": "Skeleton Army",
      "id": 26000012,
      "level": 4,
      "maxLevel": 8,
      "count": 122,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png"
      }
    },
    {
      "name": "Arrows",
      "id": 28000001,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Flsoci-Y6y8ZFVi5uRFTmgkPnCmMyMVrU7YmmuPvSBo.png"
      }
    },
    {
      "name": "Ram Rider",
      "id": 26000051,
      "level": 4,
      "maxLevel": 5,
      "count": 4,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QaJyerT7f7oMyZ3Fv1glKymtLSvx7YUXisAulxl7zRI.png"
      }
    },
    {
      "name": "Battle Ram",
      "id": 26000036,
      "level": 8,
      "maxLevel": 11,
      "count": 2099,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/dyc50V2cplKi4H7pq1B3I36pl_sEH5DQrNHboS_dbbM.png"
      }
    },
    {
      "name": "Skeleton Barrel",
      "id": 26000056,
      "level": 7,
      "maxLevel": 13,
      "count": 9395,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vCB4DWCcrGbTkarjcOiVz4aNDx6GWLm0yUepg9E1MGo.png"
      }
    },
    {
      "name": "Balloon",
      "id": 26000006,
      "level": 7,
      "maxLevel": 8,
      "count": 126,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/qBipxLo-3hhCnPrApp2Nn3b2NgrSrvwzWytvREev0CY.png"
      }
    },
    {
      "name": "Furnace",
      "id": 27000010,
      "level": 7,
      "maxLevel": 11,
      "count": 2400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/iqbDiG7yYRIzvCPXdt9zPb3IvMt7F7Gi4wIPnh2x4aI.png"
      }
    },
    {
      "name": "Lumberjack",
      "id": 26000035,
      "level": 3,
      "maxLevel": 5,
      "count": 6,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/E6RWrnCuk13xMX5OE1EQtLEKTZQV6B78d00y8PlXt6Q.png"
      }
    },
    {
      "name": "Mortar",
      "id": 27000002,
      "level": 7,
      "maxLevel": 13,
      "count": 9384,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lPOSw6H7YOHq2miSCrf7ZDL3ANjhJdPPDYOTujdNrVE.png"
      }
    },
    {
      "name": "Princess",
      "id": 26000026,
      "level": 4,
      "maxLevel": 5,
      "count": 5,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png"
      }
    },
    {
      "name": "Bomb Tower",
      "id": 27000004,
      "level": 5,
      "maxLevel": 11,
      "count": 2545,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/rirYRyHPc97emRjoH-c1O8uZCBzPVnToaGuNGusF3TQ.png"
      }
    },
    {
      "name": "Heal Spirit",
      "id": 28000016,
      "level": 5,
      "maxLevel": 11,
      "count": 2319,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/GITl06sa2nGRLPvboyXbGEv5E3I-wAwn1Eqa5esggbc.png"
      }
    },
    {
      "name": "The Log",
      "id": 28000011,
      "level": 2,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_iDwuDLexHPFZ_x4_a0eP-rxCS6vwWgTs6DLauwwoaY.png"
      }
    },
    {
      "name": "Clone",
      "id": 28000013,
      "level": 6,
      "maxLevel": 8,
      "count": 144,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png"
      }
    },
    {
      "name": "Royal Giant",
      "id": 26000024,
      "level": 11,
      "maxLevel": 13,
      "count": 7000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/mnlRaNtmfpQx2e6mp70sLd0ND-pKPF70Cf87_agEKg4.png"
      }
    },
    {
      "name": "Knight",
      "id": 26000000,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png"
      }
    },
    {
      "name": "Cannon",
      "id": 27000000,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/nZK1y-beLxO5vnlyUhK6-2zH2NzXJwqykcosqQ1cmZ8.png"
      }
    },
    {
      "name": "Skeletons",
      "id": 26000010,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/oO7iKMU5m0cdxhYPZA3nWQiAUh2yoGgdThLWB1rVSec.png"
      }
    },
    {
      "name": "Goblin Barrel",
      "id": 28000004,
      "level": 2,
      "maxLevel": 8,
      "count": 85,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png"
      }
    },
    {
      "name": "Goblin Hut",
      "id": 27000001,
      "level": 7,
      "maxLevel": 11,
      "count": 2201,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/l8ZdzzNLcwB4u7ihGgxNFQOjCT_njFuAhZr7D6PRF7E.png"
      }
    },
    {
      "name": "Bomber",
      "id": 26000013,
      "level": 8,
      "maxLevel": 13,
      "count": 9200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/12n1CesxKIcqVYntjxcF36EFA-ONw7Z-DoL0_rQrbdo.png"
      }
    },
    {
      "name": "Rocket",
      "id": 28000003,
      "level": 7,
      "maxLevel": 11,
      "count": 2040,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ie07nQNK9CjhKOa4-arFAewi4EroqaA-86Xo7r5tx94.png"
      }
    },
    {
      "name": "Miner",
      "id": 26000032,
      "level": 3,
      "maxLevel": 5,
      "count": 4,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Y4yWvdwBCg2FpAZgs8T09Gy34WOwpLZW-ttL52Ae8NE.png"
      }
    },
    {
      "name": "Dart Goblin",
      "id": 26000040,
      "level": 9,
      "maxLevel": 11,
      "count": 1641,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BmpK3bqEAviflqHCdxxnfm-_l3pRPJw3qxHkwS55nCY.png"
      }
    },
    {
      "name": "Executioner",
      "id": 26000045,
      "level": 6,
      "maxLevel": 8,
      "count": 166,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/9XL5BP2mqzV8kza6KF8rOxrpCZTyuGLp2l413DTjEoM.png"
      }
    },
    {
      "name": "Cannon Cart",
      "id": 26000054,
      "level": 6,
      "maxLevel": 8,
      "count": 142,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/aqwxRz8HXzqlMCO4WMXNA1txynjXTsLinknqsgZLbok.png"
      }
    },
    {
      "name": "Three Musketeers",
      "id": 26000028,
      "level": 8,
      "maxLevel": 11,
      "count": 2200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_J2GhbkX3vswaFk1wG-dopwiHyNc_YiPhwroiKF3Mek.png"
      }
    },
    {
      "name": "Royal Ghost",
      "id": 26000050,
      "level": 3,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/3En2cz0ISQAaMTHY3hj3rTveFN2kJYq-H4VxvdJNvCM.png"
      }
    },
    {
      "name": "Electro Dragon",
      "id": 26000063,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/tN9h6lnMNPCNsx0LMFmvpHgznbDZ1fBRkx-C7UfNmfY.png"
      }
    },
    {
      "name": "Elixir Collector",
      "id": 27000007,
      "level": 5,
      "maxLevel": 11,
      "count": 2396,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BGLo3Grsp81c72EpxLLk-Sofk3VY56zahnUNOv3JcT0.png"
      }
    },
    {
      "name": "Barbarian Barrel",
      "id": 28000015,
      "level": 6,
      "maxLevel": 8,
      "count": 71,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Gb0G1yNy0i5cIGUHin8uoFWxqntNtRPhY_jeMXg7HnA.png"
      }
    },
    {
      "name": "Bowler",
      "id": 26000034,
      "level": 4,
      "maxLevel": 8,
      "count": 161,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/SU4qFXmbQXWjvASxVI6z9IJuTYolx4A0MKK90sTIE88.png"
      }
    },
    {
      "name": "Guards",
      "id": 26000025,
      "level": 2,
      "maxLevel": 8,
      "count": 194,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/1ArKfLJxYo6_NU_S9cAeIrfbXqWH0oULVJXedxBXQlU.png"
      }
    },
    {
      "name": "Dark Prince",
      "id": 26000027,
      "level": 5,
      "maxLevel": 8,
      "count": 208,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/M7fXlrKXHu2IvpSGpk36kXVstslbR08Bbxcy0jQcln8.png"
      }
    },
    {
      "name": "Bandit",
      "id": 26000046,
      "level": 3,
      "maxLevel": 5,
      "count": 3,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QWDdXMKJNpv0go-HYaWQWP6p8uIOHjqn-zX7G0p3DyM.png"
      }
    },
    {
      "name": "Minions",
      "id": 26000005,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/yHGpoEnmUWPGV_hBbhn-Kk-Bs838OjGzWzJJlQpQKQA.png"
      }
    },
    {
      "name": "Archers",
      "id": 26000001,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/W4Hmp8MTSdXANN8KdblbtHwtsbt0o749BbxNqmJYfA8.png"
      }
    },
    {
      "name": "Rage",
      "id": 28000002,
      "level": 4,
      "maxLevel": 8,
      "count": 202,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png"
      }
    },
    {
      "name": "Elite Barbarians",
      "id": 26000043,
      "level": 10,
      "maxLevel": 13,
      "count": 8000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"
      }
    },
    {
      "name": "Ice Golem",
      "id": 26000038,
      "level": 5,
      "maxLevel": 11,
      "count": 2142,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/r05cmpwV1o7i7FHodtZwW3fmjbXCW34IJCsDEV5cZC4.png"
      }
    },
    {
      "name": "Lightning",
      "id": 28000007,
      "level": 4,
      "maxLevel": 8,
      "count": 160,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fpnESbYqe5GyZmaVVYe-SEu7tE0Kxh_HZyVigzvLjks.png"
      }
    },
    {
      "name": "Graveyard",
      "id": 28000010,
      "level": 3,
      "maxLevel": 5,
      "count": 3,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Icp8BIyyfBTj1ncCJS7mb82SY7TPV-MAE-J2L2R48DI.png"
      }
    },
    {
      "name": "Goblin Gang",
      "id": 26000041,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NHflxzVAQT4oAz7eDfdueqpictb5vrWezn1nuqFhE4w.png"
      }
    },
    {
      "name": "Barbarians",
      "id": 26000008,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/TvJsuu2S4yhyk1jVYUAQwdKOnW4U77KuWWOTPOWnwfI.png"
      }
    },
    {
      "name": "Magic Archer",
      "id": 26000062,
      "level": 4,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Avli3W7BxU9HQ2SoLiXnBgGx25FoNXUSFm7OcAk68ek.png"
      }
    },
    {
      "name": "Poison",
      "id": 28000009,
      "level": 6,
      "maxLevel": 8,
      "count": 46,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/98HDkG2189yOULcVG9jz2QbJKtfuhH21DIrIjkOjxI8.png"
      }
    },
    {
      "name": "Rascals",
      "id": 26000053,
      "level": 11,
      "maxLevel": 13,
      "count": 7000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/KV48DfwVHKx9XCjzBdk3daT_Eb52Me4VgjVO7WctRc4.png"
      }
    },
    {
      "name": "Tesla",
      "id": 27000006,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/OiwnGrxFMNiHetYEerE-UZt0L_uYNzFY7qV_CA_OxR4.png"
      }
    },
    {
      "name": "Lava Hound",
      "id": 26000029,
      "level": 3,
      "maxLevel": 5,
      "count": 4,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/unicRQ975sBY2oLtfgZbAI56ZvaWz7azj-vXTLxc0r8.png"
      }
    },
    {
      "name": "X-Bow",
      "id": 27000008,
      "level": 4,
      "maxLevel": 8,
      "count": 233,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/zVQ9Hme1hlj9Dc6e1ORl9xWwglcSrP7ejow5mAhLUJc.png"
      }
    },
    {
      "name": "Giant",
      "id": 26000003,
      "level": 9,
      "maxLevel": 11,
      "count": 1799,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Axr4ox5_b7edmLsoHxBX3vmgijAIibuF6RImTbqLlXE.png"
      }
    },
    {
      "name": "Mega Minion",
      "id": 26000039,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/-T_e4YLbuhPBKbYnBwQfXgynNpp5eOIN_0RracYwL9c.png"
      }
    },
    {
      "name": "Ice Spirit",
      "id": 26000030,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lv1budiafU9XmSdrDkk0NYyqASAFYyZ06CPysXKZXlA.png"
      }
    },
    {
      "name": "Zappies",
      "id": 26000052,
      "level": 7,
      "maxLevel": 11,
      "count": 2283,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QZfHRpLRmutZbCr5fpLnTpIp89vLI6NrAwzGZ8tHEc4.png"
      }
    },
    {
      "name": "Tombstone",
      "id": 27000009,
      "level": 7,
      "maxLevel": 11,
      "count": 2097,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/LjSfSbwQfkZuRJY4pVxKspZ-a0iM5KAhU8w-a_N5Z7Y.png"
      }
    },
    {
      "name": "Minion Horde",
      "id": 26000022,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Wyjq5l0IXHTkX9Rmpap6HaH08MvjbxFp1xBO9a47YSI.png"
      }
    },
    {
      "name": "Bats",
      "id": 26000049,
      "level": 8,
      "maxLevel": 13,
      "count": 9200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/EnIcvO21hxiNpoI-zO6MDjLmzwPbq8Z4JPo2OKoVUjU.png"
      }
    },
    {
      "name": "Mirror",
      "id": 28000006,
      "level": 4,
      "maxLevel": 8,
      "count": 210,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/wC6Cm9rKLEOk72zTsukVwxewKIoO4ZcMJun54zCPWvA.png"
      }
    },
    {
      "name": "Barbarian Hut",
      "id": 27000005,
      "level": 7,
      "maxLevel": 11,
      "count": 2400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/ho0nOG2y3Ch86elHHcocQs8Fv_QNe0cFJ2CijsxABZA.png"
      }
    },
    {
      "name": "Royal Recruits",
      "id": 26000047,
      "level": 9,
      "maxLevel": 13,
      "count": 8800,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jcNyYGUiXXNz3kuz8NBkHNKNREQKraXlb_Ts7rhCIdM.png"
      }
    },
    {
      "name": "Hunter",
      "id": 26000044,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/VNabB1WKnYtYRSG7X_FZfnZjQDHTBs9A96OGMFmecrA.png"
      }
    },
    {
      "name": "Tornado",
      "id": 28000012,
      "level": 2,
      "maxLevel": 8,
      "count": 185,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QJB-QK1QJHdw4hjpAwVSyZBozc2ZWAR9pQ-SMUyKaT0.png"
      }
    },
    {
      "name": "Goblins",
      "id": 26000002,
      "level": 7,
      "maxLevel": 13,
      "count": 9400,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/X_DQUye_OaS3QN6VC9CPw05Fit7wvSm3XegXIXKP--0.png"
      }
    },
    {
      "name": "Ice Wizard",
      "id": 26000023,
      "level": 4,
      "maxLevel": 5,
      "count": 3,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/W3dkw0HTw9n1jB-zbknY2w3wHuyuLxSRIAV5fUT1SEY.png"
      }
    },
    {
      "name": "Giant Skeleton",
      "id": 26000020,
      "level": 7,
      "maxLevel": 8,
      "count": 126,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0p0gd0XaVRu1Hb1iSG1hTYbz2AN6aEiZnhaAib5O8Z8.png"
      }
    },
    {
      "name": "Fire Spirit",
      "id": 26000031,
      "level": 8,
      "maxLevel": 13,
      "count": 9200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/16-BqusVvynIgYI8_Jci3LDC-r8AI_xaIYLgXqtlmS8.png"
      }
    },
    {
      "name": "Giant Snowball",
      "id": 28000017,
      "level": 7,
      "maxLevel": 13,
      "count": 8820,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/7MaJLa6hK9WN2_VIshuh5DIDfGwm0wEv98gXtAxLDPs.png"
      }
    },
    {
      "name": "Royal Hogs",
      "id": 26000059,
      "level": 7,
      "maxLevel": 11,
      "count": 2056,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/ASSQJG_MoVq9e81HZzo4bynMnyLNpNJMfSLb3hqydOw.png"
      }
    },
    {
      "name": "Night Witch",
      "id": 26000048,
      "level": 3,
      "maxLevel": 5,
      "count": 4,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NpCrXDEDBBJgNv9QrBAcJmmMFbS7pe3KCY8xJ5VB18A.png"
      }
    },
    {
      "name": "Goblin Giant",
      "id": 26000060,
      "level": 2,
      "maxLevel": 8,
      "count": 140,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/SoW16cY3jXBwaTDvb39DkqiVsoFVaDWbzf5QBYphJrY.png"
      }
    },
    {
      "name": "Mega Knight",
      "id": 26000055,
      "level": 3,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/O2NycChSNhn_UK9nqBXUhhC_lILkiANzPuJjtjoz0CE.png"
      }
    },
    {
      "name": "Inferno Tower",
      "id": 27000003,
      "level": 9,
      "maxLevel": 11,
      "count": 1632,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png"
      }
    },
    {
      "name": "Wall Breakers",
      "id": 26000058,
      "level": 2,
      "maxLevel": 8,
      "count": 150,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_xPphEfC8eEwFNrfU3cMQG9-f5JaLQ31ARCA7l3XtW4.png"
      }
    },
    {
      "name": "Earthquake",
      "id": 28000014,
      "level": 5,
      "maxLevel": 11,
      "count": 1614,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/XeQXcrUu59C52DslyZVwCnbi4yamID-WxfVZLShgZmE.png"
      }
    },
    {
      "name": "Goblin Cage",
      "id": 27000012,
      "level": 5,
      "maxLevel": 11,
      "count": 1488,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vD24bBgK4rSq7wx5QEbuqChtPMRFviL_ep76GwQw1yA.png"
      }
    },
    {
      "name": "Fisherman",
      "id": 26000061,
      "level": 3,
      "maxLevel": 5,
      "count": 4,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/U2KZ3g0wyufcuA5P2Xrn3Z3lr1WiJmc5S0IWOZHgizQ.png"
      }
    },
    {
      "name": "Elixir Golem",
      "id": 26000067,
      "level": 2,
      "maxLevel": 11,
      "count": 1351,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/puhMsZjCIqy21HW3hYxjrk_xt8NIPyFqjRy-BeLKZwo.png"
      }
    },
    {
      "name": "Zap",
      "id": 28000008,
      "level": 11,
      "maxLevel": 13,
      "count": 6452,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png"
      }
    },
    {
      "name": "Fireball",
      "id": 28000000,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lZD9MILQv7O-P3XBr_xOLS5idwuz3_7Ws9G60U36yhc.png"
      }
    },
    {
      "name": "Royal Delivery",
      "id": 28000018,
      "level": 1,
      "maxLevel": 13,
      "count": 3979,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/LPg7AGjGI3_xmi7gLLgGC50yKM1jJ2teWkZfoHJcIZo.png"
      }
    },
    {
      "name": "Electro Giant",
      "id": 26000085,
      "level": 7,
      "maxLevel": 8,
      "count": 60,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_uChZkNHAMq6tPb3v6A49xinOe3CnhjstOhG6OZbPYc.png"
      }
    },
    {
      "name": "Electro Spirit",
      "id": 26000084,
      "level": 1,
      "maxLevel": 13,
      "count": 3144,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/WKd4-IAFsgPpMo7dDi9sujmYjRhOMEWiE07OUJpvD9g.png"
      }
    },
    {
      "name": "Mother Witch",
      "id": 26000083,
      "level": 3,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fO-Xah8XZkYKaSK9SCp3wnzwxtvIhun9NVY-zzte1Ng.png"
      }
    },
    {
      "name": "Prince",
      "id": 26000016,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/3JntJV62aY0G1Qh6LIs-ek-0ayeYFY3VItpG7cb9I60.png"
      }
    },
    {
      "name": "Flying Machine",
      "id": 26000057,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/hzKNE3QwFcrSrDDRuVW3QY_OnrDPijSiIp-PsWgFevE.png"
      }
    },
    {
      "name": "P.E.K.K.A",
      "id": 26000004,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/MlArURKhn_zWAZY-Xj1qIRKLVKquarG25BXDjUQajNs.png"
      }
    },
    {
      "name": "Skeleton Dragons",
      "id": 26000080,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/qPOtg9uONh47_NLxGhhFc_ww9PlZ6z3Ry507q1NZUXs.png"
      }
    },
    {
      "name": "Baby Dragon",
      "id": 26000015,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cjC9n4AvEZJ3urkVh-rwBkJ-aRSsydIMqSAV48hAih0.png"
      }
    },
    {
      "name": "Firecracker",
      "id": 26000064,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/c1rL3LO1U2D9-TkeFfAC18gP3AO8ztSwrcHMZplwL2Q.png"
      }
    },
    {
      "name": "Witch",
      "id": 26000007,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cfwk1vzehVyHC-uloEIH6NOI0hOdofCutR5PyhIgO6w.png"
      }
    },
    {
      "name": "Golem",
      "id": 26000009,
      "level": 8,
      "starLevel": 1,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png"
      }
    },
    {
      "name": "Hog Rider",
      "id": 26000021,
      "level": 11,
      "starLevel": 1,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ubu0oUl8tZkusnkZf8Xv9Vno5IO29Y-jbZ4fhoNJ5oc.png"
      }
    },
    {
      "name": "Musketeer",
      "id": 26000014,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Tex1C48UTq9FKtAX-3tzG0FJmc9jzncUZG3bb5Vf-Ds.png"
      }
    },
    {
      "name": "Mini P.E.K.K.A",
      "id": 26000018,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png"
      }
    },
    {
      "name": "Valkyrie",
      "id": 26000011,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png"
      }
    }
  ],
  "currentDeck": [
    {
      "name": "Baby Dragon",
      "id": 26000015,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cjC9n4AvEZJ3urkVh-rwBkJ-aRSsydIMqSAV48hAih0.png"
      }
    },
    {
      "name": "Firecracker",
      "id": 26000064,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/c1rL3LO1U2D9-TkeFfAC18gP3AO8ztSwrcHMZplwL2Q.png"
      }
    },
    {
      "name": "Witch",
      "id": 26000007,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cfwk1vzehVyHC-uloEIH6NOI0hOdofCutR5PyhIgO6w.png"
      }
    },
    {
      "name": "Golem",
      "id": 26000009,
      "level": 8,
      "starLevel": 1,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png"
      }
    },
    {
      "name": "Hog Rider",
      "id": 26000021,
      "level": 11,
      "starLevel": 1,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ubu0oUl8tZkusnkZf8Xv9Vno5IO29Y-jbZ4fhoNJ5oc.png"
      }
    },
    {
      "name": "Musketeer",
      "id": 26000014,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Tex1C48UTq9FKtAX-3tzG0FJmc9jzncUZG3bb5Vf-Ds.png"
      }
    },
    {
      "name": "Mini P.E.K.K.A",
      "id": 26000018,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png"
      }
    },
    {
      "name": "Valkyrie",
      "id": 26000011,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png"
      }
    }
  ],
  "currentFavouriteCard": {
    "name": "Valkyrie",
    "id": 26000011,
    "maxLevel": 11,
    "iconUrls": {
      "medium": "https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png"
    }
  },
  "starPoints": 42555
}

PLAYER_2_RESPONSE = {
  "tag": "#8VUG0GQRY",
  "name": "joseph",
  "expLevel": 13,
  "trophies": 5483,
  "bestTrophies": 5889,
  "wins": 4026,
  "losses": 2975,
  "battleCount": 10242,
  "threeCrownWins": 1923,
  "challengeCardsWon": 3674,
  "challengeMaxWins": 12,
  "tournamentCardsWon": 0,
  "tournamentBattleCount": 459,
  "role": "elder",
  "donations": 124,
  "donationsReceived": 280,
  "totalDonations": 23495,
  "warDayWins": 153,
  "clanCardsCollected": 400381,
  "clan": {
    "tag": "#9GULPJ9L",
    "name": "AUSCLAN",
    "badgeId": 16000025
  },
  "arena": {
    "id": 54000013,
    "name": "Challenger II"
  },
  "leagueStatistics": {
    "currentSeason": {
      "trophies": 5483,
      "bestTrophies": 5534
    },
    "previousSeason": {
      "id": "2021-05",
      "trophies": 5671,
      "bestTrophies": 5802
    },
    "bestSeason": {
      "id": "2020-02",
      "trophies": 5757
    }
  },
  "badges": [
    {
      "name": "1000Wins",
      "progress": 4026
    },
    {
      "name": "Played1Year",
      "progress": 1390
    },
    {
      "name": "Played2Years",
      "progress": 1390
    },
    {
      "name": "Played3Years",
      "progress": 1390
    },
    {
      "name": "TopLeague",
      "progress": 5889
    },
    {
      "name": "ClanWarWins",
      "level": 3,
      "maxLevel": 3,
      "progress": 153
    }
  ],
  "achievements": [
    {
      "name": "Team Player",
      "stars": 3,
      "value": 10,
      "target": 1,
      "info": "Join a Clan",
      "completionInfo": None
    },
    {
      "name": "Friend in Need",
      "stars": 3,
      "value": 23495,
      "target": 2500,
      "info": "Donate 2500 cards",
      "completionInfo": None
    },
    {
      "name": "Road to Glory",
      "stars": 3,
      "value": 18,
      "target": 6,
      "info": "Reach Arena 6",
      "completionInfo": None
    },
    {
      "name": "Gatherer",
      "stars": 3,
      "value": 103,
      "target": 40,
      "info": "Collect 40 cards",
      "completionInfo": None
    },
    {
      "name": "TV Royale",
      "stars": 3,
      "value": 1,
      "target": 1,
      "info": "Watch a TV Royale Replay",
      "completionInfo": None
    },
    {
      "name": "Tournament Rewards",
      "stars": 0,
      "value": 0,
      "target": 1000,
      "info": "Win 1000 cards from tournaments",
      "completionInfo": None
    },
    {
      "name": "Tournament Host",
      "stars": 0,
      "value": 0,
      "target": 1,
      "info": "Create and finish one tournament",
      "completionInfo": None
    },
    {
      "name": "Tournament Player",
      "stars": 3,
      "value": 5,
      "target": 1,
      "info": "Join a tournament",
      "completionInfo": None
    },
    {
      "name": "Challenge Streak",
      "stars": 3,
      "value": 20,
      "target": 12,
      "info": "Get 12 wins in a single Challenge",
      "completionInfo": None
    },
    {
      "name": "Practice with Friends",
      "stars": 3,
      "value": 22,
      "target": 10,
      "info": "Win 10 Friendly Battles",
      "completionInfo": None
    },
    {
      "name": "Special Challenge",
      "stars": 3,
      "value": 248,
      "target": 5,
      "info": "Participate in 5 unique Special Event Challenges",
      "completionInfo": None
    },
    {
      "name": "Friend in Need II",
      "stars": 2,
      "value": 23495,
      "target": 25000,
      "info": "Donate 25000 cards",
      "completionInfo": None
    }
  ],
  "cards": [
    {
      "name": "Elixir Collector",
      "id": 27000007,
      "level": 8,
      "maxLevel": 11,
      "count": 934,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BGLo3Grsp81c72EpxLLk-Sofk3VY56zahnUNOv3JcT0.png"
      }
    },
    {
      "name": "Inferno Tower",
      "id": 27000003,
      "level": 9,
      "maxLevel": 11,
      "count": 508,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png"
      }
    },
    {
      "name": "Barbarians",
      "id": 26000008,
      "level": 10,
      "maxLevel": 13,
      "count": 5687,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/TvJsuu2S4yhyk1jVYUAQwdKOnW4U77KuWWOTPOWnwfI.png"
      }
    },
    {
      "name": "Bowler",
      "id": 26000034,
      "level": 5,
      "maxLevel": 8,
      "count": 119,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/SU4qFXmbQXWjvASxVI6z9IJuTYolx4A0MKK90sTIE88.png"
      }
    },
    {
      "name": "Royal Giant",
      "id": 26000024,
      "level": 12,
      "maxLevel": 13,
      "count": 4711,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/mnlRaNtmfpQx2e6mp70sLd0ND-pKPF70Cf87_agEKg4.png"
      }
    },
    {
      "name": "Giant Skeleton",
      "id": 26000020,
      "level": 6,
      "maxLevel": 8,
      "count": 96,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0p0gd0XaVRu1Hb1iSG1hTYbz2AN6aEiZnhaAib5O8Z8.png"
      }
    },
    {
      "name": "Battle Ram",
      "id": 26000036,
      "level": 10,
      "maxLevel": 11,
      "count": 301,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/dyc50V2cplKi4H7pq1B3I36pl_sEH5DQrNHboS_dbbM.png"
      }
    },
    {
      "name": "X-Bow",
      "id": 27000008,
      "level": 5,
      "maxLevel": 8,
      "count": 77,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/zVQ9Hme1hlj9Dc6e1ORl9xWwglcSrP7ejow5mAhLUJc.png"
      }
    },
    {
      "name": "Ram Rider",
      "id": 26000051,
      "level": 2,
      "maxLevel": 5,
      "count": 9,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QaJyerT7f7oMyZ3Fv1glKymtLSvx7YUXisAulxl7zRI.png"
      }
    },
    {
      "name": "Goblin Hut",
      "id": 27000001,
      "level": 8,
      "maxLevel": 11,
      "count": 1095,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/l8ZdzzNLcwB4u7ihGgxNFQOjCT_njFuAhZr7D6PRF7E.png"
      }
    },
    {
      "name": "Princess",
      "id": 26000026,
      "level": 2,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png"
      }
    },
    {
      "name": "Bomb Tower",
      "id": 27000004,
      "level": 8,
      "maxLevel": 11,
      "count": 1052,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/rirYRyHPc97emRjoH-c1O8uZCBzPVnToaGuNGusF3TQ.png"
      }
    },
    {
      "name": "Hunter",
      "id": 26000044,
      "level": 5,
      "maxLevel": 8,
      "count": 151,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/VNabB1WKnYtYRSG7X_FZfnZjQDHTBs9A96OGMFmecrA.png"
      }
    },
    {
      "name": "Goblins",
      "id": 26000002,
      "level": 10,
      "maxLevel": 13,
      "count": 6680,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/X_DQUye_OaS3QN6VC9CPw05Fit7wvSm3XegXIXKP--0.png"
      }
    },
    {
      "name": "Magic Archer",
      "id": 26000062,
      "level": 3,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Avli3W7BxU9HQ2SoLiXnBgGx25FoNXUSFm7OcAk68ek.png"
      }
    },
    {
      "name": "Hog Rider",
      "id": 26000021,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ubu0oUl8tZkusnkZf8Xv9Vno5IO29Y-jbZ4fhoNJ5oc.png"
      }
    },
    {
      "name": "Fireball",
      "id": 28000000,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lZD9MILQv7O-P3XBr_xOLS5idwuz3_7Ws9G60U36yhc.png"
      }
    },
    {
      "name": "Battle Healer",
      "id": 26000068,
      "level": 9,
      "maxLevel": 11,
      "count": 370,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/KdwXcoigS2Kg-cgA7BJJIANbUJG6SNgjetRQ-MegZ08.png"
      }
    },
    {
      "name": "Witch",
      "id": 26000007,
      "level": 7,
      "maxLevel": 8,
      "count": 78,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cfwk1vzehVyHC-uloEIH6NOI0hOdofCutR5PyhIgO6w.png"
      }
    },
    {
      "name": "Wizard",
      "id": 26000017,
      "level": 9,
      "maxLevel": 11,
      "count": 610,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Mej7vnv4H_3p_8qPs_N6_GKahy6HDr7pU7i9eTHS84U.png"
      }
    },
    {
      "name": "Ice Spirit",
      "id": 26000030,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lv1budiafU9XmSdrDkk0NYyqASAFYyZ06CPysXKZXlA.png"
      }
    },
    {
      "name": "Fisherman",
      "id": 26000061,
      "level": 2,
      "maxLevel": 5,
      "count": 5,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/U2KZ3g0wyufcuA5P2Xrn3Z3lr1WiJmc5S0IWOZHgizQ.png"
      }
    },
    {
      "name": "Mirror",
      "id": 28000006,
      "level": 5,
      "maxLevel": 8,
      "count": 103,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/wC6Cm9rKLEOk72zTsukVwxewKIoO4ZcMJun54zCPWvA.png"
      }
    },
    {
      "name": "Goblin Gang",
      "id": 26000041,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NHflxzVAQT4oAz7eDfdueqpictb5vrWezn1nuqFhE4w.png"
      }
    },
    {
      "name": "Flying Machine",
      "id": 26000057,
      "level": 9,
      "maxLevel": 11,
      "count": 1302,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/hzKNE3QwFcrSrDDRuVW3QY_OnrDPijSiIp-PsWgFevE.png"
      }
    },
    {
      "name": "Tombstone",
      "id": 27000009,
      "level": 8,
      "maxLevel": 11,
      "count": 1176,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/LjSfSbwQfkZuRJY4pVxKspZ-a0iM5KAhU8w-a_N5Z7Y.png"
      }
    },
    {
      "name": "Clone",
      "id": 28000013,
      "level": 5,
      "maxLevel": 8,
      "count": 161,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png"
      }
    },
    {
      "name": "Rascals",
      "id": 26000053,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/KV48DfwVHKx9XCjzBdk3daT_Eb52Me4VgjVO7WctRc4.png"
      }
    },
    {
      "name": "Musketeer",
      "id": 26000014,
      "level": 10,
      "maxLevel": 11,
      "count": 108,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Tex1C48UTq9FKtAX-3tzG0FJmc9jzncUZG3bb5Vf-Ds.png"
      }
    },
    {
      "name": "Sparky",
      "id": 26000033,
      "level": 2,
      "maxLevel": 5,
      "count": 5,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/2GKMkBrArZXgQxf2ygFjDs4VvGYPbx8F6Lj_68iVhIM.png"
      }
    },
    {
      "name": "Cannon",
      "id": 27000000,
      "level": 10,
      "maxLevel": 13,
      "count": 6392,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/nZK1y-beLxO5vnlyUhK6-2zH2NzXJwqykcosqQ1cmZ8.png"
      }
    },
    {
      "name": "Balloon",
      "id": 26000006,
      "level": 6,
      "maxLevel": 8,
      "count": 134,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/qBipxLo-3hhCnPrApp2Nn3b2NgrSrvwzWytvREev0CY.png"
      }
    },
    {
      "name": "Mega Minion",
      "id": 26000039,
      "level": 9,
      "maxLevel": 11,
      "count": 881,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/-T_e4YLbuhPBKbYnBwQfXgynNpp5eOIN_0RracYwL9c.png"
      }
    },
    {
      "name": "Royal Recruits",
      "id": 26000047,
      "level": 10,
      "maxLevel": 13,
      "count": 6105,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jcNyYGUiXXNz3kuz8NBkHNKNREQKraXlb_Ts7rhCIdM.png"
      }
    },
    {
      "name": "Mega Knight",
      "id": 26000055,
      "level": 3,
      "maxLevel": 5,
      "count": 6,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/O2NycChSNhn_UK9nqBXUhhC_lILkiANzPuJjtjoz0CE.png"
      }
    },
    {
      "name": "Barbarian Hut",
      "id": 27000005,
      "level": 7,
      "maxLevel": 11,
      "count": 1345,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/ho0nOG2y3Ch86elHHcocQs8Fv_QNe0cFJ2CijsxABZA.png"
      }
    },
    {
      "name": "Bats",
      "id": 26000049,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/EnIcvO21hxiNpoI-zO6MDjLmzwPbq8Z4JPo2OKoVUjU.png"
      }
    },
    {
      "name": "Guards",
      "id": 26000025,
      "level": 5,
      "maxLevel": 8,
      "count": 110,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/1ArKfLJxYo6_NU_S9cAeIrfbXqWH0oULVJXedxBXQlU.png"
      }
    },
    {
      "name": "Lava Hound",
      "id": 26000029,
      "level": 2,
      "maxLevel": 5,
      "count": 8,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/unicRQ975sBY2oLtfgZbAI56ZvaWz7azj-vXTLxc0r8.png"
      }
    },
    {
      "name": "Freeze",
      "id": 28000005,
      "level": 5,
      "maxLevel": 8,
      "count": 133,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/I1M20_Zs_p_BS1NaNIVQjuMJkYI_1-ePtwYZahn0JXQ.png"
      }
    },
    {
      "name": "Arrows",
      "id": 28000001,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Flsoci-Y6y8ZFVi5uRFTmgkPnCmMyMVrU7YmmuPvSBo.png"
      }
    },
    {
      "name": "Goblin Cage",
      "id": 27000012,
      "level": 9,
      "maxLevel": 11,
      "count": 194,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vD24bBgK4rSq7wx5QEbuqChtPMRFviL_ep76GwQw1yA.png"
      }
    },
    {
      "name": "Mini P.E.K.K.A",
      "id": 26000018,
      "level": 10,
      "maxLevel": 11,
      "count": 186,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png"
      }
    },
    {
      "name": "P.E.K.K.A",
      "id": 26000004,
      "level": 7,
      "maxLevel": 8,
      "count": 115,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/MlArURKhn_zWAZY-Xj1qIRKLVKquarG25BXDjUQajNs.png"
      }
    },
    {
      "name": "Mortar",
      "id": 27000002,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lPOSw6H7YOHq2miSCrf7ZDL3ANjhJdPPDYOTujdNrVE.png"
      }
    },
    {
      "name": "Barbarian Barrel",
      "id": 28000015,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Gb0G1yNy0i5cIGUHin8uoFWxqntNtRPhY_jeMXg7HnA.png"
      }
    },
    {
      "name": "The Log",
      "id": 28000011,
      "level": 3,
      "maxLevel": 5,
      "count": 1,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_iDwuDLexHPFZ_x4_a0eP-rxCS6vwWgTs6DLauwwoaY.png"
      }
    },
    {
      "name": "Skeletons",
      "id": 26000010,
      "level": 10,
      "maxLevel": 13,
      "count": 6012,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/oO7iKMU5m0cdxhYPZA3nWQiAUh2yoGgdThLWB1rVSec.png"
      }
    },
    {
      "name": "Cannon Cart",
      "id": 26000054,
      "level": 4,
      "maxLevel": 8,
      "count": 107,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/aqwxRz8HXzqlMCO4WMXNA1txynjXTsLinknqsgZLbok.png"
      }
    },
    {
      "name": "Rage",
      "id": 28000002,
      "level": 4,
      "maxLevel": 8,
      "count": 129,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png"
      }
    },
    {
      "name": "Bandit",
      "id": 26000046,
      "level": 4,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QWDdXMKJNpv0go-HYaWQWP6p8uIOHjqn-zX7G0p3DyM.png"
      }
    },
    {
      "name": "Three Musketeers",
      "id": 26000028,
      "level": 8,
      "maxLevel": 11,
      "count": 1057,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_J2GhbkX3vswaFk1wG-dopwiHyNc_YiPhwroiKF3Mek.png"
      }
    },
    {
      "name": "Ice Wizard",
      "id": 26000023,
      "level": 3,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/W3dkw0HTw9n1jB-zbknY2w3wHuyuLxSRIAV5fUT1SEY.png"
      }
    },
    {
      "name": "Minions",
      "id": 26000005,
      "level": 12,
      "maxLevel": 13,
      "count": 4595,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/yHGpoEnmUWPGV_hBbhn-Kk-Bs838OjGzWzJJlQpQKQA.png"
      }
    },
    {
      "name": "Lightning",
      "id": 28000007,
      "level": 6,
      "maxLevel": 8,
      "count": 86,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fpnESbYqe5GyZmaVVYe-SEu7tE0Kxh_HZyVigzvLjks.png"
      }
    },
    {
      "name": "Zappies",
      "id": 26000052,
      "level": 7,
      "maxLevel": 11,
      "count": 1412,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QZfHRpLRmutZbCr5fpLnTpIp89vLI6NrAwzGZ8tHEc4.png"
      }
    },
    {
      "name": "Heal Spirit",
      "id": 28000016,
      "level": 9,
      "maxLevel": 11,
      "count": 731,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/GITl06sa2nGRLPvboyXbGEv5E3I-wAwn1Eqa5esggbc.png"
      }
    },
    {
      "name": "Dart Goblin",
      "id": 26000040,
      "level": 9,
      "maxLevel": 11,
      "count": 871,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BmpK3bqEAviflqHCdxxnfm-_l3pRPJw3qxHkwS55nCY.png"
      }
    },
    {
      "name": "Fire Spirit",
      "id": 26000031,
      "level": 10,
      "maxLevel": 13,
      "count": 5873,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/16-BqusVvynIgYI8_Jci3LDC-r8AI_xaIYLgXqtlmS8.png"
      }
    },
    {
      "name": "Inferno Dragon",
      "id": 26000037,
      "level": 3,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/y5HDbKtTbWG6En6TGWU0xoVIGs1-iQpIP4HC-VM7u8A.png"
      }
    },
    {
      "name": "Royal Hogs",
      "id": 26000059,
      "level": 8,
      "maxLevel": 11,
      "count": 908,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/ASSQJG_MoVq9e81HZzo4bynMnyLNpNJMfSLb3hqydOw.png"
      }
    },
    {
      "name": "Elite Barbarians",
      "id": 26000043,
      "level": 10,
      "maxLevel": 13,
      "count": 7187,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"
      }
    },
    {
      "name": "Goblin Giant",
      "id": 26000060,
      "level": 2,
      "maxLevel": 8,
      "count": 145,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/SoW16cY3jXBwaTDvb39DkqiVsoFVaDWbzf5QBYphJrY.png"
      }
    },
    {
      "name": "Archers",
      "id": 26000001,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/W4Hmp8MTSdXANN8KdblbtHwtsbt0o749BbxNqmJYfA8.png"
      }
    },
    {
      "name": "Minion Horde",
      "id": 26000022,
      "level": 11,
      "maxLevel": 13,
      "count": 7000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Wyjq5l0IXHTkX9Rmpap6HaH08MvjbxFp1xBO9a47YSI.png"
      }
    },
    {
      "name": "Wall Breakers",
      "id": 26000058,
      "level": 4,
      "maxLevel": 8,
      "count": 168,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_xPphEfC8eEwFNrfU3cMQG9-f5JaLQ31ARCA7l3XtW4.png"
      }
    },
    {
      "name": "Electro Wizard",
      "id": 26000042,
      "level": 3,
      "maxLevel": 5,
      "count": 6,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/RsFaHgB3w6vXsTjXdPr3x8l_GbV9TbOUCvIx07prbrQ.png"
      }
    },
    {
      "name": "Graveyard",
      "id": 28000010,
      "level": 3,
      "maxLevel": 5,
      "count": 5,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Icp8BIyyfBTj1ncCJS7mb82SY7TPV-MAE-J2L2R48DI.png"
      }
    },
    {
      "name": "Ice Golem",
      "id": 26000038,
      "level": 8,
      "maxLevel": 11,
      "count": 1278,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/r05cmpwV1o7i7FHodtZwW3fmjbXCW34IJCsDEV5cZC4.png"
      }
    },
    {
      "name": "Elixir Golem",
      "id": 26000067,
      "level": 9,
      "maxLevel": 11,
      "count": 282,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/puhMsZjCIqy21HW3hYxjrk_xt8NIPyFqjRy-BeLKZwo.png"
      }
    },
    {
      "name": "Royal Delivery",
      "id": 28000018,
      "level": 8,
      "maxLevel": 13,
      "count": 4009,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/LPg7AGjGI3_xmi7gLLgGC50yKM1jJ2teWkZfoHJcIZo.png"
      }
    },
    {
      "name": "Skeleton Dragons",
      "id": 26000080,
      "level": 1,
      "maxLevel": 13,
      "count": 738,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/qPOtg9uONh47_NLxGhhFc_ww9PlZ6z3Ry507q1NZUXs.png"
      }
    },
    {
      "name": "Electro Spirit",
      "id": 26000084,
      "level": 5,
      "maxLevel": 13,
      "count": 948,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/WKd4-IAFsgPpMo7dDi9sujmYjRhOMEWiE07OUJpvD9g.png"
      }
    },
    {
      "name": "Electro Giant",
      "id": 26000085,
      "level": 3,
      "maxLevel": 8,
      "count": 16,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_uChZkNHAMq6tPb3v6A49xinOe3CnhjstOhG6OZbPYc.png"
      }
    },
    {
      "name": "Mother Witch",
      "id": 26000083,
      "level": 1,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fO-Xah8XZkYKaSK9SCp3wnzwxtvIhun9NVY-zzte1Ng.png"
      }
    },
    {
      "name": "Zap",
      "id": 28000008,
      "level": 12,
      "maxLevel": 13,
      "count": 4217,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png"
      }
    },
    {
      "name": "Goblin Barrel",
      "id": 28000004,
      "level": 7,
      "maxLevel": 8,
      "count": 6,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png"
      }
    },
    {
      "name": "Furnace",
      "id": 27000010,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/iqbDiG7yYRIzvCPXdt9zPb3IvMt7F7Gi4wIPnh2x4aI.png"
      }
    },
    {
      "name": "Tesla",
      "id": 27000006,
      "level": 12,
      "maxLevel": 13,
      "count": 4498,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/OiwnGrxFMNiHetYEerE-UZt0L_uYNzFY7qV_CA_OxR4.png"
      }
    },
    {
      "name": "Giant Snowball",
      "id": 28000017,
      "level": 11,
      "maxLevel": 13,
      "count": 5635,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/7MaJLa6hK9WN2_VIshuh5DIDfGwm0wEv98gXtAxLDPs.png"
      }
    },
    {
      "name": "Spear Goblins",
      "id": 26000019,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/FSDFotjaXidI4ku_WFpVCTWS1hKGnFh1sxX0lxM43_E.png"
      }
    },
    {
      "name": "Giant",
      "id": 26000003,
      "level": 9,
      "maxLevel": 11,
      "count": 837,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Axr4ox5_b7edmLsoHxBX3vmgijAIibuF6RImTbqLlXE.png"
      }
    },
    {
      "name": "Prince",
      "id": 26000016,
      "level": 7,
      "maxLevel": 8,
      "count": 98,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/3JntJV62aY0G1Qh6LIs-ek-0ayeYFY3VItpG7cb9I60.png"
      }
    },
    {
      "name": "Dark Prince",
      "id": 26000027,
      "level": 7,
      "maxLevel": 8,
      "count": 73,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/M7fXlrKXHu2IvpSGpk36kXVstslbR08Bbxcy0jQcln8.png"
      }
    },
    {
      "name": "Knight",
      "id": 26000000,
      "level": 12,
      "maxLevel": 13,
      "count": 4003,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png"
      }
    },
    {
      "name": "Earthquake",
      "id": 28000014,
      "level": 9,
      "maxLevel": 11,
      "count": 243,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/XeQXcrUu59C52DslyZVwCnbi4yamID-WxfVZLShgZmE.png"
      }
    },
    {
      "name": "Royal Ghost",
      "id": 26000050,
      "level": 3,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/3En2cz0ISQAaMTHY3hj3rTveFN2kJYq-H4VxvdJNvCM.png"
      }
    },
    {
      "name": "Miner",
      "id": 26000032,
      "level": 5,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Y4yWvdwBCg2FpAZgs8T09Gy34WOwpLZW-ttL52Ae8NE.png"
      }
    },
    {
      "name": "Firecracker",
      "id": 26000064,
      "level": 12,
      "maxLevel": 13,
      "count": 727,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/c1rL3LO1U2D9-TkeFfAC18gP3AO8ztSwrcHMZplwL2Q.png"
      }
    },
    {
      "name": "Poison",
      "id": 28000009,
      "level": 7,
      "maxLevel": 8,
      "count": 11,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/98HDkG2189yOULcVG9jz2QbJKtfuhH21DIrIjkOjxI8.png"
      }
    },
    {
      "name": "Goblin Drill",
      "id": 27000013,
      "level": 1,
      "maxLevel": 8,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/eN2TKUYbih-26yBi0xy5LVFOA0zDftgDqxxnVfdIg1o.png"
      }
    },
    {
      "name": "Valkyrie",
      "id": 26000011,
      "level": 10,
      "maxLevel": 11,
      "count": 743,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png"
      }
    },
    {
      "name": "Skeleton Barrel",
      "id": 26000056,
      "level": 11,
      "maxLevel": 13,
      "count": 5502,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vCB4DWCcrGbTkarjcOiVz4aNDx6GWLm0yUepg9E1MGo.png"
      }
    },
    {
      "name": "Rocket",
      "id": 28000003,
      "level": 8,
      "maxLevel": 11,
      "count": 890,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ie07nQNK9CjhKOa4-arFAewi4EroqaA-86Xo7r5tx94.png"
      }
    },
    {
      "name": "Executioner",
      "id": 26000045,
      "level": 7,
      "maxLevel": 8,
      "count": 18,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/9XL5BP2mqzV8kza6KF8rOxrpCZTyuGLp2l413DTjEoM.png"
      }
    },
    {
      "name": "Baby Dragon",
      "id": 26000015,
      "level": 7,
      "maxLevel": 8,
      "count": 113,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cjC9n4AvEZJ3urkVh-rwBkJ-aRSsydIMqSAV48hAih0.png"
      }
    },
    {
      "name": "Bomber",
      "id": 26000013,
      "level": 12,
      "maxLevel": 13,
      "count": 3938,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/12n1CesxKIcqVYntjxcF36EFA-ONw7Z-DoL0_rQrbdo.png"
      }
    },
    {
      "name": "Electro Dragon",
      "id": 26000063,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/tN9h6lnMNPCNsx0LMFmvpHgznbDZ1fBRkx-C7UfNmfY.png"
      }
    },
    {
      "name": "Golem",
      "id": 26000009,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png"
      }
    },
    {
      "name": "Lumberjack",
      "id": 26000035,
      "level": 3,
      "maxLevel": 5,
      "count": 7,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/E6RWrnCuk13xMX5OE1EQtLEKTZQV6B78d00y8PlXt6Q.png"
      }
    },
    {
      "name": "Night Witch",
      "id": 26000048,
      "level": 5,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NpCrXDEDBBJgNv9QrBAcJmmMFbS7pe3KCY8xJ5VB18A.png"
      }
    },
    {
      "name": "Skeleton Army",
      "id": 26000012,
      "level": 6,
      "maxLevel": 8,
      "count": 92,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png"
      }
    },
    {
      "name": "Tornado",
      "id": 28000012,
      "level": 6,
      "maxLevel": 8,
      "count": 100,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QJB-QK1QJHdw4hjpAwVSyZBozc2ZWAR9pQ-SMUyKaT0.png"
      }
    }
  ],
  "currentDeck": [
    {
      "name": "Baby Dragon",
      "id": 26000015,
      "level": 7,
      "maxLevel": 8,
      "count": 113,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cjC9n4AvEZJ3urkVh-rwBkJ-aRSsydIMqSAV48hAih0.png"
      }
    },
    {
      "name": "Bomber",
      "id": 26000013,
      "level": 12,
      "maxLevel": 13,
      "count": 3938,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/12n1CesxKIcqVYntjxcF36EFA-ONw7Z-DoL0_rQrbdo.png"
      }
    },
    {
      "name": "Electro Dragon",
      "id": 26000063,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/tN9h6lnMNPCNsx0LMFmvpHgznbDZ1fBRkx-C7UfNmfY.png"
      }
    },
    {
      "name": "Golem",
      "id": 26000009,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png"
      }
    },
    {
      "name": "Lumberjack",
      "id": 26000035,
      "level": 3,
      "maxLevel": 5,
      "count": 7,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/E6RWrnCuk13xMX5OE1EQtLEKTZQV6B78d00y8PlXt6Q.png"
      }
    },
    {
      "name": "Night Witch",
      "id": 26000048,
      "level": 5,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NpCrXDEDBBJgNv9QrBAcJmmMFbS7pe3KCY8xJ5VB18A.png"
      }
    },
    {
      "name": "Skeleton Army",
      "id": 26000012,
      "level": 6,
      "maxLevel": 8,
      "count": 92,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png"
      }
    },
    {
      "name": "Tornado",
      "id": 28000012,
      "level": 6,
      "maxLevel": 8,
      "count": 100,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QJB-QK1QJHdw4hjpAwVSyZBozc2ZWAR9pQ-SMUyKaT0.png"
      }
    }
  ],
  "currentFavouriteCard": {
    "name": "Golem",
    "id": 26000009,
    "maxLevel": 8,
    "iconUrls": {
      "medium": "https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png"
    }
  },
  "starPoints": 5408
}

PLAYER_3_RESPONSE = {
  "tag": "#LYJVYUUUR",
  "name": "ZEPOL 1244",
  "expLevel": 13,
  "trophies": 5428,
  "bestTrophies": 5932,
  "wins": 9122,
  "losses": 12988,
  "battleCount": 23672,
  "threeCrownWins": 2142,
  "challengeCardsWon": 414,
  "challengeMaxWins": 7,
  "tournamentCardsWon": 0,
  "tournamentBattleCount": 212,
  "role": "coLeader",
  "donations": 1036,
  "donationsReceived": 520,
  "totalDonations": 55367,
  "warDayWins": 33,
  "clanCardsCollected": 93035,
  "clan": {
    "tag": "#9GULPJ9L",
    "name": "AUSCLAN",
    "badgeId": 16000025
  },
  "arena": {
    "id": 54000013,
    "name": "Challenger II"
  },
  "leagueStatistics": {
    "currentSeason": {
      "trophies": 5428,
      "bestTrophies": 5734
    },
    "previousSeason": {
      "id": "2021-05",
      "trophies": 5804,
      "bestTrophies": 5932
    },
    "bestSeason": {
      "id": "2021-04",
      "trophies": 5806
    }
  },
  "badges": [
    {
      "name": "1000Wins",
      "progress": 9122
    },
    {
      "name": "Played1Year",
      "progress": 601
    },
    {
      "name": "TopLeague",
      "progress": 5932
    },
    {
      "name": "ClanWarWins",
      "level": 2,
      "maxLevel": 3,
      "progress": 33,
      "target": 100
    }
  ],
  "achievements": [
    {
      "name": "Team Player",
      "stars": 3,
      "value": 2,
      "target": 1,
      "info": "Join a Clan",
      "completionInfo": None
    },
    {
      "name": "Friend in Need",
      "stars": 3,
      "value": 55367,
      "target": 2500,
      "info": "Donate 2500 cards",
      "completionInfo": None
    },
    {
      "name": "Road to Glory",
      "stars": 3,
      "value": 18,
      "target": 6,
      "info": "Reach Arena 6",
      "completionInfo": None
    },
    {
      "name": "Gatherer",
      "stars": 3,
      "value": 103,
      "target": 40,
      "info": "Collect 40 cards",
      "completionInfo": None
    },
    {
      "name": "TV Royale",
      "stars": 0,
      "value": 0,
      "target": 1,
      "info": "Watch a TV Royale Replay",
      "completionInfo": None
    },
    {
      "name": "Tournament Rewards",
      "stars": 0,
      "value": 0,
      "target": 1000,
      "info": "Win 1000 cards from tournaments",
      "completionInfo": None
    },
    {
      "name": "Tournament Host",
      "stars": 0,
      "value": 0,
      "target": 1,
      "info": "Create and finish one tournament",
      "completionInfo": None
    },
    {
      "name": "Tournament Player",
      "stars": 0,
      "value": 0,
      "target": 1,
      "info": "Join a tournament",
      "completionInfo": None
    },
    {
      "name": "Challenge Streak",
      "stars": 3,
      "value": 15,
      "target": 12,
      "info": "Get 12 wins in a single Challenge",
      "completionInfo": None
    },
    {
      "name": "Practice with Friends",
      "stars": 3,
      "value": 43,
      "target": 10,
      "info": "Win 10 Friendly Battles",
      "completionInfo": None
    },
    {
      "name": "Special Challenge",
      "stars": 3,
      "value": 175,
      "target": 5,
      "info": "Participate in 5 unique Special Event Challenges",
      "completionInfo": None
    },
    {
      "name": "Friend in Need II",
      "stars": 3,
      "value": 55367,
      "target": 25000,
      "info": "Donate 25000 cards",
      "completionInfo": None
    }
  ],
  "cards": [
    {
      "name": "Three Musketeers",
      "id": 26000028,
      "level": 9,
      "maxLevel": 11,
      "count": 1798,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_J2GhbkX3vswaFk1wG-dopwiHyNc_YiPhwroiKF3Mek.png"
      }
    },
    {
      "name": "Royal Giant",
      "id": 26000024,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/mnlRaNtmfpQx2e6mp70sLd0ND-pKPF70Cf87_agEKg4.png"
      }
    },
    {
      "name": "Bowler",
      "id": 26000034,
      "level": 7,
      "maxLevel": 8,
      "count": 199,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/SU4qFXmbQXWjvASxVI6z9IJuTYolx4A0MKK90sTIE88.png"
      }
    },
    {
      "name": "Royal Delivery",
      "id": 28000018,
      "level": 11,
      "maxLevel": 13,
      "count": 7000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/LPg7AGjGI3_xmi7gLLgGC50yKM1jJ2teWkZfoHJcIZo.png"
      }
    },
    {
      "name": "Elixir Collector",
      "id": 27000007,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BGLo3Grsp81c72EpxLLk-Sofk3VY56zahnUNOv3JcT0.png"
      }
    },
    {
      "name": "Goblins",
      "id": 26000002,
      "level": 11,
      "maxLevel": 13,
      "count": 7000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/X_DQUye_OaS3QN6VC9CPw05Fit7wvSm3XegXIXKP--0.png"
      }
    },
    {
      "name": "Royal Recruits",
      "id": 26000047,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jcNyYGUiXXNz3kuz8NBkHNKNREQKraXlb_Ts7rhCIdM.png"
      }
    },
    {
      "name": "Tombstone",
      "id": 27000009,
      "level": 9,
      "maxLevel": 11,
      "count": 1761,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/LjSfSbwQfkZuRJY4pVxKspZ-a0iM5KAhU8w-a_N5Z7Y.png"
      }
    },
    {
      "name": "Guards",
      "id": 26000025,
      "level": 6,
      "maxLevel": 8,
      "count": 288,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/1ArKfLJxYo6_NU_S9cAeIrfbXqWH0oULVJXedxBXQlU.png"
      }
    },
    {
      "name": "Lava Hound",
      "id": 26000029,
      "level": 4,
      "maxLevel": 5,
      "count": 20,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/unicRQ975sBY2oLtfgZbAI56ZvaWz7azj-vXTLxc0r8.png"
      }
    },
    {
      "name": "Earthquake",
      "id": 28000014,
      "level": 9,
      "maxLevel": 11,
      "count": 1798,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/XeQXcrUu59C52DslyZVwCnbi4yamID-WxfVZLShgZmE.png"
      }
    },
    {
      "name": "Barbarians",
      "id": 26000008,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/TvJsuu2S4yhyk1jVYUAQwdKOnW4U77KuWWOTPOWnwfI.png"
      }
    },
    {
      "name": "Cannon",
      "id": 27000000,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/nZK1y-beLxO5vnlyUhK6-2zH2NzXJwqykcosqQ1cmZ8.png"
      }
    },
    {
      "name": "Mirror",
      "id": 28000006,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/wC6Cm9rKLEOk72zTsukVwxewKIoO4ZcMJun54zCPWvA.png"
      }
    },
    {
      "name": "Flying Machine",
      "id": 26000057,
      "level": 9,
      "maxLevel": 11,
      "count": 1800,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/hzKNE3QwFcrSrDDRuVW3QY_OnrDPijSiIp-PsWgFevE.png"
      }
    },
    {
      "name": "Royal Hogs",
      "id": 26000059,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/ASSQJG_MoVq9e81HZzo4bynMnyLNpNJMfSLb3hqydOw.png"
      }
    },
    {
      "name": "Goblin Hut",
      "id": 27000001,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/l8ZdzzNLcwB4u7ihGgxNFQOjCT_njFuAhZr7D6PRF7E.png"
      }
    },
    {
      "name": "Skeleton Dragons",
      "id": 26000080,
      "level": 11,
      "maxLevel": 13,
      "count": 7000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/qPOtg9uONh47_NLxGhhFc_ww9PlZ6z3Ry507q1NZUXs.png"
      }
    },
    {
      "name": "Mini P.E.K.K.A",
      "id": 26000018,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png"
      }
    },
    {
      "name": "Ice Spirit",
      "id": 26000030,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lv1budiafU9XmSdrDkk0NYyqASAFYyZ06CPysXKZXlA.png"
      }
    },
    {
      "name": "Lumberjack",
      "id": 26000035,
      "level": 3,
      "maxLevel": 5,
      "count": 6,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/E6RWrnCuk13xMX5OE1EQtLEKTZQV6B78d00y8PlXt6Q.png"
      }
    },
    {
      "name": "Wall Breakers",
      "id": 26000058,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_xPphEfC8eEwFNrfU3cMQG9-f5JaLQ31ARCA7l3XtW4.png"
      }
    },
    {
      "name": "Spear Goblins",
      "id": 26000019,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/FSDFotjaXidI4ku_WFpVCTWS1hKGnFh1sxX0lxM43_E.png"
      }
    },
    {
      "name": "Sparky",
      "id": 26000033,
      "level": 3,
      "maxLevel": 5,
      "count": 15,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/2GKMkBrArZXgQxf2ygFjDs4VvGYPbx8F6Lj_68iVhIM.png"
      }
    },
    {
      "name": "Furnace",
      "id": 27000010,
      "level": 11,
      "starLevel": 1,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/iqbDiG7yYRIzvCPXdt9zPb3IvMt7F7Gi4wIPnh2x4aI.png"
      }
    },
    {
      "name": "Lightning",
      "id": 28000007,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fpnESbYqe5GyZmaVVYe-SEu7tE0Kxh_HZyVigzvLjks.png"
      }
    },
    {
      "name": "Poison",
      "id": 28000009,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/98HDkG2189yOULcVG9jz2QbJKtfuhH21DIrIjkOjxI8.png"
      }
    },
    {
      "name": "Ice Golem",
      "id": 26000038,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/r05cmpwV1o7i7FHodtZwW3fmjbXCW34IJCsDEV5cZC4.png"
      }
    },
    {
      "name": "Wizard",
      "id": 26000017,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Mej7vnv4H_3p_8qPs_N6_GKahy6HDr7pU7i9eTHS84U.png"
      }
    },
    {
      "name": "Baby Dragon",
      "id": 26000015,
      "level": 7,
      "maxLevel": 8,
      "count": 172,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cjC9n4AvEZJ3urkVh-rwBkJ-aRSsydIMqSAV48hAih0.png"
      }
    },
    {
      "name": "Fireball",
      "id": 28000000,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lZD9MILQv7O-P3XBr_xOLS5idwuz3_7Ws9G60U36yhc.png"
      }
    },
    {
      "name": "Zappies",
      "id": 26000052,
      "level": 9,
      "maxLevel": 11,
      "count": 1754,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QZfHRpLRmutZbCr5fpLnTpIp89vLI6NrAwzGZ8tHEc4.png"
      }
    },
    {
      "name": "Giant Skeleton",
      "id": 26000020,
      "level": 7,
      "maxLevel": 8,
      "count": 200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0p0gd0XaVRu1Hb1iSG1hTYbz2AN6aEiZnhaAib5O8Z8.png"
      }
    },
    {
      "name": "Giant Snowball",
      "id": 28000017,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/7MaJLa6hK9WN2_VIshuh5DIDfGwm0wEv98gXtAxLDPs.png"
      }
    },
    {
      "name": "Giant",
      "id": 26000003,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Axr4ox5_b7edmLsoHxBX3vmgijAIibuF6RImTbqLlXE.png"
      }
    },
    {
      "name": "Rocket",
      "id": 28000003,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ie07nQNK9CjhKOa4-arFAewi4EroqaA-86Xo7r5tx94.png"
      }
    },
    {
      "name": "Fire Spirit",
      "id": 26000031,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/16-BqusVvynIgYI8_Jci3LDC-r8AI_xaIYLgXqtlmS8.png"
      }
    },
    {
      "name": "Hog Rider",
      "id": 26000021,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Ubu0oUl8tZkusnkZf8Xv9Vno5IO29Y-jbZ4fhoNJ5oc.png"
      }
    },
    {
      "name": "Fisherman",
      "id": 26000061,
      "level": 4,
      "maxLevel": 5,
      "count": 19,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/U2KZ3g0wyufcuA5P2Xrn3Z3lr1WiJmc5S0IWOZHgizQ.png"
      }
    },
    {
      "name": "Hunter",
      "id": 26000044,
      "level": 7,
      "maxLevel": 8,
      "count": 200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/VNabB1WKnYtYRSG7X_FZfnZjQDHTBs9A96OGMFmecrA.png"
      }
    },
    {
      "name": "Bats",
      "id": 26000049,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/EnIcvO21hxiNpoI-zO6MDjLmzwPbq8Z4JPo2OKoVUjU.png"
      }
    },
    {
      "name": "Balloon",
      "id": 26000006,
      "level": 7,
      "maxLevel": 8,
      "count": 200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/qBipxLo-3hhCnPrApp2Nn3b2NgrSrvwzWytvREev0CY.png"
      }
    },
    {
      "name": "Barbarian Hut",
      "id": 27000005,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/ho0nOG2y3Ch86elHHcocQs8Fv_QNe0cFJ2CijsxABZA.png"
      }
    },
    {
      "name": "Heal Spirit",
      "id": 28000016,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/GITl06sa2nGRLPvboyXbGEv5E3I-wAwn1Eqa5esggbc.png"
      }
    },
    {
      "name": "Miner",
      "id": 26000032,
      "level": 4,
      "maxLevel": 5,
      "count": 13,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Y4yWvdwBCg2FpAZgs8T09Gy34WOwpLZW-ttL52Ae8NE.png"
      }
    },
    {
      "name": "Witch",
      "id": 26000007,
      "level": 6,
      "maxLevel": 8,
      "count": 206,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/cfwk1vzehVyHC-uloEIH6NOI0hOdofCutR5PyhIgO6w.png"
      }
    },
    {
      "name": "Musketeer",
      "id": 26000014,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Tex1C48UTq9FKtAX-3tzG0FJmc9jzncUZG3bb5Vf-Ds.png"
      }
    },
    {
      "name": "Cannon Cart",
      "id": 26000054,
      "level": 7,
      "maxLevel": 8,
      "count": 141,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/aqwxRz8HXzqlMCO4WMXNA1txynjXTsLinknqsgZLbok.png"
      }
    },
    {
      "name": "Minions",
      "id": 26000005,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/yHGpoEnmUWPGV_hBbhn-Kk-Bs838OjGzWzJJlQpQKQA.png"
      }
    },
    {
      "name": "Dark Prince",
      "id": 26000027,
      "level": 7,
      "maxLevel": 8,
      "count": 136,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/M7fXlrKXHu2IvpSGpk36kXVstslbR08Bbxcy0jQcln8.png"
      }
    },
    {
      "name": "Archers",
      "id": 26000001,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/W4Hmp8MTSdXANN8KdblbtHwtsbt0o749BbxNqmJYfA8.png"
      }
    },
    {
      "name": "Electro Giant",
      "id": 26000085,
      "level": 7,
      "maxLevel": 8,
      "count": 166,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_uChZkNHAMq6tPb3v6A49xinOe3CnhjstOhG6OZbPYc.png"
      }
    },
    {
      "name": "X-Bow",
      "id": 27000008,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/zVQ9Hme1hlj9Dc6e1ORl9xWwglcSrP7ejow5mAhLUJc.png"
      }
    },
    {
      "name": "Battle Healer",
      "id": 26000068,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/KdwXcoigS2Kg-cgA7BJJIANbUJG6SNgjetRQ-MegZ08.png"
      }
    },
    {
      "name": "Mother Witch",
      "id": 26000083,
      "level": 5,
      "starLevel": 1,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fO-Xah8XZkYKaSK9SCp3wnzwxtvIhun9NVY-zzte1Ng.png"
      }
    },
    {
      "name": "Rage",
      "id": 28000002,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png"
      }
    },
    {
      "name": "Tornado",
      "id": 28000012,
      "level": 7,
      "maxLevel": 8,
      "count": 200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QJB-QK1QJHdw4hjpAwVSyZBozc2ZWAR9pQ-SMUyKaT0.png"
      }
    },
    {
      "name": "Elixir Golem",
      "id": 26000067,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/puhMsZjCIqy21HW3hYxjrk_xt8NIPyFqjRy-BeLKZwo.png"
      }
    },
    {
      "name": "Freeze",
      "id": 28000005,
      "level": 7,
      "maxLevel": 8,
      "count": 200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/I1M20_Zs_p_BS1NaNIVQjuMJkYI_1-ePtwYZahn0JXQ.png"
      }
    },
    {
      "name": "Rascals",
      "id": 26000053,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/KV48DfwVHKx9XCjzBdk3daT_Eb52Me4VgjVO7WctRc4.png"
      }
    },
    {
      "name": "Inferno Tower",
      "id": 27000003,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png"
      }
    },
    {
      "name": "Magic Archer",
      "id": 26000062,
      "level": 5,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Avli3W7BxU9HQ2SoLiXnBgGx25FoNXUSFm7OcAk68ek.png"
      }
    },
    {
      "name": "P.E.K.K.A",
      "id": 26000004,
      "level": 6,
      "maxLevel": 8,
      "count": 300,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/MlArURKhn_zWAZY-Xj1qIRKLVKquarG25BXDjUQajNs.png"
      }
    },
    {
      "name": "Battle Ram",
      "id": 26000036,
      "level": 10,
      "maxLevel": 11,
      "count": 1000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/dyc50V2cplKi4H7pq1B3I36pl_sEH5DQrNHboS_dbbM.png"
      }
    },
    {
      "name": "Royal Ghost",
      "id": 26000050,
      "level": 4,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/3En2cz0ISQAaMTHY3hj3rTveFN2kJYq-H4VxvdJNvCM.png"
      }
    },
    {
      "name": "Barbarian Barrel",
      "id": 28000015,
      "level": 7,
      "maxLevel": 8,
      "count": 200,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Gb0G1yNy0i5cIGUHin8uoFWxqntNtRPhY_jeMXg7HnA.png"
      }
    },
    {
      "name": "Goblin Gang",
      "id": 26000041,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NHflxzVAQT4oAz7eDfdueqpictb5vrWezn1nuqFhE4w.png"
      }
    },
    {
      "name": "Goblin Drill",
      "id": 27000013,
      "level": 6,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/eN2TKUYbih-26yBi0xy5LVFOA0zDftgDqxxnVfdIg1o.png"
      }
    },
    {
      "name": "Goblin Cage",
      "id": 27000012,
      "level": 9,
      "maxLevel": 11,
      "count": 1800,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vD24bBgK4rSq7wx5QEbuqChtPMRFviL_ep76GwQw1yA.png"
      }
    },
    {
      "name": "Clone",
      "id": 28000013,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png"
      }
    },
    {
      "name": "Electro Spirit",
      "id": 26000084,
      "level": 11,
      "maxLevel": 13,
      "count": 6960,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/WKd4-IAFsgPpMo7dDi9sujmYjRhOMEWiE07OUJpvD9g.png"
      }
    },
    {
      "name": "Elite Barbarians",
      "id": 26000043,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"
      }
    },
    {
      "name": "Executioner",
      "id": 26000045,
      "level": 6,
      "maxLevel": 8,
      "count": 178,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/9XL5BP2mqzV8kza6KF8rOxrpCZTyuGLp2l413DTjEoM.png"
      }
    },
    {
      "name": "Tesla",
      "id": 27000006,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/OiwnGrxFMNiHetYEerE-UZt0L_uYNzFY7qV_CA_OxR4.png"
      }
    },
    {
      "name": "Bomber",
      "id": 26000013,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/12n1CesxKIcqVYntjxcF36EFA-ONw7Z-DoL0_rQrbdo.png"
      }
    },
    {
      "name": "Electro Dragon",
      "id": 26000063,
      "level": 7,
      "maxLevel": 8,
      "count": 199,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/tN9h6lnMNPCNsx0LMFmvpHgznbDZ1fBRkx-C7UfNmfY.png"
      }
    },
    {
      "name": "Mortar",
      "id": 27000002,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/lPOSw6H7YOHq2miSCrf7ZDL3ANjhJdPPDYOTujdNrVE.png"
      }
    },
    {
      "name": "Night Witch",
      "id": 26000048,
      "level": 4,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/NpCrXDEDBBJgNv9QrBAcJmmMFbS7pe3KCY8xJ5VB18A.png"
      }
    },
    {
      "name": "Valkyrie",
      "id": 26000011,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png"
      }
    },
    {
      "name": "Minion Horde",
      "id": 26000022,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Wyjq5l0IXHTkX9Rmpap6HaH08MvjbxFp1xBO9a47YSI.png"
      }
    },
    {
      "name": "Goblin Giant",
      "id": 26000060,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/SoW16cY3jXBwaTDvb39DkqiVsoFVaDWbzf5QBYphJrY.png"
      }
    },
    {
      "name": "Bandit",
      "id": 26000046,
      "level": 4,
      "maxLevel": 5,
      "count": 1,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QWDdXMKJNpv0go-HYaWQWP6p8uIOHjqn-zX7G0p3DyM.png"
      }
    },
    {
      "name": "Ice Wizard",
      "id": 26000023,
      "level": 3,
      "maxLevel": 5,
      "count": 14,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/W3dkw0HTw9n1jB-zbknY2w3wHuyuLxSRIAV5fUT1SEY.png"
      }
    },
    {
      "name": "Graveyard",
      "id": 28000010,
      "level": 4,
      "maxLevel": 5,
      "count": 12,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Icp8BIyyfBTj1ncCJS7mb82SY7TPV-MAE-J2L2R48DI.png"
      }
    },
    {
      "name": "Firecracker",
      "id": 26000064,
      "level": 13,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/c1rL3LO1U2D9-TkeFfAC18gP3AO8ztSwrcHMZplwL2Q.png"
      }
    },
    {
      "name": "Inferno Dragon",
      "id": 26000037,
      "level": 4,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/y5HDbKtTbWG6En6TGWU0xoVIGs1-iQpIP4HC-VM7u8A.png"
      }
    },
    {
      "name": "Ram Rider",
      "id": 26000051,
      "level": 3,
      "maxLevel": 5,
      "count": 2,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/QaJyerT7f7oMyZ3Fv1glKymtLSvx7YUXisAulxl7zRI.png"
      }
    },
    {
      "name": "Zap",
      "id": 28000008,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png"
      }
    },
    {
      "name": "Mega Minion",
      "id": 26000039,
      "level": 11,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/-T_e4YLbuhPBKbYnBwQfXgynNpp5eOIN_0RracYwL9c.png"
      }
    },
    {
      "name": "Golem",
      "id": 26000009,
      "level": 8,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png"
      }
    },
    {
      "name": "Prince",
      "id": 26000016,
      "level": 8,
      "starLevel": 1,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/3JntJV62aY0G1Qh6LIs-ek-0ayeYFY3VItpG7cb9I60.png"
      }
    },
    {
      "name": "Electro Wizard",
      "id": 26000042,
      "level": 4,
      "maxLevel": 5,
      "count": 4,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/RsFaHgB3w6vXsTjXdPr3x8l_GbV9TbOUCvIx07prbrQ.png"
      }
    },
    {
      "name": "Skeleton Army",
      "id": 26000012,
      "level": 7,
      "maxLevel": 8,
      "count": 42,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png"
      }
    },
    {
      "name": "Arrows",
      "id": 28000001,
      "level": 12,
      "maxLevel": 13,
      "count": 5000,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/Flsoci-Y6y8ZFVi5uRFTmgkPnCmMyMVrU7YmmuPvSBo.png"
      }
    },
    {
      "name": "Mega Knight",
      "id": 26000055,
      "level": 5,
      "starLevel": 1,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/O2NycChSNhn_UK9nqBXUhhC_lILkiANzPuJjtjoz0CE.png"
      }
    },
    {
      "name": "The Log",
      "id": 28000011,
      "level": 5,
      "starLevel": 1,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_iDwuDLexHPFZ_x4_a0eP-rxCS6vwWgTs6DLauwwoaY.png"
      }
    },
    {
      "name": "Princess",
      "id": 26000026,
      "level": 5,
      "starLevel": 1,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png"
      }
    },
    {
      "name": "Bomb Tower",
      "id": 27000004,
      "level": 11,
      "starLevel": 1,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/rirYRyHPc97emRjoH-c1O8uZCBzPVnToaGuNGusF3TQ.png"
      }
    },
    {
      "name": "Skeletons",
      "id": 26000010,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/oO7iKMU5m0cdxhYPZA3nWQiAUh2yoGgdThLWB1rVSec.png"
      }
    },
    {
      "name": "Skeleton Barrel",
      "id": 26000056,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vCB4DWCcrGbTkarjcOiVz4aNDx6GWLm0yUepg9E1MGo.png"
      }
    },
    {
      "name": "Dart Goblin",
      "id": 26000040,
      "level": 11,
      "starLevel": 2,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BmpK3bqEAviflqHCdxxnfm-_l3pRPJw3qxHkwS55nCY.png"
      }
    },
    {
      "name": "Goblin Barrel",
      "id": 28000004,
      "level": 8,
      "starLevel": 3,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png"
      }
    },
    {
      "name": "Knight",
      "id": 26000000,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png"
      }
    }
  ],
  "currentDeck": [
    {
      "name": "The Log",
      "id": 28000011,
      "level": 5,
      "starLevel": 1,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/_iDwuDLexHPFZ_x4_a0eP-rxCS6vwWgTs6DLauwwoaY.png"
      }
    },
    {
      "name": "Princess",
      "id": 26000026,
      "level": 5,
      "starLevel": 1,
      "maxLevel": 5,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png"
      }
    },
    {
      "name": "Bomb Tower",
      "id": 27000004,
      "level": 11,
      "starLevel": 1,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/rirYRyHPc97emRjoH-c1O8uZCBzPVnToaGuNGusF3TQ.png"
      }
    },
    {
      "name": "Skeletons",
      "id": 26000010,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/oO7iKMU5m0cdxhYPZA3nWQiAUh2yoGgdThLWB1rVSec.png"
      }
    },
    {
      "name": "Skeleton Barrel",
      "id": 26000056,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/vCB4DWCcrGbTkarjcOiVz4aNDx6GWLm0yUepg9E1MGo.png"
      }
    },
    {
      "name": "Dart Goblin",
      "id": 26000040,
      "level": 11,
      "starLevel": 2,
      "maxLevel": 11,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/BmpK3bqEAviflqHCdxxnfm-_l3pRPJw3qxHkwS55nCY.png"
      }
    },
    {
      "name": "Goblin Barrel",
      "id": 28000004,
      "level": 8,
      "starLevel": 3,
      "maxLevel": 8,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png"
      }
    },
    {
      "name": "Knight",
      "id": 26000000,
      "level": 13,
      "starLevel": 1,
      "maxLevel": 13,
      "count": 0,
      "iconUrls": {
        "medium": "https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png"
      }
    }
  ],
  "currentFavouriteCard": {
    "name": "Princess",
    "id": 26000026,
    "maxLevel": 5,
    "iconUrls": {
      "medium": "https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png"
    }
  },
  "starPoints": 15220
}
