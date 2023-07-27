
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

get_responses_cities = []

for city in threeCities:
    getURL = geoCodingBaseURL + city[0] + "," + city[1] + "," +  city[2] + "&limit=1&appid=" + openweather_apiKey
    response = urllib.request.urlopen(getURL)
    data = response.read()
    dictionary_result = json.loads(data)
    print(f'lattitude: {dictionary_result[0]["lat"]} longitude: {dictionary_result[0]["lon"]}')
    get_responses_cities.append(dictionary_result)




