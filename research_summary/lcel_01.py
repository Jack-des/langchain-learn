from research_summary.tools.llm_models import get_llm
from research_summary.tools.prompts import ASSISTANT_SELECTION_PROMPT_TEMPLATE

question = 'What can I see and do in the Spanish town of Astorga?'
assistant_instructions_chain = (
        ASSISTANT_SELECTION_PROMPT_TEMPLATE | get_llm()
)

if __name__ == '__main__':
    assistant_instruction = assistant_instructions_chain.invoke(question)
    print(assistant_instruction)
