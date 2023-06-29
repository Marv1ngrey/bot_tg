import config
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# замените YOUR_BOT_TOKEN на токен вашего бота
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

def vote(bot, update):
    # сообщение отправьляем одно из 5 частей 1 - команда /vote, 2 - id канала (ссылка на вступление), 3 - айди чата этого канала, 4 - айди голосования, 5 - вариант за который нужно голосовать
    channel_id = update.message.text.split()[1]
    chat_id = update.message.text.split()[2]
    message_id = update.message.text.split()[3]
    option = update.message.text.split()[4]

    bot.join_chat(channel_id)
    bot.send_poll_answer(chat_id=chat_id, message_id=message_id, option_ids=[int(option)])


# замените YOUR_BOT_TOKEN на токен вашего бота
updater = Updater(token='YOUR_BOT_TOKEN')
vote_handler = CommandHandler('vote', vote)
updater.dispatcher.add_handler(vote_handler)
updater.start_polling()
updater.idle()
