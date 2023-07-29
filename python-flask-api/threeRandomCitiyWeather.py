
from flask import Flask
import urllib.request, json
from decouple import config
from typing import List
import random
from threeCityGetWeather import getWeatherOfThreeCities

def getWeatherOfThreeRandomCities() -> dict:
    list_of_locations = [
        ("Paris", "Paris", "FR"),
        ("London", "England", "GB"),
        ("Berlin", "Berlin", "DE"),
        ("Cardiff", "Wales", "GB"),
        ("Edinburgh", "Scotland", "GB"),
        ("Copenhagen", "Copenhagen", "DK"),
        ("Helsinki", "Helsinki", "NO"),
        ("Sydney", "Sydney", "FR"),
    ]      
    random_3_cities = [random.choice(list_of_locations) for i in range(3)]
    print(random_3_cities)
    if random_3_cities:
        return getWeatherOfThreeCities(cities=random_3_cities)
    else: 
        raise IndexError("No random cities selected")
    