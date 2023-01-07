import telebot
from telebot import types
BOT_URL = "https://t.me/Dwqertyjukfyjdthsdbot"

TOKEN = "5853852070:AAFiPnJtzMbaNFNPNCcfAWEKgiynQHtq4dE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}. Я бот дневник и могу помочь тебе с уроками\n Ты можешь вызвать меню /menu ')


@bot.message_handler(commands=['menu'])
def rad(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buton1 = types.KeyboardButton("Электронный журнал")
    buton2 = types.KeyboardButton("Расписание")
    buton3 = types.KeyboardButton('Убрать клавиатуру')
    markup.add(buton1, buton2, buton3)
    bot.send_message(message.chat.id,'Открываю меню...', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Понедельник"):
        bot.send_message(message.chat.id, 'Вот расписание на ужасный понедельник:\n'
                                          "\n"
                                        "1	Изо\n"
                                        "2	Англ яз\n"
                                        "3	Физра\n"
                                        "4	Алгебра\n"
                                        "5	Икт\n"
                                        "6	Рус яз\n"
                                        "7	Доп. матем\n ")
    elif message.text == "Вторник":
        bot.send_message(message.chat.id, 'Вот расписание на такой себе вторник:\n'
                                          "\n"
                                        "1	Истроия\n"
                                        "2	Физра\n"
                                        "3	Химия\n"
                                        "4	Немецкий\n"
                                        "5	Рус яз\n"
                                        "6	Геометрия\n"
                                        "7	Кл час\n ")
    elif message.text == "Среда":
        bot.send_message(message.chat.id, 'Вот расписание на среднию среду:\n'
                                          "\n"
                                        "1	Физика\n"
                                        "2	Англ яз\n"
                                        "3	Биология\n"
                                        "4	Рус яз\n"
                                        "5	Алгебра\n"
                                        "6	География\n")
    elif message.text == "Четверг":
        bot.send_message(message.chat.id, 'Вот расписание на сложний четверг:\n'
                                        "\n"
                                        "1	Литер\n"
                                        "2	Биология\n"
                                        "3	Рус яз\n"
                                        "4	Геометрия\n"
                                        "5	Химия\n"
                                        "6	Общество\n")
    elif message.text == "Пятница":
        bot.send_message(message.chat.id, 'Вот расписание на отличную пятницу:\n'
                                          "\n"
                                        "1	Алгебра\n"
                                        "2	Рус яз\n"
                                        "3	Родной\n"
                                        "4	Баш/ИКБ\n"
                                        "5	ОБЖ\n"
                                        "6	История\n"
                                        "7	Технологи\n ")
    elif message.text == "Суббота":
        bot.send_message(message.chat.id, 'В субботу выходной так что, отдыхай')
    elif message.text == "Спасибо":
        bot.send_message(message.chat.id, 'Пожалуйста, приходи еще')
    elif message.text == "Расписание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Суббота")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id,'Чтобы посмотреть расписание выбери день недели', reply_markup=markup)
    elif message.text == "Электронный журнал":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Электронный журнал", url='https://elschool.ru/')
        markup.add(button1)
        bot.send_message(message.chat.id,'Нажми на кнопку чтобы перейти в электронный журнал', reply_markup=markup)
    elif message.text == "/remove":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Убираю клавиатуру', reply_markup=a)
    elif message.text == "Убрать клавиатуру":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Убираю клавиатуру', reply_markup=a)

bot.infinity_polling()
