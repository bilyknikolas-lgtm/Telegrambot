import telebot
import smtplib
from email.mime.text import MIMEText

TOKEN = "7631628545:AAFnesbnhVHiS04_vZwy9oTEOrtoy1NbFpE"

EMAIL = "bilyknikolas@gmail.com"
APP_PASSWORD = "YOUR_APP_PASSWORD"

bot = telebot.TeleBot(TOKEN)

user_name = {}

def send_email(name, file_id):
    try:
        msg = MIMEText(f"Имя: {name}\nVideo file_id: {file_id}")
        msg["Subject"] = "Telegram bot video"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

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


@bot.message_handler(content_types=['video', 'document'])
def get_video(message):
    chat_id = message.chat.id
    name = user_name.get(chat_id, "неизвестно")

    file_id = None

    if message.content_type == "video":
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    success = send_email(name, file_id)

    if success:
        bot.send_message(chat_id, "Видео отправлено")
    else:
       э bot.send_message(chat_id, "Ошибка отправки")


if __name__ == "__main__":
    bot.infinity_polling()
