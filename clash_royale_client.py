import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ClashRoyaleClient:
    def __init__(self):
        self.base_url = 'https://api.clashroyale.com/v1'
        self.auth_token = os.getenv('ROYALE_API_KEY')
        self.request_headers = {'Authorization': 'Bearer {}'.format(self.auth_token)}

    # url param pre-condition -> clan_tag should not have # and all caps
    def get_clan_members(self, clan_tag):
        cleaned_tag = clan_tag.replace('#','').upper()
        # Note: the '%23' is # when it is in the url
        request_url = '{}/clans/%23{}/members'.format(self.base_url, cleaned_tag)
        response = requests.get(request_url, headers=self.request_headers)
        return response.json()

    # url param pre-condition -> player_tag should not have # and all caps
    def get_player_info(self, player_tag):
        cleaned_tag = player_tag.replace('#','').upper()
        request_url = '{}/players/%23{}'.format(self.base_url, cleaned_tag)
        response = requests.get(request_url, headers=self.request_headers)
        return response.json()
