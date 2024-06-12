import telebot
import random
bot = telebot.TeleBot('6762704276:AAEQnls0E6WXbet1yidT0-jfzIHumah7o_8')

random_number = None  # Переменная для хранения загаданного числа

@bot.message_handler(commands=['start'])
def start_game(message):
    global random_number  # Используем глобальную переменную
    random_number = random.randint(1, 10)
    bot.send_message(message.chat.id, "Привет! Я загадал число от 1 до 10. Попробуй угадать!")

@bot.message_handler(func=lambda message: True)
def check_guess(message):
    global random_number  # Используем глобальную переменную
    try:
        guess = int(message.text)
        if guess < 1 or guess > 10:
            bot.send_message(message.chat.id, "Пожалуйста, введите число от 1 до 10.")
        else:
            if guess == random_number:
                bot.send_message(message.chat.id, f"Поздравляю, ты угадал число {random_number}!")
            elif guess < random_number:
                bot.send_message(message.chat.id, "Загаданное число больше. Попробуй еще раз.")
            else:
                bot.send_message(message.chat.id, "Загаданное число меньше. Попробуй еще раз.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число от 1 до 10.")

bot.polling()