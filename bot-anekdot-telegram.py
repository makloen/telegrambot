# -*- coding: utf-8 -*-
import telebot
import requests

bot = telebot.TeleBot("token")

def random_joke():
	url = "http://api.icndb.com/jokes/random"
	joke = requests.get(url).json()
	return joke['value']['joke']

@bot.message_handler(content_types=["text"])
def any_msg(message):
	if message.text.lower() == "вйо":
		bot.send_message(message.chat.id, random_joke())
	else:
		bot.send_message(message.chat.id, 'Напиши "вйо", щоб почути анекдот')

if __name__ == '__main__':
	bot.polling(none_stop=True)