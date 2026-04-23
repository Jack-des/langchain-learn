import logging
import random
import time

from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List

import os

logging.basicConfig(
    level=logging.INFO,  # Set the lowest level to capture
    format='%(asctime)s - %(levelname)s - %(message)s'  # Define the output look
)


def web_search(web_query: str, num_results: int) -> List[str]:
    logging.info(f"web_search of {web_query} with {num_results} results")
    os.environ["DDGS_PROXY"] = "http://192.168.2.21:7890"
    delay = random.uniform(0, 3)
    time.sleep(delay)
    results = DuckDuckGoSearchAPIWrapper().results(web_query, num_results)

    result_links = [r["link"] for r in results]
    logging.info(f"get result links from ddgs")
    return result_links


if __name__ == '__main__':
    result = web_search(
        web_query="How many titles did Michael Jordan win?",
        num_results=5)
    print(result)
