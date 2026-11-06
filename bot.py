import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

balance = 10.00

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        f"Pump.fun Demo Bot is running!\n"
        f"Virtual Balance: ${balance:.2f}\n"
        f"Mode: DEMO"
    )

bot.infinity_polling()
