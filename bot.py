import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7733763063:AAEo6sg_E-4wNTuIPWVVER6m1sBMJ8CEdUw" 
CARD_NUMBER = "4400 4301 1454 5251"  

bot = telebot.TeleBot(TOKEN)

def main():
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        button = KeyboardButton("Поддержать проект 💰")
        markup.add(button)
        bot.send_message(message.chat.id, "Добро пожаловать! Нажмите кнопку, чтобы получить реквизиты для доната.", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Поддержать проект 💰")
    def send_card_number(message):
        bot.send_message(message.chat.id, f"Вы можете поддержать проект, отправив донат на карту: {CARD_NUMBER}")

    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()