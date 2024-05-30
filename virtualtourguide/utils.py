import logging 
from fuzzywuzzy import process
import pycountry

logger = logging.getLogger(__name__)

def get_country():

    countries = [country.name for country in pycountry.countries]
    while True:
        try:
            country = input("Please enter the country you'd like to visit: ")
            assert isinstance(country, str), 'Country must be a string.'

            # Use fuzzy matching to suggest the closest country name
            closest_match, match_score = process.extractOne(country, countries)
            if match_score > 60:
                suggestion = input(f'Did you mean {closest_match}? (Yes/No): ').strip().lower()
                if suggestion == 'yes':
                    return closest_match
            else:
                logger.info('Country not recognized! Please try again.')
        except AssertionError as e:
            logger.error(e)
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")

def get_days():
    while True:
        try:
            days = input("Please enter the number of days for your trip: ")
            days = int(days)
            assert days > 0, "Number of days must be a positive integer."
            return days 
        except ValueError:
            logger.info('Invalid input. Please enter a valid integer for the number of days.')
        except AssertionError as e:
            logger.info(e)