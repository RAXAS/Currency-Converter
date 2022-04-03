import telebot
from script import TOKEN
from extensions import ConversionException, ValueConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Введите буквенные коды валют, которые хотите конвертировать в формате: <имя валюты, цену которой вы хотите узнать>, <имя валюты в которой надо узнать цену первой валюты>, <колличество первой валюты>. Например: usd rub 100')
    bot.register_next_step_handler(sent)

@bot.message_handler(commands=['values'])
def values(message):
    available_values = bot.send_message(message.chat.id, 'Доступны все буквенные коды валют, криптовалют, DeFi и NFT')
    bot.register_next_step_handler(available_values, сonverter)

@bot.message_handler()
def сonverter(message):

    try:
        quote, base, amount = message.text.split(" ")
    except ValueError:
        raise ConversionException("Введено неверное колличество параметров")

    total_base = ValueConverter.convert(quote, base, amount)
    #response = json.loads(requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}").text)

    bot.send_message(message.chat.id, f'{amount} {quote} = {c} {base}   {total_base}')

bot.polling()
