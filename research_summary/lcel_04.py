from langchain_core.runnables import RunnableLambda

from research_summary.tools.web_search import web_search
from research_summary.utils.utils import json_to_object

NUM_SEARCH_RESULTS_PER_QUERY = 3

search_result_urls_chain = (
    RunnableLambda(lambda x:
                   [
                       {
                           'result_url': url,
                           'search_query': x['search_query'],
                           'user_question': x['user_question']
                       }
                       for url in web_search(
                       web_query=x['search_query'],
                       num_results=NUM_SEARCH_RESULTS_PER_QUERY)
                   ]
                   )
)
if __name__ == '__main__':
    web_search_str = '{"search_query": "Astorga Spain attractions", "user_question": "What can I see and do in the Spanish town of Astorga?"}'
    web_search_dict = json_to_object(web_search_str)
    result_urls_list = search_result_urls_chain.invoke(web_search_dict)
    print(result_urls_list)
