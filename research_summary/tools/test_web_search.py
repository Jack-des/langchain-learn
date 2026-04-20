from unittest import TestCase

from research_summary.tools.web_search import web_search


class Test(TestCase):
    def test_web_search(self):
        result = web_search(
            web_query="How many titles did Michael Jordan win?",
            num_results=5)
        print(result)
