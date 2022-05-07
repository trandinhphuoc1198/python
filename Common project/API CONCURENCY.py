from requests import get
from pprint import PrettyPrinter
printer=PrettyPrinter()
API="0d009b2dd43cc7f130dd"
url="https://free.currconv.com"
currencies="/api/v7/currencies?apiKey="+API
def get_currencies():
    listCurrencies=list(get(url+currencies).json()['results'].items())
    listCurrencies.sort()
    for currency in listCurrencies:
        currencyName=currency[1]['currencyName']
      
        symbol=currency[1].get('currentSymbol','None')
        print(f'currency: {currency[0]} | currencyName: {currencyName} | Symbol: {symbol}')
        
    