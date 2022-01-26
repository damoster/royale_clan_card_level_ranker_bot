import os

import requests


# pre-condition: Assumes environment variable 'ROYALE_API_KEY' has been set
class ClashRoyaleClient:
    def __init__(self):
        # self.base_url = 'https://api.clashroyale.com/v1' - Leaving the original Royal API url as it might be needed in the future
        self.base_url = 'https://proxy.royaleapi.dev/v1'
        self.auth_token = os.getenv('ROYALE_API_KEY')
        self.request_headers = {'Authorization': 'Bearer {}'.format(self.auth_token)}

    def make_request(self, request_url, method_name):
        response = requests.get(request_url, headers=self.request_headers)
        if response.status_code == 200:
            return response.json()
        else:
            # TODO is throwing an exception the best way of handling this? Should add exception handlinig at top level probs
            raise ValueError(
                "[{}] recieved response code: {}. Error body: {}".format(method_name, response.status_code, response.json())
            )

    # url param pre-condition -> clan_tag should not have # and all caps
    def get_clan_info(self, clan_tag):
        cleaned_tag = clan_tag.replace('#', '').upper()
        # Note: the '%23' is # when it is in the url
        request_url = '{}/clans/%23{}'.format(self.base_url, cleaned_tag)
        return self.make_request(request_url, 'get_clan_info')

    # url param pre-condition -> player_tag should not have # and all caps
    def get_player_info(self, player_tag):
        cleaned_tag = player_tag.replace('#', '').upper()
        request_url = '{}/players/%23{}'.format(self.base_url, cleaned_tag)
        return self.make_request(request_url, 'get_player_info')

    # url param pre-conditoin -> clan_tag should not have # and all caps
    def get_river_race_log(self, clan_tag):
        return True
