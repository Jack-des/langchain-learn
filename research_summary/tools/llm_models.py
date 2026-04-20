from langchain_ollama import ChatOllama

llm = ChatOllama(model="gpt-oss:120b-cloud", temperature=0)


def get_llm():
    return llm
