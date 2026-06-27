import telebot

TOKEN = "7631628545:AAFnesbnhVHiS04_vZwy9oTEOrtoy1NbFpE"

bot = telebot.TeleBot(TOKEN)

user_name = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте. Введите имя")

@bot.message_handler(content_types=['text'])
def get_name(message):
    chat_id = message.chat.id
    user_name[chat_id] = message.text
    bot.send_message(chat_id, "Теперь отправьте видео")

@bot.message_handler(content_types=['video', 'document'])
def get_video(message):
    chat_id = message.chat.id

    name = user_name.get(chat_id, "неизвестно")

    bot.send_message(chat_id, "Видео отправлено\nИмя: " + name)

if __name__ == "__main__":
    bot.infinity_polling()
