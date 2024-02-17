from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()


API_KEY = os.environ.get('WEATHER_API_KEY')
BASE_URL = 'https://api.weatherapi.com/v1/forecast.json'


def get_weather(city, mock: bool = False):
    if mock:
        with open('dummy.json') as file:
            return json.load(file)
            
    payload = { 'key': API_KEY, 'q': city, 'days': 1}
    request = requests.get(BASE_URL, params=payload)
    data: json = request.json()
    with open('dummy.json', 'w') as file:
        json.dump(data, file, indent=4)
    return data


def main():
    city = input('Enter the city: ')
    weather_report = get_weather(city)
    current = weather_report['current']
    forecast_weather = weather_report['forecast']['forecastday'][0]['day']['condition']['text']
    return f'The weather in {city} is {forecast_weather} with a temperature of {current["temp_c"]}°C'

if __name__ == '__main__':
   print(main())