import json
from flask import Flask, jsonify, request
from threeCityGetWeather import getWeatherOfThreeCities
from threeRandomCitiyWeather import getWeatherOfThreeRandomCities
from urllib.error import URLError
from typing import List


app = Flask(__name__)

@app.route('/getThreeMainCitiesTemp', methods= ['GET'])
def get_temp_3_main_cities():
    main_cities = [
        ("London", "England", "GB"),
        ("New_York_City", "New_York", "US"),
        ("Tokyo", "Tokyo", "JP"),
    ]

    try:
        city_temps = getWeatherOfThreeCities(cities=main_cities)
        return jsonify(city_temps)
    except AssertionError:
        return jsonify({ 'error': 'Input error. Please ensure cities input is three tuples of form: (City_name, State_name, Country_code)'}), 400
    except URLError:
        return jsonify({'error': "Unorthorised, please check request"}), 401
    

@app.route('/getThreeRandomCitiesTemp', methods= ['GET'])
def get_temp_3_random_cities():

    try:
        city_temps = getWeatherOfThreeRandomCities()
        return jsonify(city_temps)
    except AssertionError:
        return jsonify({ 'error': 'Input error. Please ensure cities input is three tuples of form: (City_name, State_name, Country_code)'}), 400
    except URLError:
        return jsonify({'error': "Unorthorised, please check request"}), 401
    
@app.route('/getSelectedThreeCitiesTemp/', methods= ['GET'])
def get_temp_3_selected_cities():
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
        "Slovenia": ("Ljubljana", "Ljubljana", "SI"),
        "Moscow": ("Moscow", "Moscow", "RU")
    }  

    selectedCities = request.args.getlist('city')
    # return jsonify([capital_city_list.get(city, None) for city in selectedCities])

    if len(list(set(selectedCities))) != 3:
        return jsonify({"error": "You must input 3 unique Cities"}), 400
    if not all ([city in capital_city_list.keys() for city in selectedCities]):
        return jsonify({"error": "Each city must be in the selected list of European capitals"}), 400


    try:
        selecteddCityity_temps = getWeatherOfThreeCities(cities=[capital_city_list.get(city, None) for city in selectedCities])
        return jsonify(selecteddCityity_temps)
    except AssertionError:
        return jsonify({ 'error': 'Input error. Please ensure cities input is three tuples of form: (City_name, State_name, Country_code)'}), 400
    except URLError:
        return jsonify({'error': "Unorthorised, please check request"}), 401
    

if __name__ == '__main__':
   app.run(port=5000, debug=True)

    
