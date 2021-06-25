import re

import cloudscraper # Not sure if will work
import requests
from bs4 import BeautifulSoup


class RoyaleApiWebsiteScraper:
    def __init__(self):
        self.soup = BeautifulSoup()

    def get_html_soup(self, url):
        # response = requests.get(url)
        # Trying with cloudFlare scraper
        # scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()
        response = scraper.get(url)
        print(response.text)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            raise ValueError(
                f'Encounter a problem with royaleAPI.com. Status code: [{response.status_code}]'
            )

    def get_test_html(self):
        with open('temp.html') as fp:
            return BeautifulSoup(fp, 'html.parser')

    def get_player_table(self, clan_tag):
        clan_tag = clan_tag.replace('#', '').upper()
        request_url = f'https://royaleapi.com/clan/{clan_tag}/war/race'
        # For now just load from the file and test so we don't get DDOS-ed lol
        # soup = self.get_test_html()
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
            data.append(all_cols) # Get rid of empty values
        
        boat_attackers = [p for p in data if int(p[5]) > 0]

        return boat_attackers


# cave man testing
# scraper = RoyaleApiWebsiteScraper()
# scraper.get_player_table('9GULPJ9L')