import telebot
from telebot import types
import time
import json
import sys

with open('secret.json', 'r') as secretfile:
    json_data=secretfile.read()

data = json.loads(json_data)

#GRUPO = -399335665

bot = telebot.TeleBot(str(data['token']))

AYUDA = 'Tu para que quieres ayuda, tonto'

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
    time.sleep(0.3)
    bot.send_message(cid, AYUDA)

@bot.message_handler(commands=['evento'])
def command_evento(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(0.2)
    bot.send_message(cid, 'EVENTRO CREADO, PONLE NOMBRE: ')
    NombreEvento = True

@bot.message_handler(func=lambda message: True)
def reply_message(m):
    cid = m.chat.id
    if cid > 0:
        NombreEv = m.text
        bot.send_message(cid, str(NombreEv))
        print("Funciona")
        f = open( 'info.txt', 'a')
        f.write(str(NombreEv) + ";")
        f.close()

bot.polling()
