import requests
import json
from script import keys


class ConversionException(Exception):
    pass


class ValueConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Не удалось обработать колличество {amount}")
        
        if int(amount) < 0:
            raise ConversionException("Колличество валюты не может быть ниже нуля")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не смог обработать валюту {quote}')

        if quote == base:
            raise ConversionException("Невозможно перевести одинаковые валюты")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не смог обработать валюту {base}')

        
        response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = float(json.loads(response.content)[base_ticker]) * amount
        return total_base
