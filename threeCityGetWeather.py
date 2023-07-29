
from flask import Flask
import urllib.request, json
from decouple import config

threeCities = [
    ("London", "England", "GB"),
    ("New_York_City", "New_York", "US"),
    ("Tokyo", "Tokyo", "JP")
]



openweather_apiKey = config("openweathermap")
geoCodingBaseURL = "http://api.openweathermap.org/geo/1.0/direct?q="

city_coords = {}

for city in threeCities:
    getURL = geoCodingBaseURL + city[0] + "," + city[1] + "," +  city[2] + "&limit=1&appid=" + openweather_apiKey
    response = urllib.request.urlopen(getURL)
    data = response.read()
    dictionary_result = json.loads(data)
    # print(f'lattitude: {dictionary_result[0]["lat"]} longitude: {dictionary_result[0]["lon"]}')
    city_coords[city[0]] = (dictionary_result[0]["lat"], dictionary_result[0]["lon"])


weatherHourlyForecastBaseUrl = "http://api.openweathermap.org/data/2.5/forecast?"

city_temps = {}

for city in threeCities:
    cityCoordinate = city_coords[city[0]]
    getURL = weatherHourlyForecastBaseUrl + "lat=" + str(cityCoordinate[0]) + "&lon=" + str(cityCoordinate[1]) + "&appid=" + openweather_apiKey + "&cnt=8&units=metric"
    response = urllib.request.urlopen(getURL)
    data = response.read()
    dictionary_result = json.loads(data)
    city_temps[city[0]] = dictionary_result["list"][-1]["main"]["temp"]

print("The temperature forecasts of the 3 cities tomorrow are:")
print(str(city_temps))

