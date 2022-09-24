import telebot
from telebot import types
import random

messages_storage = []
lst_random_phrases = ['Смотри, какой я классный', 'Ыыы', 'Здравствуйте, меня зовут Дядя Степа, мне 24 годика', 'Говорят, что в первый раз только геморрой', 'Паровозик турутуру', 'Я не пидр, я гомосексуал', 'Называй меня дробителем аналов']
lst_bad_words = ['Шлюха', 'шлюха', '', '', '', '', '', '', '', '',]



lst_stas = ['stas_and_misha2.jpg']
lst_daniil = []
lst_valia = []
lst_misha = ['stas_and_misha2.jpg']
lst_ilusha = []
lst_danil = []
lst_all_photos = [lst_stas,lst_daniil,lst_valia,lst_misha,lst_ilusha,lst_daniil] #Импровизированный лист, он на самом деле не используеться, но я использую его как подсказку для переменной choose_character

def fill_lists():
    for i in range(1,13):
        lst_stas.append('stas'+str(i)+'.jpg')
    for i in range(2,17):
        lst_valia.append('valia'+str(i)+'.jpg')
    for i in range(1,16):
        lst_misha.append('misha'+str(i)+'.jpg')
    for i in range(1,14):
        lst_daniil.append('daniil'+str(i)+'.jpg')
    for i in range(1,6):
        lst_danil.append('danil'+str(i)+'.jpg')
    for i in range(1,8):
        lst_ilusha.append('ilusha'+str(i)+'.jpg')
fill_lists()


bot = telebot.TeleBot('5789422619:AAGRAyhZY4OEfcp1iH0nU76HSHVBG-tUy4M')




@bot.message_handler(commands=['random'])
def create_random_btn(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Рандом фото'))
    bot.send_message(msg.chat.id,'Нажимай на кнопку что бы получить рандомное фото гачи-мэнов. Если хочешь выбрать какого-то конкретного персонажа, то, напиши /select',reply_markup=markup)
    #bot.register_next_step_handler(message, random_function)
@bot.message_handler(func=lambda msg: msg.text == 'Рандом фото')
def send_photo(msg):
    messages_storage.append(msg.text)
    print(messages_storage)

  
    hmmims = len(messages_storage) #how_many_messages_in_messages_store
    if hmmims / 10 == 1 or hmmims / 10 == 2 or hmmims / 10 == 3 or hmmims / 10 == 4 or hmmims / 10 == 5 or hmmims / 10 == 6 or hmmims / 10 == 7 or hmmims / 10 == 8 or hmmims / 10 == 9 or hmmims / 10 == 10:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Рандом фото'))
        bot.send_message(msg.chat.id, 'Ты так же можешь написать комнаду /select что бы выбрать гачи чела',reply_markup=markup)
    else:
        pass
    


    choose_character = random.randint(0,5)
    photos = 'photos/'
    should_we_add_phrases = random.randint(1,5)
    random_number_for_phrases_list = random.randint(0,6)

    if choose_character == 0:
        count_random1 = random.randint(0,12)
        open1 = open(photos+lst_stas[count_random1],'rb')
        bot.send_photo(msg.chat.id,open1)
        open1.close()
        lamb = lambda msg: bot.send_message(msg.chat.id,lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrases == 1) else None
        lamb(msg)
    elif choose_character == 1:
        count_random2 = random.randint(0,12)
        open2 = open(photos+lst_daniil[count_random2],'rb')
        bot.send_photo(msg.chat.id,open2)
        open2.close()
        lamb = lambda msg: bot.send_message(msg.chat.id,lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrases == 1) else None
        lamb(msg)
    elif choose_character == 2:
        count_random3 = random.randint(0,14)
        open3 = open(photos+lst_valia[count_random3],'rb')
        bot.send_photo(msg.chat.id,open3)
        open3.close()
        lamb = lambda msg: bot.send_message(msg.chat.id,lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrases == 1) else None
        lamb(msg)
    elif choose_character == 3:
        count_random4 = random.randint(0,13)
        open4 = open(photos+lst_misha[count_random4],'rb')
        bot.send_photo(msg.chat.id,open4)
        open4.close()
        lamb = lambda msg: bot.send_message(msg.chat.id,lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrases == 1) else None
        lamb(msg)
    elif choose_character == 4:
        count_random5 = random.randint(0,6)
        open5 = open(photos+lst_ilusha[count_random5],'rb')
        bot.send_photo(msg.chat.id,open5)
        open5.close()
        lamb = lambda msg: bot.send_message(msg.chat.id,lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrases == 1) else None
        lamb(msg)
    elif choose_character == 5:
        count_random6 = random.randint(0,4)
        open6 = open(photos+lst_danil[count_random6],'rb')
        bot.send_photo(msg.chat.id,open6)
        open6.close()
        lamb = lambda msg: bot.send_message(msg.chat.id,lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrases == 1) else None
        lamb(msg)





@bot.message_handler(content_types=['text'])
def any_message(msg):
    messages_storage.append(msg.text)
    print(messages_storage)
    if msg.text == 'пидр' or msg.text == 'Пидр':
        bot.reply_to(msg, 'Я не пидр, я гомосексуал')
    elif msg.text in lst_bad_words:
        bot.reply_to(msg, f'сам {msg.text}')
    else:
        bot.send_message(msg.chat.id, "Я вас не понимаю. Можете написать команду /help для помощи")

bot.infinity_polling()