# script to get weather report

import requests
import json
import os
from dotenv import load_dotenv
import configparser


def check_config_file():
    """ Checks if current file exists or not"""
    path = os.path.join('.', '.weather-config')
    return os.path.isfile(path)

def create_config_file(city):
    """Creates a config file"""
    path = os.path.join('.', '.weather-config')
    with open(path, "w") as f:
        ret = configparser.ConfigParser()
        ret.add_section("default")
        ret.set("default", "city", city)
        ret.write(f)


def read_config_file():
    """Read a config file and return the config parser object"""
    path = os.path.join('.', '.weather-config')
    config = configparser.ConfigParser()
    config.read(path)
    return config

def create_api(api_key, city):
    """returns the api with parameters filled in"""
    api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api_key)
    return api

def get_current_weather(api_key, city=None):
    """Function to get current weather"""

    response = None

    if not api_key:
        raise Exception('ERROR: get_current_weather(): API key is missing')
    
    if not city:
        # get current location
        config = read_config_file()
        default_city = config['default']['city']
        api = create_api(api_key, default_city)
        response = requests.get(api)

        if response.status_code == 404:
            raise Exception('URL not found\nPlease check your default city name or api key')
    else:

        api = create_api(api_key, city)
        response = requests.get(api)
        # condition to handle failure of requests.
        if response.status_code == 404:
            raise Exception('URL not found\nPlease insert correct city name or api key')

    weather_data = response.json()
    return weather_data


if __name__=="__main__":
    load_dotenv()
    api_key = os.getenv('WEATHER_API')

    # check if config file exist
    existence = check_config_file()

    if not existence:
        while True:
            city = input('Enter default city (current permanent location): ')
            if city: break
        create_config_file(city)

    city = input('Enter city:')
    weather_data = get_current_weather(api_key, city)
    # temperature converted to celsius
    avg_temp = weather_data['main']['temp']
    avg_temp = avg_temp - 273.15
    min_temp = weather_data['main']['temp_min'] - 273.15
    max_temp = weather_data['main']['temp_max'] - 273.15

    print("{} TEMPERATURE STATS\n".format(city.upper()))
    # temperature rounded to 2 decimal places.
    print('Average Temperature: {} celsius'.format(round(avg_temp, 2)))
    print('Maximum Temperature: {} celsius'.format(round(max_temp, 2)))
    print('Minimum Temperature: {} celsius'.format(round(min_temp, 2)))