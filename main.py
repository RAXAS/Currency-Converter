import telebot
import requests

TOKEN = "5216680764:AAFpQ4yUAtdqPMkq58PUmJiYP5YnE5ld0f0"
value1 = input("Введите USD или EUR")
value2 = input("Введите USD или EUR")
response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={value1}&tsyms={value2}")
response.text
print(response.text)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

bot.polling()
