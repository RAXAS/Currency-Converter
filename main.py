import telebot
import requests
import json

TOKEN = "5216680764:AAFpQ4yUAtdqPMkq58PUmJiYP5YnE5ld0f0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Введите буквенные коды валют, которые хотите конвертировать в формате: <имя валюты, цену которой вы хотите узнать>, <имя валюты в которой надо узнать цену первой валюты>, <колличество первой валюты>. Например: usd rub 100')
    bot.register_next_step_handler(sent)

@bot.message_handler(commands=['values'])
def values(message):
    available_values = bot.send_message(message.chat.id, 'Доступны все буквенные коды валют криптовалют, DeFi и NFT')
    bot.register_next_step_handler(available_values, сonverter)
@bot.message_handler()
def сonverter(message):
    elements = message.text
    elements = list(elements.split(" "))
    response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={elements[0]}&tsyms={elements[1]}")
    a = json.loads(response.text)
    b = list(a.values())
    c = float(elements[2]) * float(b[0])
    bot.send_message(message.chat.id, f'{elements[2]} {elements[0]} = {c} {elements[1]}')

bot.polling()
