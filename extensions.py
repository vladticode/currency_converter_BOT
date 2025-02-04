import requests
import json
from config import apiKEY

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')
        
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')
        
        r = requests.get(f'https://v6.exchangerate-api.com/v6/{apiKEY}/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate']

        return total_base