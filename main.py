from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import phonenumbers
import opencage
import folium

from phone_number import number
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

key = "geocoder key"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)
my_map.save("my location.html")
