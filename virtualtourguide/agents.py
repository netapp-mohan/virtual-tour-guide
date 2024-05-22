import os
from textwrap import dedent

from crewai import Agent
from langchain_community.llms import Ollama
#from tools.browser_tools import BrowserTools
#from tools.search_tools import SearchTools
from langchain_community.tools import DuckDuckGoSearchRun
ollama = Ollama(model = 'mistral', temperature = 0.4)
search_tool = DuckDuckGoSearchRun()

class TourGuideAgent():

    def country_agent(self):
        return Agent(
            role = 'Seasoned traveller with extensive knowledge of the country',
            goal = "Given the country, provide general info about the country, including dos and donts, \
                    tips on navigating the country and how the experience can be better",
            backstory = 'You have travelled to this country in the past. You also have friends who have travelled here. \
                         Based on their experiences and your own experience, suggest pointers so as to make this trip smooth',
            tools = [search_tool],
            llm=ollama,
            verbose = True
        )
    
    def itinerary_agent(self):
        return Agent(
            role = 'Expert itinerary maker with strong background in planning vacations',
            goal = "Craft an itinerary based on the number of days input by the user. \
                    The itinerary should be well balanced with enough time to see major attractions and also rest well in between.",
            backstory = 'You are a balanced traveller who prioritizes seeing attractions and resting well equally. \
                         You are not exhausted by the end of the trip, at the same time, you are not slacking and make sure to visit the important places',
            tools = [search_tool],
            llm=ollama,
            verbose = True
        )
    
    def transport_agent(self):
        return Agent(
            role = 'Expert knowledge in getting around the country making efficient use of transportation.',
            goal = "Given the itinerary, suggest the most efficient form of transportation for the trip. \
                    It should be cost-efficient and convenient. Do not compromise on either.",
            backstory = 'Having travelled extensively across the country, you are well-versed with getting around. \
                         You know the best (time and cost effective) way of getting around!',
            tools = [search_tool],
            llm=ollama,
            verbose = True
        )
    
    def food_culture_agent(self):
        return Agent(
            role = 'Expert knowledge of local cuisine and culture of the country.',
            goal = "Suggest a list of local delicacies and most popular restaurants/cafes that serve authentic local cuisine. \
                    Also suggest a list of cultural specialities of the country that one should experience",
            backstory = 'You have a great taste for local food and culture. In your previous trips, \
                         you have had authentic experiences with respect to food and culture.',
            tools = [search_tool],
            llm=ollama,
            verbose = True
        )