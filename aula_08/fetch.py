from requests import Session
from requests.exceptions import ConnectionError,Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
from pprint import pprint 


load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'symbol': 'BTC',
    'convert': 'BRL'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY') # AQUI OBTÉM A CHAVE DO .ENV
}

session = Session()
session.headers.update(headers)

response = session.get(url=url, params=parameters)

data = json.loads(response.text)

bitcoin_data = data['data']['BTC']
brl_quote = bitcoin_data['quote']['BRL']

pprint(brl_quote)
pprint(brl_quote['price'])
pprint(brl_quote['last_updated'])
pprint(brl_quote['volume_24h'])
pprint(brl_quote['market_cap'])


