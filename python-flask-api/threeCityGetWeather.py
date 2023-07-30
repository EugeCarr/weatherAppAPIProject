
from flask import Flask
import urllib.request, json
from decouple import config
from typing import List




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
        try: 
            city_coords[city[0]] = (dictionary_result[0]["lat"], dictionary_result[0]["lon"])
        except IndexError:
            print(city[0])
            break


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


def selectThreecities():
    capital_city_list = {
        "Paris": ("Paris", "Paris", "FR"),
        "London": ("London", "England", "GB"),
        "Berlin": ("Berlin", "Berlin", "DE"),
        "Cardiff": ("Cardiff", "Wales", "GB"),
        "Edinburgh": ("Edinburgh", "Scotland", "GB"),
        "Copenhagen": ("Copenhagen", "Copenhagen", "DK"),
        "Madrid": ("Madrid", "Madrid", "ES"),
        "Amsterdam": ("Amsterdam", "Amsterdam", "NL"),
        "Oslo": ("Oslo", "Oslo", "NO"),
        "Helsinki": ("Helsinki", "Helsinki", "SE"),
        "Warsaw": ("Warsaw", "Warsaw", "PL"),
        "Lisbon": ("Lisbon", "Lisbon", "PT"),
        "Rome": ("Rome", "Rome", "IT"),
        "Slovenia": ("Ljubljana", "Ljubljana", "SI")
    }  

    selected_city_list = []

    for i in range(3):
        selectedCityValid = False
        while not selectedCityValid:
            city_name = str(input("Please choose a european city to get a forecast: "))
            if city_name in capital_city_list.keys() and city_name not in [city[0] for city in selected_city_list]:
                selected_city_list.append(capital_city_list[city_name])
                selectedCityValid = True
                print(f'{city_name} has been added successfully. Your chosen list of cities is: {[city[0] for city in selected_city_list]}')
            else:
                if city_name in [city[0] for city in selected_city_list]:
                    print(f'Sorry, {city_name}, was not in the list of cities we can forecast. Please try again.')
                else:       
                    print(f'Sorry, {city_name}, has already been selected. Please try again.')

    



if __name__ == '__main__':
   cities = selectThreecities()
   print(cities)