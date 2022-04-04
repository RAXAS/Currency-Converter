import telebot
import requests
import json
from script import TOKEN, keys
from extensions import ConversionException, ValueConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Введите буквенные коды валют, которые хотите конвертировать в формате: <имя валюты, цену которой вы хотите узнать>, <имя валюты в которой надо узнать цену первой валюты>, <колличество первой валюты>. Например: usd rub 100')
    bot.register_next_step_handler(sent)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        quote, base, amount = message.text.split(" ")
    except ValueError:
        raise ConversionException("Введено неверное колличество параметров")


    #response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
    #a = json.loads(response.text)
    #b = list(a.values())
    #c = float(amount) * float(b[0])
    #total_base = ValueConverter.get_price(quote, base, amount)
    bot.send_message(message.chat.id, f'{amount} {quote} = {base}')

bot.polling()
