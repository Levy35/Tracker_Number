import phonenumbers 
import opencage 
import folium 
from myphone import number 

from phonenumbers import geocoder
#country name 
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print (location)

# Service provider 
from phonenumbers import carrier 
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode 

key ='32ae2ed95b73467c880339ba79a3d8c8'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0] ['geometry'] ['lat']
lng = results[0] ['geometry'] ['lng']
print(lat,lng)

myMap =folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)

myMap.save("mylocation.html")
