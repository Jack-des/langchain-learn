from unittest import TestCase

from research_summary.tools.llm_models import get_llm


class Test(TestCase):
    def test_get_llm(self):
        llm = get_llm()
        response = llm.invoke("1+1=?")
        print(response.content)
