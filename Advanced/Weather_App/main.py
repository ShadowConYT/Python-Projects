from dotenv import load_dotenv
import requests
import os

load_dotenv()


API_KEY = os.environ.get('WEATHER_API_KEY')
BASE_URL = 'https://pro.openweathermap.org/data/2.5/forecast'


def get_weather(city):
    params: dict = {
        'lat': city['lat'],
        'lon': city['lon'],
        'appid': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 401:
        return 'Unauthorized', response.json()
    
    return response.json()

def main():
    city = {
        'lat': 35.6895,
        'lon': 139.6917
    }
    weather = get_weather(city)
    print(weather)

if __name__ == '__main__':
    main()
