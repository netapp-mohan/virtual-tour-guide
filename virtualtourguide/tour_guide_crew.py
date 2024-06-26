from crewai import Crew
from agents import TourGuideAgent
from tasks import TourGuideTasks
from textwrap import dedent
from utils import get_country, get_days
import logging


'''
from dotenv import load_dotenv
load_dotenv()
'''

# Define tasks and agents

class TourGuideCrew:

    def __init__(self, country, days):
        self.country = country
        self.days = days


    def run(self):
        tour_agent  = TourGuideAgent()
        tour_tasks = TourGuideTasks()

        # define agents and call them 

        c_agent = tour_agent.country_agent()
        i_agent = tour_agent.itinerary_agent()
        t_agent = tour_agent.transport_agent()
        f_agent = tour_agent.food_culture_agent()
        # define tasks and call them 

        gi_task = tour_tasks.gather_info_task(c_agent, self.country,self.days)
        pl_task = tour_tasks.plan_task(i_agent, self.country, self.days)
        res_task = tour_tasks.research_task(t_agent, self.country, self.days)
        rev_task = tour_tasks.review_task(f_agent, self.country,self.days)

        crew = Crew(
            agents = [c_agent, i_agent, t_agent, f_agent], 
            tasks = [gi_task, pl_task, res_task, rev_task],
            verbose = True
        )

        result = crew.kickoff()
        return result 