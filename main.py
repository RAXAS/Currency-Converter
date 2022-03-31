import telebot
import requests
import json

TOKEN = "5216680764:AAFpQ4yUAtdqPMkq58PUmJiYP5YnE5ld0f0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Введите валюты, которые хотите конвертировать в формате: первая валюта, вторая валюта, колличество первой валюты')
    bot.register_next_step_handler(sent, сonverter)

def сonverter(message):
    elements = message.text
    elements = list(elements.split(" "))
    #elements = elements.text
    response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={elements[0]}&tsyms={elements[1]}")
    a = json.loads(response.text)
    b = list(a.values())
    c = float(elements[2]) * float(b[0])
    bot.send_message(message.chat.id, f'Ответ {c}')

bot.polling()
