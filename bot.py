import telebot
from decouple import config
from keyboards.inline_keyboard import inline_key as in_kye
bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start', ])
def welcome(message):
    bot.send_message(message.chat.id, 'Hello Guest', reply_markup=in_kye)

bot.polling(none_stop=True)