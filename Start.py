# -*- coding: utf-8 -*-

import telebot
from telebot import types
import os
import subprocess

TOKEN = '372274699:AAH8t7ML7zdXoCSxiJOqPSSFmTILQ68zflY'
bot = telebot.TeleBot(TOKEN)

chat_id = "-184142656"

def listener(mensajes): 
	for m in mensajes: 
		texto = m.text 
# Con print chr(27)+"[1;31m" coloreamos de rojo
		print chr(27)+"[1;31m"+('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto)
# Volvemos al color por defecto
		print chr(27)+"[0m" 
bot.set_update_listener(listener)

commands = {  # Diccionario para la ayuda comando help
              'hola': '',
              'adios': '',
              'ip': 'Devuelve la direccion IP publica del servidor.',
              'chatid': 'Devuelve el ID del chat, COMINGSOON.',
	      'estado': 'Devuelve un archivo HTML con el estado del servidor.',
	      'visitas': 'Muestra el numero total de visitas, COMINGSOON.',
	      'top': 'Muestra un listado de las 10 primeras IPs, COMINGSOON.',
}

# Ayuda
@bot.message_handler(commands=['help'])
def command_help(mensaje):
    help_text = "Que quieres perra?: \n \n"
    for key in commands:  # Bucle que extrae los datos del diccionario commands
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(chat_id, help_text) 

@bot.message_handler(commands=['chatid'])
def comando_hola(mensaje):
    bot.send_message(chat_id, 'Hola zorra')

@bot.message_handler(commands=['hola'])
def comando_hola(mensaje): 
    bot.send_message(chat_id, 'Hola zorra') 

@bot.message_handler(commands=['adios'])
def adios(mensaje):
    bot.send_message(chat_id, 'Drupal no se va a hacer solo cacho mierda')

@bot.message_handler(commands=['ip'])
def ip(mensaje):
# Descarga un index donde dice la IP publica
    os.system("wget cualesmiip.com")
# Filtra la direccion IP de toda la pagina y lo almacena en una variable
    ip = str("Su IP amo: ") + str("https://") + subprocess.check_output("cat index.html |grep 'real es'|cut -d' ' -f5|cut -d'<' -f1|cut -d'e' -f1 | sed 's/ //g' | tr -d '\n'", shell=True)
# Convierte la variable a un string para poder enviarlo correctamente luego
    string = str(ip)
# Elimina el index descargado previamente
    os.system("rm -r index.html")
    bot.send_message(chat_id, string)

@bot.message_handler(commands=['estado'])
def screenshot(mensaje):
    os.system("echo q | htop | aha --black --line-fix > Estado.html")
    doc = open('Estado.html', 'rb')
    os.system("rm Estado.html")
    bot.send_document(chat_id, doc)

bot.polling(none_stop = True)


