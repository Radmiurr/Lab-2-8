import telebot
import json
import config

from telebot import types

bot = telebot.TeleBot('5819328038:AAHMFtRHHXvT_l5TmfLtBcXhs3sn18nwBSE', parse_mode = None)

JSON_FILE = 'students.json'

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    marks = json.load(f)

@bot.message_handler(commands=['start'])
def welkome(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Список группы")
    item2 = types.KeyboardButton("Покормить Кирби")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет я Криби!! Я знаю всю успеваемость студентов ;)', reply_markup=markup)

s=0
for g in marks:
    s=s+1
@bot.message_handler(content_types=['text'])
def lalala(message):
    a=message.text
    for g in range(0,s,1):
        if a==marks[g]['id']:
            q=marks[g]['epsents']
            bot.send_message(message.chat.id, marks[g]['lessons'])
            bot.send_message(message.chat.id, marks[g]['epsents'])
    if message.chat.type == 'private':
        if message.text == 'Список группы':
            for g in range(0, s, 1):
                bot.send_message(message.chat.id, marks[g]['id'])
        elif message.text == 'Покормить Кирби':
            bot.send_message(message.chat.id, 'Спасибо я очень рад!!')



bot.polling(none_stop=True)
