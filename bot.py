# coding=utf-8
import telebot
import const
from telebot import types

TOKEN = '1175158114:AAGsO3OLdGo-FL00vs5W0DDaJDoiiGvgL1E'

bot = telebot.TeleBot(TOKEN)

PHOTO_1 = 'https://sun6-16.userapi.com/c841129/v841129454/8e3/Io2pyhQ60Ts.jpg'

@bot.message_handler(commands=['start'])
def startpg(message):
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Заполнить анкету')
    bot.send_message(message.chat.id, 'Добро пожаловать!\nНаш бот познакомит Вас с девушками для общения и не только 😌')
    bot.send_message(message.chat.id, 'Жми заполнить анкету ❤', reply_markup=startmenu)

@bot.message_handler(content_types=['text'])
def osnov(message):
    global keks
    keks = 'keks'
    if message.text == 'Заполнить анкету':
        send = bot.send_message(message.chat.id, 'Введите своё имя:')
        bot.register_next_step_handler(send, next1)
    elif message.text == 'Показать анкету':
        if keks == 'keks':
            knopka = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text='📱Tel. +79242716*** 💝instagram.com/*****', url='google.com')
            but_2 = types.InlineKeyboardButton(text='Date her', url='https://youtube.com')
            knopka.add(but_1)
            knopka.add(but_2)
            bot.send_photo(message.chat.id, PHOTO_1, caption='Аня, 26 лет', reply_markup=knopka)

def next1(message):
    send = bot.send_message(message.chat.id, 'Очень приятно, {name}, сколько вам лет?'.format(name=message.text))
    bot.register_next_step_handler(send, next2)

def next2(message):
    global keks
    keks = 'keks'
    forwhat = types.ReplyKeyboardMarkup(True, False)
    forwhat.row('Показать анкету')
    bot.send_message(message.chat.id, 'Хорошо мы найдем вам девушку примерно вашего возраста. Начать показывать анкеты?'.format(sity=message.text), reply_markup=forwhat)





bot.polling()