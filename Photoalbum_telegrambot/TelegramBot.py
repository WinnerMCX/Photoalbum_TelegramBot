import telebot
from telebot import types
import random
import Settings


messages_storage = []
lst_random_phrases = ['Смотри, какой я классный', 'Ыыы', 'Здравствуйте, меня зовут Дядя Степа, мне 24 годика', 'Говорят, что в первый раз только геморрой', 'Паровозик турутуру', 'Я не пидр, я гомосексуал', 'Называй меня дробителем аналов']
lst_bad_words = ['Шлюха', 'шлюха', '', '', '', '', '', '', '', '',]
lst_pidor = ['Пидр', 'пидр', 'Ты пидр', 'ты пидр', 'Пидор', 'пидор', 'Ты пидор', 'ты пидор']


lst_stas_2022 = ['photos/stas_and_misha_2022 (1).jpg','photos/stas_and_misha_2022 (2).jpg']
lst_stas_2021 = ['photos/stas_2021 (1).jpg']
lst_stas_2020 = ['photos/stas_2020 (1).jpg']
lst_stas_2012_2014 = ['photos/stas_2012_2014 (1).jpg']

lst_daniil_2022 = []
lst_daniil_2021 = ['photos/misha_and_daniil_2021 (1).jpg', 'photos/misha_and_daniil_2021 (2).jpg']

lst_valia_2022 = ['photos/valia_all_years (1).jpg', 'photos/valia_all_years (2).jpg']
lst_valia_2021 = ['photos/valia_all_years (1).jpg', 'photos/valia_all_years (2).jpg']

lst_misha_2022 = ['photos/stas_and_misha_2022 (1).jpg','photos/stas_and_misha_2022 (2).jpg', 'photos/misha_all_years (1).jpg']
lst_misha_2021 = ['photos/misha_all_years (1).jpg', 'photos/misha_and_daniil_2021 (1).jpg', 'photos/misha_and_daniil_2021 (2).jpg']
lst_misha_2020 = ['photos/misha_2020 (1).jpg']
lst_misha_2019 = ['photos/misha_2019 (1).jpg', 'photos/misha_2019 (2).jpg', 'photos/misha_all_years (1).jpg']

lst_ilusha_2022 = []
lst_ilusha_2021 = []

lst_danil_2022 = []

lst_all_photos = ['photos/stas_and_misha_2022 (1).jpg','photos/stas_and_misha_2022 (2).jpg','photos/stas_2021 (1).jpg',  
'photos/stas_2020 (1).jpg','photos/valia_all_years (1).jpg', 'photos/valia_all_years (2).jpg','photos/misha_and_daniil_2021 (1).jpg',
'photos/misha_and_daniil_2021 (2).jpg','photos/stas_and_misha_2022 (2).jpg','photos/misha_2020 (1).jpg','photos/misha_2019 (1).jpg',
'photos/misha_2019 (2).jpg', 'photos/misha_all_years (1).jpg']

lst_all_photos_order = ['lst_stas_12-22','lst_daniil_21-22','lst_valia_21-22','lst_misha_20-22','lst_ilusha_21-22','lst_danil_22'] #Импровизированный лист, он на самом деле не используеться, но я использую его как подсказку для переменной choose_character
lst_years = ['~2012-2014','2019','2020','2021','2022']
lst_all_names = ['Сас', 'Фистинг-энал-мастер', 'va L ix', 'Качок мыша', 'Уебан', 'Наполовину гачи чел по кличке Даниил']

def fill_lists():
    for i in range(1,10):
        lst_stas_2022.append('photos/'+'stas_2022 ('+str(i)+')''.jpg') #Стас
        lst_all_photos.append('photos/'+'stas_2022 ('+str(i)+')''.jpg') #Стас

    for i in range(1,10):
        lst_daniil_2021.append('photos/'+'daniil_2021 ('+str(i)+')''.jpg') #Даннил
        lst_all_photos.append('photos/'+'daniil_2021 ('+str(i)+')''.jpg')
    for i in range(1,4):
        lst_daniil_2022.append('photos/'+'daniil_2022 ('+str(i)+')''.jpg')
        lst_all_photos.append('photos/'+'daniil_2022 ('+str(i)+')''.jpg') #Даниил

    for i in range(1,6):
        lst_valia_2021.append('photos/'+'valia_2021 ('+str(i)+')''.jpg') #Валя
        lst_all_photos.append('photos/'+'valia_2021 ('+str(i)+')''.jpg') 
    for i in range(1,9):
        lst_valia_2022.append('photos/'+'valia_2022 ('+str(i)+')''.jpg')
        lst_all_photos.append('photos/'+'valia_2022 ('+str(i)+')''.jpg') #Валя

    for i in range(1,6):
        lst_misha_2021.append('photos/'+'misha_2021 ('+str(i)+')''.jpg') #Миша
        lst_all_photos.append('photos/'+'misha_2021 ('+str(i)+')''.jpg')
    for i in range(1,13):
        lst_misha_2022.append('photos/'+'misha_2022 ('+str(i)+')''.jpg')
        lst_all_photos.append('photos/'+'misha_2022 ('+str(i)+')''.jpg') #Валя

    for i in range(1,4):
        lst_ilusha_2021.append('photos/'+'ilusha_2021 ('+str(i)+')''.jpg') #Илюша
        lst_all_photos.append('photos/'+'ilusha_2021 ('+str(i)+')''.jpg')
    for i in range(1,5):
        lst_ilusha_2022.append('photos/'+'ilusha_2022 ('+str(i)+')''.jpg')
        lst_all_photos.append('photos/'+'ilusha_2022 ('+str(i)+')''.jpg') #Илюша

    for i in range(1,6):
        lst_danil_2022.append('photos/'+'danil_2022 ('+str(i)+')''.jpg') #Даниил Бурков

    for i in range(1,8):
        lst_all_photos.append('photos/'+'funphoto ('+str(i)+')''.jpg') #Фанфото

fill_lists()
#print(len(lst_misha_2022))


bot = telebot.TeleBot(Settings.API_KEY)


#while True:
    
#bot.send_message(813622197, 'Не, ну я угарно сделал, докажи?') #Данил Бурков
#bot.send_message(1184145229, 'ладн, пока') #Миша
#bot.send_message(1520959970, '') #Валя
#bot.send_message(5226124276, '') #Илья
#bot.send_message(1445713749, f'1000-7 = {a}') #Даниил Каргин
@bot.message_handler(commands=['help','хелп','помощь'])
def send_help(msg):
    messages_storage.append(msg.text)
    with open('Photoalbum_telegrambot/Вся инфа.txt', 'rb') as open1:
        bot.send_message(msg.chat.id, '''Команды и что они делают:

/help (/хелп, /помощь), /random (/рандом), /select (/селект, /выбрать), /download (/скачать)

/help - информация о боте /random - фановая функция что бы покрутить рандомные фотки гачи мэнов. ~10% на то, что бы добавилась рандомная надпись(их всего 6 пока что). В этой команде так же встречаеться фото не гачи мэнов. /select - основная команда, что бы выбрать конкретного гачи чела и год и посмотреть пару фоток. Может встретиться фотка не гачи мэна, но, это значит, что эта фотка охарактеризовывает его. Максимум можно посмотреть 3 гачи-мэна за раз. /download - тоже основная команда, что бы скачать абсолютно все фотки, которые здесь есть, включая фановых. 

Инфа о боте:

В основном, этот бот создан что бы хранить все наши фотки разных годов и их можно было удобно посмотреть в любой момент. Но так же, если скучно, можно полистать /рандом по-фану. 

Бот был создан 24.09.2022, тогда я еще не умел хорошо его кодить и написал что-то фиговое. Под конец этого же дня я обнаружил, что если register_next_step_handler и что можно просто ссылать на функцию, а не вызывать ее и начал переделывать бота. 25.09.2022 полностью закончил его. Код все еще фиговый, длинный, но рабочий. В общем, написал его за 2 дня. ПРЯМ ЦЕЛЫХ, ПОЛНОЦЕННЫХ 2 ДНЯ.

Всего фоток: 78 (точное число).

(не точно) (все года):
Фановых - 7
Стас - 14
Даниил Каргин - 12
Валя - 13
Миша - 22
Илья - 7
Даниил Бурков - 5''')
        bot.send_document(msg.chat.id,open1)
        bot.send_message(msg.chat.id,'Лучше скачать файл и окрыть его через что-то, текст не должен быть сбитым, ну, или же можешь читать этот убитый текст вверху. Изменено: Файл уже усторевший, текст вроде бы сделал норм.')

@bot.message_handler(commands=['download','скачать'])
def send_all_photos(msg):
    messages_storage.append(msg.text)
    with open('Photoalbum_telegrambot/Архив WinRaR.rar', 'rb') as open1:
        bot.send_message(msg.chat.id, 'Внизу абсолютно все фотки')
        bot.send_document(msg.chat.id, open1)

@bot.message_handler(commands=['random','рандом'])
def create_random_btn(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Рандом фото'))
    bot.send_message(msg.chat.id,'Нажимай на кнопку что бы получить рандомное фото гачи-мэнов. Если хочешь выбрать какого-то конкретного персонажа, то, напиши cumанду /select',reply_markup=markup)
    #bot.register_next_step_handler(message, random_function)

@bot.message_handler(func=lambda msg: msg.text == 'Рандом фото')
def send_random_photo(msg):
    messages_storage.append(msg.text)

    hmmims = len(messages_storage) #how_many_messages_in_messages_store
    if hmmims / 20 == 1 or hmmims / 20 == 2 or hmmims / 20 == 3 or hmmims / 20 == 4 or hmmims / 20 == 5 or hmmims / 20 == 6 or hmmims / 20 == 7 or hmmims / 20 == 8 or hmmims / 20 == 9 or hmmims / 20 == 10:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Рандом фото'))
        bot.send_message(msg.chat.id, 'Ты так же можешь написать cumанду /select что бы выбрать гачи чела',reply_markup=markup)
    
    should_we_add_phrase = random.randint(1,5)
    random_number_for_phrases_list = random.randint(0,6)

    choose_random_photo = random.randint(0, 76)
    open1 = open(lst_all_photos[choose_random_photo], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    lamb = lambda msg: bot.send_message(msg.chat.id, lst_random_phrases[random_number_for_phrases_list]) if (should_we_add_phrase == 1) else None
    lamb(msg)

@bot.message_handler(commands=['select','выбрать','селект'])
def create_btn_for_directions(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Сас'),types.KeyboardButton('Фистинг-энал-мастер'),types.KeyboardButton('va L ix'),types.KeyboardButton('Качок мыша'),types.KeyboardButton('Уебан'),types.KeyboardButton('Наполовину гачи чел по кличке Даниил'))
    register_thing = bot.send_message(msg.chat.id, 'Выбери гачи-мэна', reply_markup = markup)
    bot.register_next_step_handler(register_thing,directions)
    messages_storage.append(msg.text)
def directions(msg):
    bot.send_message(msg.chat.id,'👨‍❤️‍💋‍👨')
    if msg.text == 'Сас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('2022'),types.KeyboardButton('2021'),types.KeyboardButton('2020'),types.KeyboardButton('~2012-2014'))
        register_thing = bot.send_message(msg.chat.id,'Выбери год',reply_markup=markup)
        bot.register_next_step_handler(register_thing,check_what_year)
    elif msg.text == 'Фистинг-энал-мастер':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('2022'),types.KeyboardButton('2021'))
        register_thing = bot.send_message(msg.chat.id,'Выбери год',reply_markup=markup)
        bot.register_next_step_handler(register_thing,check_what_year)
    elif msg.text == 'va L ix':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('2022'),types.KeyboardButton('2021'))
        register_thing = bot.send_message(msg.chat.id,'Выбери год',reply_markup=markup)
        bot.register_next_step_handler(register_thing,check_what_year)
    elif msg.text == 'Качок мыша':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('2022'),types.KeyboardButton('2021'),types.KeyboardButton('2020'),types.KeyboardButton('2019'))
        register_thing = bot.send_message(msg.chat.id,'Выбери год',reply_markup=markup)
        bot.register_next_step_handler(register_thing,check_what_year)
    elif msg.text == 'Уебан':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('2022'),types.KeyboardButton('2021'))
        register_thing = bot.send_message(msg.chat.id,'Выбери год',reply_markup=markup)
        bot.register_next_step_handler(register_thing,check_what_year)
    elif msg.text == 'Наполовину гачи чел по кличке Даниил':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('2022'))
        register_thing = bot.send_message(msg.chat.id,'Выбери год',reply_markup=markup)
        bot.register_next_step_handler(register_thing,check_what_year)
    else:
        markup1 = types.ReplyKeyboardRemove()
        bot.send_message(msg.chat.id,'ты - 🤡', reply_markup=markup1)
    messages_storage.append(msg.text)
    print(messages_storage)


def check_what_year(msg):
    messages_storage.append(msg.text)
    if messages_storage[-2] == 'Сас' and msg.text == '2022':
        stas_2022(msg)
    elif messages_storage[-2] == 'Сас' and msg.text == '2021':
        stas_2021(msg)
    elif messages_storage[-2] == 'Сас' and msg.text == '2020':
        stas_2020(msg)
    elif messages_storage[-2] == 'Сас' and msg.text == '~2012-2014':
        stas_2012_2014(msg)

    elif messages_storage[-2] == 'Фистинг-энал-мастер' and msg.text == '2022':
        daniil_2022(msg)
    elif messages_storage[-2] == 'Фистинг-энал-мастер' and msg.text == '2021':

        daniil_2021(msg)
    elif messages_storage[-2] == 'va L ix' and msg.text == '2022':
        valia_2022(msg)
    elif messages_storage[-2] == 'va L ix' and msg.text == '2021':
        valia_2021(msg)
    
    elif messages_storage[-2] == 'Качок мыша' and msg.text == '2022':
        misha_2022(msg)
    elif messages_storage[-2] == 'Качок мыша' and msg.text == '2021':
        misha_2021(msg)
    elif messages_storage[-2] == 'Качок мыша' and msg.text == '2020':
        misha_2020(msg)
    elif messages_storage[-2] == 'Качок мыша' and msg.text == '2019':
        misha_2019(msg)

    elif messages_storage[-2] == 'Уебан' and msg.text == '2022':
        ilusha_2022(msg)
    elif messages_storage[-2] == 'Уебан' and msg.text == '2021':
        ilusha_2021(msg)

    elif messages_storage[-2] == 'Наполовину гачи чел по кличке Даниил' and msg.text == '2022':
        danil_2022(msg)
                        
    else:
        #bot.send_message(msg.chat.id,'🤡 кидаю в мут')
        markup1 = types.ReplyKeyboardRemove()
        bot.send_message(msg.chat.id,'🤡 кидаю в мут', reply_markup=markup1)


def stas_2022(msg):
    count_random = random.randint(0,10) #+2 потому что 2 фотки еще отдельно внутри листа
    open1 = open(lst_stas_2022[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()    
    extra_buttons(msg)                                       #Создать кнопку повтора
def stas_2021(msg):
    open1 = open(lst_stas_2021[0], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    bot.send_message(msg.chat.id,'Всего 1 фото, напишите /select что бы начать заново') 
def stas_2020(msg):
    open1 = open(lst_stas_2020[0], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    bot.send_message(msg.chat.id,'Всего 1 фото, напишите /select что бы начать заново')
def stas_2012_2014(msg):
    open1 = open(lst_stas_2012_2014[0], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close() 
    bot.send_message(msg.chat.id,'Всего 1 фото, напишите /select что бы начать заново')

def daniil_2022(msg):
    count_random = random.randint(0,2)
    open1 = open(lst_daniil_2022[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)
def daniil_2021(msg):
    count_random = random.randint(0,10) #+2 потому что 2 фотки еще отдельно внутри листа
    open1 = open(lst_daniil_2021[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)


def valia_2022(msg):
    count_random = random.randint(0,9) #+2 потому что 2 фотки еще отдельно внутри листа
    open1 = open(lst_valia_2022[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)
def valia_2021(msg):
    count_random = random.randint(0,6) #+2 потому что 2 фотки еще отдельно внутри листа
    open1 = open(lst_valia_2021[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)

def misha_2022(msg):
    count_random = random.randint(0,14) #+3 потому что еще 3 фотки отдельно внутри листа
    open1 = open(lst_misha_2022[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)
def misha_2021(msg):
    count_random = random.randint(0, 7) #+3 потому что еще 3 фотки отдельно внутри листа
    open1 = open(lst_misha_2021[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)
def misha_2020(msg):
    open1 = open(lst_misha_2020[0], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    bot.send_message(msg.chat.id,'Всего 1 фото, напишите /select что бы начать заново')
def misha_2019(msg):
    count_random = random.randint(0, 2) #3 фотки уже в листе
    open1 = open(lst_misha_2021[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)

def ilusha_2022(msg):
    count_random = random.randint(0,3)
    open1 = open(lst_ilusha_2022[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)
def ilusha_2021(msg):
    count_random = random.randint(0,2)
    open1 = open(lst_ilusha_2021[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)

def danil_2022(msg):
    count_random = random.randint(0,4)
    open1 = open(lst_danil_2022[count_random], 'rb')
    bot.send_photo(msg.chat.id,open1)
    open1.close()
    extra_buttons(msg)



def extra_buttons(msg):
    print(messages_storage)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)   #Создать кнопку повтора
    markup.add(types.KeyboardButton('Еще фото'), types.KeyboardButton('Нет'))
    register_thing = bot.send_message(msg.chat.id,'Еще одно фото этого же гачи мэна и года?',reply_markup=markup)
    bot.register_next_step_handler(register_thing, again)
def again(msg):
    messages_storage.append(msg.text)
    print(messages_storage)
    if msg.text == 'Нет':
        open1 = open('photos/funphoto (7).jpg', 'rb')
        markup1 = types.ReplyKeyboardRemove()
        bot.send_photo(msg.chat.id, open1,'Гомосексуала ответ', reply_markup=markup1)
        open1.close()
    elif messages_storage[-3] == 'Сас' and messages_storage[-2] == '2022' or messages_storage[-4] == 'Сас' and messages_storage[-3] == '2022':
        stas_2022(msg)
    elif messages_storage[-3] == 'Фистинг-энал-мастер' and messages_storage[-2] == '2022' or messages_storage[-4] == 'Фистинг-энал-мастер' and messages_storage[-3] == '2022':
        daniil_2022(msg)
    elif messages_storage[-3] == 'Фистинг-энал-мастер' and messages_storage[-2] == '2021' or messages_storage[-4] == 'Фистинг-энал-мастер' and messages_storage[-3] == '2021':
        daniil_2021(msg)
    elif messages_storage[-3] == 'va L ix' and messages_storage[-2] == '2022' or messages_storage[-4] == 'va L ix' and messages_storage[-3] == '2022':
        valia_2022(msg)
    elif messages_storage[-3] == 'va L ix' and messages_storage[-2] == '2021' or messages_storage[-4] == 'va L ix' and messages_storage[-3] == '2021':
        valia_2021(msg)
    elif messages_storage[-3] == 'Качок мыша' and messages_storage[-2] == '2022' or messages_storage[-4] == 'Качок мыша' and messages_storage[-3] == '2022':
        misha_2022(msg)
    elif messages_storage[-3] == 'Качок мыша' and messages_storage[-2] == '2021' or messages_storage[-4] == 'Качок мыша' and messages_storage[-3] == '2021':
        misha_2021(msg)
    elif messages_storage[-3] == 'Качок мыша' and messages_storage[-2] == '2019' or messages_storage[-4] == 'Качок мыша' and messages_storage[-3] == '2019':
        misha_2019(msg)
    elif messages_storage[-3] == 'Уебан' and messages_storage[-2] == '2022' or messages_storage[-4] == 'Уебан' and messages_storage[-3] == '2022':
        ilusha_2022(msg)
    elif messages_storage[-3] == 'Уебан' and messages_storage[-2] == '2021' or messages_storage[-4] == 'Уебан' and messages_storage[-3] == '2021':
        ilusha_2021(msg)
    elif messages_storage[-3] == 'Наполовину гачи чел по кличке Даниил' and messages_storage[-2] == '2022' or messages_storage[-4] == 'Наполовину гачи чел по кличке Даниил' and messages_storage[-3] == '2022':
        danil_2022(msg)
    else:
        markup1 = types.ReplyKeyboardRemove()
        bot.send_message(msg.chat.id, 'Все, хватит дрочить! Выбери еще кого-нибудь /select или же /random', reply_markup=markup1)
        

@bot.message_handler(content_types=['text'])
def any_message(msg):
    messages_storage.append(msg.text)
    print(messages_storage)
    print(f'айди чата: {msg.chat.id} пользователь: {msg.from_user.username} {msg.from_user.first_name} {msg.from_user.last_name}')
    #print(msg.from_user.first_name)
    #print(msg.from_user.last_name)
    #print(msg.from_user.username)
    #bot.send_message(msg.chat.id, msg)
    if msg.text in lst_pidor:
        bot.reply_to(msg, 'Я не пидр, я гомосексуал')
    elif msg.text == 'Привет' or msg.text == 'привет':
        bot.send_message(msg.chat.id,'Добро пожаловать в dungeon')
    elif msg.text in lst_bad_words:
        bot.reply_to(msg, f'сам {msg.text}')
    else:
        bot.send_message(msg.chat.id, 'Если ты 🤡, который нуждается в помощи напиши /help \n\nКраткий список команд(можешь просто нажать): \n\n/random, /select, /download (Для download прочитай /help) ')

bot.infinity_polling()