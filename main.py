from random import choice
from telebot import TeleBot

import telebot

SECRET_KEY = '5950500285:AAEtn4gi1w1IEXbxhsowVtD_L63Q3M1TIC0'

bot = TeleBot(SECRET_KEY)

# Create a reaction to /start command
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    red_button = telebot.types.KeyboardButton("🟥")
    black_button = telebot.types.KeyboardButton("⬛")
    keyboard.row(red_button)
    keyboard.row(black_button)

    bot.send_message(message.chat.id, "What color is it: 🟥 or ⬛ ?", reply_markup=keyboard)
    bot.register_next_step_handler(message, answer_card)

def answer_card(message):
    card, suit = random_card()
    if message.text == "🟥" and suit in ['H', 'D']:
        bot.send_message(message.chat.id, f"Congrats! You've guessed! The card was {card}{suit}")
    elif message.text == "⬛" and suit in ['S', 'C']:
        bot.send_message(message.chat.id, f"Congrats! You've guessed! The card was {card}{suit}")
    else:
        bot.send_message(message.chat.id, f"Oops! You didn't guess. The card was {card}{suit}")

    start_message(message)

# Generate a random card
def random_card():
    chosen_card_number = choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
    chosen_card_suit = choice(["H", "D", "S", "C"])

    return chosen_card_number, chosen_card_suit

bot.infinity_polling()