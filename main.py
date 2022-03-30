import telebot
import requests
import json

TOKEN = "5216680764:AAFpQ4yUAtdqPMkq58PUmJiYP5YnE5ld0f0"
bot = telebot.TeleBot(TOKEN)

value1, value2 = input("Введите USD или EUR\n"), input("Введите USD или EUR\n")

response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={value1}&tsyms={value2}")
response.text
print(response.text)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

bot.polling()
