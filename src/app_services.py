import requests
import os

# Config API
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_key = os.getenv('OPEN_WEATHER_API_KEY')

# Constants
zero_kelvin = 273.15
city_index = 0
country_index = 1
temp_index = 2
icon_index = 3
weather_index = 4


def get_city_weather(city):
    """
    Gets the weather in the given city, using the Open Weather API
    :param city: city name
    :return: tuple with the weather information or None
    """
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        # Getting the info that we want {City, Country, Temperatures, Icon, Weather Description}
        # Location
        city = json["name"]
        country = json["sys"]["country"]

        # Temperature
        temp_kelvin = json["main"]["temp"]
        temp_celsius = round(temp_kelvin - zero_kelvin, 2)  # Converting kelvin to celsius
        min_temp_celsius = round(json["main"]["temp_min"] - zero_kelvin, 2)
        max_temp_celsius = round(json["main"]["temp_max"] - zero_kelvin, 2)

        # Weather description and icon
        icon = json["weather"][0]["icon"]
        weather_desc = json["weather"][0]["description"]

        return city, country, temp_celsius, icon, weather_desc, min_temp_celsius, max_temp_celsius
    else:
        return None
