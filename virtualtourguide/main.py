from utils import get_country, get_days
from tour_guide_crew import TourGuideCrew
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %message)s')
logger = logging.getLogger(__name__)

def main():
        
        logger.info(" Hi! I'm your Virtual Tour Guide! ")
        logger.info(' ------------------------------ ')

        # define parameters 
        country = get_country()
        days = get_days()

        tour_guide_crew = TourGuideCrew(country, days )

        result = tour_guide_crew.run()

        logger.info(' Here is your guide. Have an amazing vacation!')
        logger.info(result)

if __name__ == "__main__":
        main()
 