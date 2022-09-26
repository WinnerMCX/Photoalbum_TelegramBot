from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5789422619:AAGRAyhZY4OEfcp1iH0nU76HSHVBG-tUy4M')

@bot.message_handler(content_types=['text'])
def test(msg):
    message = msg.text
    bot.register_next_step_handler(message,idk)
def idk(msg):
    bot.send_message(msg.chat.id,'it worked')
bot.infinity_polling()