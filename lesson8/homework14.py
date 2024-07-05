"""
Homework 14
"""
import random

import telebot
from telebot import types

token = '<PLEASE PUT TOKEN HERE>'
f = open('countries_immigration.txt', 'r', encoding='UTF-8')
immigration = f.read().split('\n')
f.close()
f = open('countries_tourism.txt.txt', 'r', encoding='UTF-8')
tourism = f.read().split('\n')
f.close()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Immigration")
    item2 = types.KeyboardButton("Tourism")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Check the top countries shortlist for immigration or for tourism ',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip().find('Immigration') != -1:
        bot.send_message(message.chat.id, random.choice(immigration))
    elif message.text.strip().find('Tourism') != -1:
        bot.send_message(message.chat.id, random.choice(tourism))


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
