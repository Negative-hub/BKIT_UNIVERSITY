import os
from config import API_KEY
import telebot
from telebot import types

# Сообщения
mes_hi = 'Заставить бота сказать привет'
mes_photo = 'Спокойной ночи'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# Идентификатор диалога
	chat_id = message.chat.id

	# Текст, введенный пользователем, то есть текст с кнопки
	text = message.text
	
	# Проверка сообщения и вывод данных
	if text == mes_hi:
		bot.send_message(chat_id, "Привет, Юзер!")
	elif text == mes_photo:
		img = open(os.path.join(cur_path, 'img\GoodNight.jpg'), 'rb')
		bot.send_photo(chat_id, img)
	else:
		markup = types.ReplyKeyboardMarkup(row_width=2)
		itembtn1 = types.KeyboardButton(mes_hi)
		itembtn2 = types.KeyboardButton(mes_photo)
		markup.add(itembtn1, itembtn2)
		bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)

bot.infinity_polling()