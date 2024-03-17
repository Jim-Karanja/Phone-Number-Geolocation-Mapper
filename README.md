# Phone-Number-Geolocation-Mapper
This Python script utilizes the OpenCage Geocoder and Phonenumbers libraries to map the geographical location of a phone number and display it on a Folium map.

# Features
Phone Number Geolocation: Determines the geographical location of a phone number using the Phonenumbers library.
Service Provider Identification: Identifies the service provider associated with the phone number.
Map Visualization: Displays the location of the phone number on an interactive Folium map.
Customizable Geocoding Service: Utilizes the OpenCage Geocoder service, allowing for customization and configuration with your own API key.
# Prerequisites
Python 3.x
OpenCage Geocoder API key
Phonenumbers library
Folium library
Installation
Install the required libraries:

# Copy code
pip install phonenumbers folium
Sign up for an account at OpenCage Geocoder to obtain an API key.

# Usage
Import the necessary modules in your Python script:

# python
Copy code
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder
import phonenumbers
import folium
Replace "geocoder key" with your OpenCage Geocoder API key.

Customize the number variable with the phone number you want to geolocate.

# Run the script:

# Copy code
python geolocation_mapper.py
The script will output the location and service provider of the phone number and generate an HTML file (my_location.html) containing an interactive map with the location marker.
