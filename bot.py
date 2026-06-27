import telebot
import smtplib
from email.mime.text import MIMEText

TOKEN = "7631628545:AAFS978oXDfE6R8e8gj7aOGf4tRzOx94gqg"

EMAIL = "bilyknikolas@gmail.com"
APP_PASSWORD = "ggme nqte bjee xvnm"

bot = telebot.TeleBot(TOKEN)

user_name = {}

def send_email(name, file_id):
    try:
        msg = MIMEText(f"Имя: {name}\nВидео file_id: {file_id}")
        msg["Subject"] = "Telegram Bot Video"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("EMAIL SENT SUCCESS")
        return True

    except Exception as e:
        print("EMAIL ERROR:", e)
        return False

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте. Введите имя")

@bot.message_handler(content_types=['text'])
def get_name(message):
    chat_id = message.chat.id
    user_name[chat_id] = message.text
    bot.send_message(chat_id, "Теперь отправьте видео")

@bot.message_handler(content_types=['video'])
def get_video(message):
    chat_id = message.chat.id
    name = user_name.get(chat_id, "неизвестно")

    file_id = message.video.file_id

    success = send_email(name, file_id)

    if success:
        bot.send_message(chat_id, "✔ Отправлено")
    else:
        bot.send_message(chat_id, "❌ Ошибка отправки")

bot.infinity_polling()
