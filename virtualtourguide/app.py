import streamlit as st 
from tour_guide_crew import TourGuideCrew
import pycountry
from fuzzywuzzy import process

def get_country_list():
    return [country.name for country in pycountry.countries]

def find_closest_country(country_name, countries):
    closest_match, match_score = process.extractOne(country_name, countries)
    return closest_match, match_score

def main():
    st.title("Virtual Tour Guide")

    # user input 
    countries = get_country_list()
    country = st.selectbox("Choose the country you would like to visit:", countries)
    days = st.number_input("Enter the number of days for your trip:", min_value=1, value=7, step=1)

    if st.button("Plan my trip!"):
        closest_country = find_closest_country(country, countries)
        if closest_country:
            country = closest_country
        
        tour_guide_crew = TourGuideCrew(country, days)

        try:
            result = tour_guide_crew.run()
            st.success("Here's your guide. Have an amazing vacation!")
            st.write(result)

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

