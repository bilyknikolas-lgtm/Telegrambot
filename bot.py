import telebot

bot = telebot.TeleBot("7631628545:AAFS978oXDfE6R8e8gj7aOGf4tRzOx94gqg")

user_step = {}
user_name = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте")
    user_step[message.chat.id] = 1

@bot.message_handler(content_types=['text'])
def text_handler(message):
    chat_id = message.chat.id

    if user_step.get(chat_id) == 1:
        user_name[chat_id] = message.text
        bot.send_message(chat_id, "Отправьте видео")
        user_step[chat_id] = 2

@bot.message_handler(content_types=['video'])
def video_handler(message):
    chat_id = message.chat.id

    if user_step.get(chat_id) == 2:
        name = user_name.get(chat_id, "неизвестно")
        bot.send_message(chat_id, f"Видео получено от: {name}")
        user_step[chat_id] = 1

bot.infinity_polling()
