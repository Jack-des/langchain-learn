import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from research_summary.lcel_02 import assistant_instructions_chain
from research_summary.lcel_03 import web_searches_chain
from research_summary.lcel_04 import search_result_urls_chain
from research_summary.lcel_05 import search_result_text_and_summary_chain
from research_summary.tools.llm_models import get_llm
from research_summary.tools.prompts import RESEARCH_REPORT_PROMPT_TEMPLATE

search_and_summarization_chain = (
        search_result_urls_chain
        | search_result_text_and_summary_chain.map()  # parallelize for each url
        | RunnableLambda(lambda x:
                         {
                             'summary': '\n'.join([i['summary'] for i in x]),
                             'user_question': x[0]['user_question'] if len(x) > 0 else ''
                         })
)

web_research_chain = (
        assistant_instructions_chain
        | web_searches_chain
        | search_and_summarization_chain.map()  # parallelize for each web search
        | RunnableLambda(lambda x:
                         {
                             'research_summary': '\n\n'.join([i['summary'] for i in x]),
                             'user_question': x[0]['user_question'] if len(x) > 0 else ''
                         })
        | RESEARCH_REPORT_PROMPT_TEMPLATE | get_llm() | StrOutputParser()
)
os.environ["HTTP_PROXY"] = "http://192.168.2.21:7890"
os.environ["HTTPS_PROXY"] = "http://192.168.2.21:7890"
question = 'What can I see and do in the Spanish town of Astorga?'

web_research_report = web_research_chain.invoke(question)
print(web_research_report)
