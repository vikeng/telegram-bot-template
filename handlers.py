from init_env import TOKEN
import telebot
from datetime import datetime

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    bot.reply_to(message, "Hello!\n" + now)


@bot.message_handler(commands=['l', 'list'])
def start_command(message):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    notes = 'Текущая дата: ' + now
    bot.reply_to(message, notes)
