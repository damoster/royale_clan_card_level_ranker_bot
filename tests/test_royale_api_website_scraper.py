import os

import unittest
from bs4 import BeautifulSoup
from mockito import when

from royale_api_website_scraper import RoyaleApiWebsiteScraper


THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestRoyaleApiWebsiteScraper(unittest.TestCase):

    def test_get_war_participation_table(self):
        royale_api_website_scraper = RoyaleApiWebsiteScraper()
        clan_tag = "#9GULPJ9L"
        request_url = 'https://royaleapi.com/clan/{}/war/race'.format(clan_tag.replace('#', ''))
        with open(os.path.join(THIS_DIR, 'resources/royale_api_river_race.html')) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        # Mock GET request
        when(royale_api_website_scraper).get_html_soup(request_url).thenReturn(soup)

        clan_info, result = royale_api_website_scraper.get_war_participation_table(clan_tag)
        self.assertEqual('AUSCLAN', clan_info['name'])
        self.assertEqual('https://cdn.royaleapi.com/static/img/badge/gold-2/Skull_02.png?t=6b868473c', clan_info['logo_url'])
        self.assertEqual(
            result,
            [['33', '- Lpak -', 'Member', '4', '8', '8', '800']]
        )


if __name__ == '__main__':
    unittest.main()
