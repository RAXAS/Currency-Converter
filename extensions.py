import requests
import json


class ConversionException(Exception):
    pass


class ValueConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException("Невозможно перевести одинаковые валюты")

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Не удалось обработать колличество {amount}")

        response = json.loads(requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}").text)
        b = ValueConverter(list(response.values()))
        c = float(amount) * float(b[0])
