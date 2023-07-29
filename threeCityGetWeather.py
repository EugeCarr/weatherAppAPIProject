
from flask import Flask
import urllib.request, json
from decouple import config
from typing import List

threeCities = [
    ("London", "England", "GB"),
    ("New_York_City", "New_York", "US"),
    ("Tokyo", "Tokyo", "JP")
]


def getWeatherOfThreeCities(cities) -> dict:
    assert isinstance(cities, list), "Cities input must be a tuple"
    assert len(cities) == 3, "You must input 3 Cities"
    assert all([len(city) == 3 for city in cities]), "Each city tuple must be in form: (City_name, State_name, Country_code)"
    assert all( [type(l) == str for city in cities for l in city]), "Each part of the city tuple must be a string"


    openweather_apiKey = config("openweathermap")
    geoCodingBaseURL = "http://api.openweathermap.org/geo/1.0/direct?q="

    city_coords = {}

    for city in cities:
        getURL = geoCodingBaseURL + city[0] + "," + city[1] + "," +  city[2] + "&limit=1&appid=" + openweather_apiKey
        response = urllib.request.urlopen(getURL)
        data = response.read()
        dictionary_result = json.loads(data)
        # print(f'lattitude: {dictionary_result[0]["lat"]} longitude: {dictionary_result[0]["lon"]}')
        city_coords[city[0]] = (dictionary_result[0]["lat"], dictionary_result[0]["lon"])


    weatherHourlyForecastBaseUrl = "http://api.openweathermap.org/data/2.5/forecast?"

    city_temps = {}

    for city in cities:
        cityCoordinate = city_coords[city[0]]
        getURL = weatherHourlyForecastBaseUrl + "lat=" + str(cityCoordinate[0]) + "&lon=" + str(cityCoordinate[1]) + "&appid=" + openweather_apiKey + "&cnt=8&units=metric"
        response = urllib.request.urlopen(getURL)
        data = response.read()
        dictionary_result = json.loads(data)
        city_temps[city[0]] = dictionary_result["list"][-1]["main"]["temp"]

    return city_temps

test = getWeatherOfThreeCities(cities=threeCities)
print(str(test))