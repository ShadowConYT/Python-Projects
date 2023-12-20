import urllib
import requests

from dotenv import load_dotenv
load_dotenv()

import os
api_key = os.getenv('API_KEY')
base_url = 'https://cutt.ly/api/api.php'

def shorten_url(long_url: str):
    payload = {'key': api_key, 'short': long_url}
    request = requests.get(base_url, params=payload)
    data: dict = request.json()
    
    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print(f'Link: {short_link}')
        else:
            print(f'Error: {url_data["status"]}')

def main():
    input_link: str = input("enter a Link to shorten: \n")
    shorten_url(input_link)

if __name__ == '__main__':
    main()