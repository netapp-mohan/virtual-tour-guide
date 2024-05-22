from crewai import Task
from textwrap import dedent
from datetime import date

class TourGuideTasks():

    def gather_info_task(self, agent, country,days):
        return Task(description=dedent(f"""
            Return important information about the chosen country and provide informative suggestions and tips.
            These can include dos and donts, how to conduct oneselves in the country, follow rule of law,
            be wary of country's safety history (areas to avoid/general safety tips). 
            Also mention how one can optimize their trip, just give general pointers. Imagine if you were to go to 
            this country again, what pitfalls would you actively avoid, and what would you do differently?
            Country of interest: {country}"""),
            expected_output='A list of 10 concise bullet points, each covering different aspects of rich information about the country and valuable tips',
            async_execution=True,
            agent=agent  
        )
    
    def plan_task(self, agent, country,days):
        return Task(description=dedent(f"""
            Plan a detailed itinerary in country:{country} for {days} number of days. The itinerary must include a list of places to visit, cover major attractions,    
            numbers(distances/time taken) from one place to another. It should also include major tourist spots in every location/city.
            Plan the itinerary in such a way that it is well balanced. The visitor must be able to cover most places but it should not be overwhelmingly hectic.
            Allow enough time in between attractions to rest well. Also suggest things to do in the free time (during evenings)."""),
            expected_output= 'A detailed itinerary outlining major attractions/places to cover in the given number of days',
            agent=agent,
            )
                                       
    
    def research_task(self,agent,country,days):
        return Task(description=dedent(f"""
            Given the number of days in the country and the full itinerary, research and come up with the most efficient modes of 
            transportation across the country. If you have suggested places in the country that are distant from each other, figure out the best way to cover 
            these places within the given number of days. Your research should be thorough, accounting for transportation based on your own experience and experiences from 
            other travellers in the past. Also factor in cost, safety, reliability, and efficiency of these modes. Suggest ways to get around
            both within the city and between cities. 
            days: {days}
            country: {country} """),
            expected_output='Comprehensive note on types of public/private transportation available and when and how to take them',
            async_execution=True,
            #context=[self.plan_task],
            agent=agent)
    
    def review_task(self, agent, country,days):
        return Task(description=dedent(f""""
            List the most authentic dishes and cuisine to try out in country:{country}. Additionally, collect reviews from the best restaurants in each of the 
            places to visit and mention them. If there are cultural experiences that one should experience in the country, mention that too. """),
            expected_output='List of authentic dishes from the local cuisine, along with top restaurants in the area. Also list must-do cultural experiences.',
            #context = [self.plan_task],
            agent=agent)
    

                                       

                                