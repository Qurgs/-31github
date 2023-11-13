import telebot
from datetime import datetime

# Замените 'YOUR_TOKEN' на реальный токен вашего бота
TOKEN = '6461060704:AAHT6X2eWVVD51eNp95TKwUcIdM6aRXW6yk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для отчетов. Просто отправь мне информацию о заданиях.")

@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup', content_types=['text'])
def process_report(message):
    try:
        chat_id = message.chat.id
        user_info = message.text.split('\n')[1:-1]  # Информация о пользователях
        total_tasks = int(user_info[-1].split()[-1])  # Общее количество заданий

        report = f"Отчет\n{datetime.now().strftime('%d.%m.%y')}\n"

        for user_data in user_info:
            user_data = user_data.strip()
            if user_data.startswith("#"):
                user_id = user_data[1:]
                continue

            if user_data:  # Пропускаем пустые строки
                report += f"#{user_id} {user_data}\n"

        report += f"Количество стаж заданий ({total_tasks})"

        bot.send_message(chat_id, report)

    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
