import telebot
import requests
import json

TOKEN = "5216680764:AAFpQ4yUAtdqPMkq58PUmJiYP5YnE5ld0f0"
bot = telebot.TeleBot(TOKEN)


elements = list(input("Введите числа через пробел:\n").split())

print(elements[0])
response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={elements[0]}&tsyms={elements[1]}")
response.text
print(response.text)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Введите валюты, которые хотите конвертировать в формате: первая валюта, вторая валюта, колличество первой валюты')
    bot.register_next_step_handler(sent, сonverter)

def сonverter(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

bot.polling()
