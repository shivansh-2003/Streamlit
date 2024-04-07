import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static


def main():
    st.title("Location Finder")

    # Get user input for location
    location_str = st.text_input("Enter a location:")

    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="location_finder")

    try:
        # Geocode the location string
        location = geolocator.geocode(location_str)

        if location:
            # Get latitude and longitude
            lat, lon = location.latitude, location.longitude

            # Create a Folium map centered around the geocoded location
            m = folium.Map(location=[lat, lon], zoom_start=12)

            # Add a marker for the geocoded location
            folium.Marker([lat, lon], popup=location.address).add_to(m)

            # Render Folium map using Streamlit
            folium_static(m)
        else:
            st.error("Location not found. Please enter a valid location.")
    except Exception as e:
        st.error("Error occurred while geocoding. Please try again.")


if __name__ == "__main__":
    main()
