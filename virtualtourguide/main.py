from utils import get_country, get_days
from tour_guide_crew import TourGuideCrew

def main():
        
        print(" Hi! I'm your Virtual Tour Guide! ")
        print(' ------------------------------ ')

        # define parameters 
        country = get_country()
        days = get_days()

        tour_guide_crew = TourGuideCrew(country, days )

        result = tour_guide_crew.run()

        print(' Here is your guide. Have an amazing vacation!')
        print(result)

if __name__ == "__main__":
        main()
 