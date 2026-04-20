from unittest import TestCase

from research_summary.tools.web_scrap import web_scrape


class Test(TestCase):
    def test_web_scrape(self):
        result = web_scrape('https://en.wikipedia.org/wiki/List_of_career_achievements_by_Michael_Jordan')
        print(result)
