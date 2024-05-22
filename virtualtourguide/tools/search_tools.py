import json
import os

import requests
from langchain.tools import tool

class SearchTools():

    @tool("Search the Internet")
    def search_internet(query):
        """ Useful to search the Internet
            about a given topic and return relevant results"""
        
        top_result_to_return = 5
        url = 'https://google.serper.dev/search'
        payload = json.dumps({'q':query})
        headers = {
                    'X-API-KEY': os.environ['SERPER_API_KEY'],
                    'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        