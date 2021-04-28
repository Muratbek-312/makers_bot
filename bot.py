import telebot
from decouple import config
from keyboards.inline_keyboard import inline_key as in_kye
bot = telebot.TeleBot(config('TOKEN'))


@bot.message_handler(commands=['start', ])
def welcome(message):
    msg = bot.send_message(message.chat.id, 'Hello Guest', reply_markup=in_kye)
    bot.register_next_step_handler(msg, send_nik)


def send_nik(message):
    msg = bot.send_message(message.chat.id, 'Введите ваш ник нейм: ')
    bot.register_next_step_handler(msg, send_age)


def send_age(message):
    bot.send_message(message.chat.id, "Введите ваш возраст: ")


bot.polling(none_stop=True)