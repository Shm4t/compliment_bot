import telebot as tb
import random
from telebot import types
from my_secrets import BOT_TOKEN
from compliments import COMPLIMENTS
bot = tb.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start_mesage(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    action_button = types.KeyboardButton('💕Комплимент')
    markup.add(action_button)
    bot.send_message(message.chat.id, text='Привет, {0.first_name}\nВоспользуйся кнопками!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == '💕Комплимент':
        random_index = random.randint(0, len(COMPLIMENTS) - 1)
        bot.send_message(message.chat.id, text=f'{COMPLIMENTS[random_index]}')
    else:
        bot.send_message(message.chat.id, text='Бро, лучше воспользуйся кнопками😉')


bot.polling(none_stop=True, interval=0)
