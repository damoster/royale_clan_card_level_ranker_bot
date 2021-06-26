import re
import socket
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup
from requests.packages import urllib3


# To hide warning about:
# InsecureRequestWarning: Unverified HTTPS request is being made to host 'royaleapi.com'. Adding certificate verification
# is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RoyaleApiWebsiteScraper:
    def __init__(self):
        self.soup = BeautifulSoup()

    def get_html_soup(self, url):
        # Followed approach here to avoid Cloudflare captcha / cookie / JS check
        # https://stackoverflow.com/questions/62684468/pythons-requests-triggers-cloudflares-security-while-urllib-does-not
        headers = OrderedDict({
            'Host': "royaleapi.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        })
        s = requests.Session()
        s.headers = headers
        response = s.get(url, verify=False)
        response.close()  # Close connection to the server

        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            raise ValueError(
                f'Encounter a problem with royaleAPI.com. Status code: [{response.status_code}]'
            )

    def get_war_participation_table(self, clan_tag):
        clan_tag = clan_tag.replace('#', '').upper()
        request_url = f'https://royaleapi.com/clan/{clan_tag}/war/race'
        soup = self.get_html_soup(request_url)

        data = []
        table = soup.find("table", {"class": "sortable_participant"})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            # Sample cols[1] looks like 'the ironstein\n    \n\n    Co-leader\n    \n\n\n4\n20\n0\n1500'
            all_cols = [cols[0]] + [e for e in re.split('\n+ *', cols[1]) if e]
            # Columns at time of writing are:
            # Rank, Name, Role, DecksUsedToday, TotalDecksUsed, BoatAttacks, Medal
            if len(all_cols) != 7:
                raise ValueError('Structure of Table being webscraped has changed, no longer in expected format')
            data.append(all_cols)  # Get rid of empty values

        boat_attackers = [p for p in data if int(p[5]) > 0]

        clan_logo = soup.find('a', {'class': 'active_clan'}).find('div',{'class': 'badge'}).find('img')['src']
        clan_name = re.split(f' *#{clan_tag}', soup.find('title').string)[0]
        clan_info = {'name': clan_name, 'tag': f'#{clan_tag}', 'logo_url': clan_logo}
        return clan_info, boat_attackers
