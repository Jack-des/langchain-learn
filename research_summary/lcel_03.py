from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from research_summary.tools.llm_models import get_llm
from research_summary.tools.prompts import WEB_SEARCH_PROMPT_TEMPLATE
from research_summary.utils.utils import json_to_object

NUM_SEARCH_QUERIES = 2

web_searches_chain = (
        RunnableLambda(lambda x:
                       {
                           'assistant_instructions': x['assistant_instructions'],
                           'num_search_queries': NUM_SEARCH_QUERIES,
                           'user_question': x['user_question']
                       }
                       )
        | WEB_SEARCH_PROMPT_TEMPLATE
        | get_llm() | StrOutputParser() | json_to_object
)

if __name__ == '__main__':
    assistant_instruction_str = '{"assistant_type": "Tour guide assistant", "assistant_instructions": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights.", "user_question": "What can I see and do in the Spanish town of Astorga?"}'
    assistant_instruction_dict = json_to_object(assistant_instruction_str)
    web_searches_list = web_searches_chain.invoke(assistant_instruction_dict)
    print(web_searches_list)
