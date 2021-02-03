# script to get weather report

import requests
import json
import os
from dotenv import load_dotenv

def get_current_weather(api_key, city=None):
    """Function to get current weather"""

    if not api_key:
        raise Exception('ERROR: get_current_weather(): API key is missing')
    
    if not city:
        # current location
        pass
    else:
        api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api_key)
        response = requests.get(api)
        weather_data = response.json()
        return weather_data


if __name__=="__main__":
    load_dotenv()
    api_key = os.getenv('WEATHER_API')

    city = "Kolkata"
    weather_data = get_current_weather(api_key, city)
    # temperature converted to celsius
    avg_temp = weather_data['main']['temp']
    avg_temp = avg_temp - 273.15
    min_temp = weather_data['main']['temp_min'] - 273.15
    max_temp = weather_data['main']['temp_max'] - 273.15

    print("{} TEMPERATURE STATS\n".format(city.upper()))
    print('Average Temperature: {}'.format(avg_temp))
    print('Maximum Temperature: {}'.format(max_temp))
    print('Minimum Temperature: {}'.format(min_temp))