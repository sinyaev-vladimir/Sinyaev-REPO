import telebot
from config import keys, TOKEN                              # перенос переменных keys, TOKEN из файла Config
from extensions import CryptoConverter, ConversionException      # перенос классов из файла Utils

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    text = 'Для начала работы введите команду в след. формате:\n<имя валюты> \ <в какую валюту перевести> \ <кол-во переводимой валюты>\nпосмотреть список доступных валют - /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)     # .chat.id необх писать при send_message и можно не писать при reply_to

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Проверьте количество введенных параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена {amount} {quote}(ов) : {total_base * float(amount)} {base}(ов)'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)