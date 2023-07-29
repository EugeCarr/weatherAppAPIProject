import json
from flask import Flask, jsonify, request
from threeCityGetWeather import getWeatherOfThreeCities
from threeRandomCitiyWeather import getWeatherOfThreeRandomCities
from urllib.error import URLError


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
    

if __name__ == '__main__':
   app.run(port=5000)
    
    
