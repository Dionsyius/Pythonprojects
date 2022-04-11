import phonenumbers
import folium
from numberlocate import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number)
YourLocation = (geocoder.description_for_number(ch_nmber, "en"))
print(YourLocation)
key = 'b4facbc256f243aab19ba93b6db10032'

from phonenumbers import carrier
service_nmber= phonenumbers.parse(number)
print(carrier.name_for_number(service_nmber, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(YourLocation)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat , lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng],popup=YourLocation).add_to((myMap))

#save to html file
myMap.save("myLocation.html")

from phonenumbers import timezone
timezone_nmber = phonenumbers.parse(number, "")
print(timezone.time_zones_for_number(timezone_nmber, ))







