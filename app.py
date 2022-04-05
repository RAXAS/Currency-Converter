import telebot
from script import TOKEN, keys
from extensions import ConversionException, ValueConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    text = 'Введите буквенные коды валют, которые хотите конвертировать в формате: <имя валюты, цену которой вы хотите узнать>, <имя валюты в которой надо узнать>, <колличество первой валюты>. Например: доллар рубль 100'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        input_values = message.text.split(" ")
        if len(input_values) != 3:
            raise ConversionException('Введите команду или 3 параметра')

        quote, base, amount = input_values
        total_base = ValueConverter.get_price(quote, base, amount)

    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так с {e}')
    else:
        bot.reply_to(message, f'{amount} {quote} = {total_base} {base}')


bot.polling()


bot.polling()
