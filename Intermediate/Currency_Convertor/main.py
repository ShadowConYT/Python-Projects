import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"

def get_currency_list(mock = False) -> list:
    if mock:
        with open('currency.json', 'r') as file:
            data = json.load(file)
    
    payload = {'access_key': API_KEY}
    url = requests.get(url=BASE_URL)
    data = url.json()

    with open('currency.json', 'w') as file:
        json.dump(data, file)

    return data

def get_currency(currency: str, rate: dict) -> float:
    currency = currency.upper()
    if currency in rate.keys():
        return rate.get(currency)
    else:
        raise ValueError(f"{currency} is not a valid currency")

def convert_currency(amount, base_curr, vs_curr, rate):
    base_rate = get_currency(base_curr, rate)
    vs_rate = get_currency(vs_curr, rate)

    conversion = round((vs_rate/base_rate) * amount, 2)
    print(f"{amount:,.2f} ({base_curr.upper()}) is, {conversion:,.2f} ({vs_curr.upper()})")
    return conversion

def main():
    currency_list = get_currency_list()
    currency_rate = currency_list.get('rates')

    amount = float(input("Enter amount to convert: "))
    base_currency = input("Enter base currency: ")
    vs_currency = input("Enter currency to convert to: ")

    convert_currency(amount, base_currency, vs_currency, currency_rate)    

if __name__ == "__main__":
    main()