from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

from research_summary.tools.llm_models import get_llm
from research_summary.tools.prompts import SUMMARY_PROMPT_TEMPLATE
from research_summary.tools.web_scrap import web_scrape
from research_summary.utils.utils import json_to_object

RESULT_TEXT_MAX_CHARACTERS = 10000

search_result_text_and_summary_chain = (
        RunnableLambda(lambda x:
                       {
                           'search_result_text': web_scrape(url=x['result_url'])[:RESULT_TEXT_MAX_CHARACTERS],
                           'result_url': x['result_url'],
                           'search_query': x['search_query'],
                           'user_question': x['user_question']
                       }
                       )
        | RunnableParallel({
    'text_summary': SUMMARY_PROMPT_TEMPLATE | get_llm() | StrOutputParser(),
    'result_url': lambda x: x['result_url'],
    'user_question': lambda x: x['user_question']})
        | RunnableLambda(lambda x:
                         {
                             'summary': f"Source Url: {x['result_url']}\nSummary: {x['text_summary']}",
                             'user_question': x['user_question']
                         }
                         )
)

if __name__ == '__main__':
    result_url_str = '{"result_url": "https://citiesandattractions.com/spain/astorga-spain-uncovering-the-jewels-of-a-hidden-spanish-gem/", "search_query": "Astorga Spain attractions", "user_question": "What can I see and do in the Spanish town of Astorga?"}'
    result_url_dict = json_to_object(result_url_str)

    search_text_summary = search_result_text_and_summary_chain.invoke(result_url_dict)
    print(search_text_summary)
