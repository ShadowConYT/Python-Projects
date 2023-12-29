from flask import Flask
from random import randint, choice
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    with open('quotes.json', 'r') as quote:
        quotes = json.load(quote)
        quote = choice(quotes)

    return f'Date: {datetime.now()}, \n Quote: {quote}'

if __name__ == '__main__':
    app.run()
