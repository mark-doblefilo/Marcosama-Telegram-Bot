import telebot
from telebot import types
import time
import json
import sys

import gcalendar

with open('secret.json', 'r') as secretfile:
    json_data=secretfile.read()

data = json.loads(json_data)

bot = telebot.TeleBot(str(data['token']))

AYUDA = '[ ! ] I only work for my owner.'

print ("Token working. Starting...")
NombreEvento = False

def listener(messages):
    for m in messages:
        cid = m.chat.id
        if cid > 0:
            mensaje = str(m.chat.first_name) + "[" +str(cid) + "]: " + 'Ha mandado un mensaje'
        else:
            mensaje = str(m.from_user.username) + "[" + str(cid) + "]: " + 'Ha mandado un mensaje'
        print (mensaje)


bot.set_update_listener(listener)

@bot.message_handler(commands=['ayuda'])
def command_ayuda(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(0.2)
    bot.send_message(cid, AYUDA)

@bot.message_handler(commands=['calendario'])
def command_ayuda(m):
    cid = m.chat.id
    if (str(cid) == str(data['my_id'])):
        gcalendar.get_calendar(cid)
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(0.2)
        bot.send_message(cid, "[ ! ] You're not my owner. ")

bot.polling()
