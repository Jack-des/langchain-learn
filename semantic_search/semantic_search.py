import asyncio

from langchain_classic.schema import retriever
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_core.runnables import chain
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = "../example_data/TheLittlePrince.pdf"
loader = PyPDFLoader(file_path)

# pages of the PDF
docs:list = loader.load()

# print(len(docs))
# PyPDFLoader loads one Document object per PDF page.
# For each, we can easily access:
# print(f"{docs[10].page_content[:200]}\n")
# print(docs[10].metadata)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=100, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

# print(len(all_splits))


embeddings = OllamaEmbeddings(model="qwen3-embedding:4b")
# content = all_splits[20].page_content
# print(content)
# vector_1 = embeddings.embed_query(all_splits[20].page_content)
# vector_2 = embeddings.embed_query(all_splits[21].page_content)
#
# assert len(vector_1) == len(vector_2)
# print(f"Generated vectors of length {len(vector_1)}\n")
# print(vector_1[:10])

from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

# save
# ids = vector_store.add_documents(documents=all_splits)



# results = vector_store.similarity_search(
#     "does the little prince miss his rose?"
# )
#
# print(results[1])



# async def search_examples():
#     results = await vector_store.asimilarity_search(
#         "does the little prince miss his rose?"
#     )
#
#     print(results[1])
# asyncio.run(search_examples())



# Note that providers implement different scores; the score here
# is a distance metric that varies inversely with similarity.

# results = vector_store.similarity_search_with_score(
#     "Does the little prince miss his rose?"
# )
# doc, score = results[0]
# print(f"Score: {score}\n")
# print(doc)


# results = vector_store.similarity_search_by_vector(embeddings.embed_query("Does the little prince miss his rose?"))
# print(results[0])

# @chain
# def my_retriever(query:str) -> list[Document]:
#     return vector_store.similarity_search(query)
#

# my_retriever = vector_store.as_retriever()
# results = my_retriever.batch(
#     ["Dose the little prince miss his rose?",
#      "Who like count stars"]
# )
#
# print(results[0][0])
# print(results[1][0])