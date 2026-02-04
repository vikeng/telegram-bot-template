from init_env import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Hello!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, message.text)
