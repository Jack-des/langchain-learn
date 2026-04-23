from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from research_summary.tools.llm_models import get_llm
from research_summary.tools.prompts import ASSISTANT_SELECTION_PROMPT_TEMPLATE
from research_summary.utils.utils import json_to_object

assistant_instructions_chain = (
        {'user_question': RunnablePassthrough()}
        | ASSISTANT_SELECTION_PROMPT_TEMPLATE
        | get_llm() | StrOutputParser() | json_to_object
)
if __name__ == '__main__':
    assistant_instructions = assistant_instructions_chain.invoke(
        {'user_question': 'What can I see and do in the Spanish town of Astorga?'})
    print(assistant_instructions)
