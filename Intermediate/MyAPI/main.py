from flask import Flask, request
from random import randint, choice, sample
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    with open('quotes.json', 'r') as quote:
        quotes = json.load(quote)
        rand_quote = choice(quotes)

    return f'Date: {datetime.now()}, Quote: {rand_quote}'


@app.route('/api/v1/kural')
def kural():
    num = request.args.get('number', type=int, default = 1)
    with open('thirukural.json', 'r', encoding='utf-8') as kural:
        kurals = json.load(kural)
        rand_kural = sample(kurals['kural'], num)
    
    return f"""Date: {datetime.now()}, 
                Kural: {rand_kural}"""

if __name__ == '__main__':
    app.run()


