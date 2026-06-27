import telebot
import smtplib
from email.mime.text import MIMEText

TOKEN = "7631628545:AAFS978oXDfE6R8e8gj7aOGf4tRzOx94gqg"

EMAIL = "bilyknikolas@gmail.com"
APP_PASSWORD = "ggme nqte bjee xvnm"

bot = telebot.TeleBot(TOKEN)

user_name = {}

def send_email(name, file_id):
    msg = MIMEText(f"Имя: {name}\nВидео file_id: {file_id}")
    msg["Subject"] = "Новое видео из Telegram бота"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте. Введите имя")

@bot.message_handler(content_types=['text'])
def get_name(message):
    user_name[message.chat.id] = message.text
    bot.send_message(message.chat.id, "Теперь отправьте видео")

@bot.message_handler(content_types=['video'])
def get_video(message):
    chat_id = message.chat.id
    name = user_name.get(chat_id, "неизвестно")

    file_id = message.video.file_id

    send_email(name, file_id)

    bot.send_message(chat_id, "Видео отправлено на почту")

bot.infinity_polling()
