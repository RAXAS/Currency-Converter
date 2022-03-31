import telebot
import requests
import json

TOKEN = "5216680764:AAFpQ4yUAtdqPMkq58PUmJiYP5YnE5ld0f0"
bot = telebot.TeleBot(TOKEN)


elements = list(input("Введите значения через пробел:\n").split())

print(elements[0])
response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={elements[0]}&tsyms={elements[1]}")

a = json.loads(response.text)
b = list(a.values())
c = float(elements[2]) * float(b[0])
print(c)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Введите валюты, которые хотите конвертировать в формате: первая валюта, вторая валюта, колличество первой валюты')
    bot.register_next_step_handler(sent, сonverter)

def сonverter(message):
    message = list(input("Введите числа через пробел:\n").split())
    сurrency_one = message[0]
    сurrency_two = message[1]
    value = message[2]
    сurrency_final = value * 1
    bot.send_message(message.chat.id, 'Привет, {elements}. Рад тебя видеть.'.format(elements=list(input().split()).text))

bot.polling()
