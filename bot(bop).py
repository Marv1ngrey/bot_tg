import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# замените YOUR_BOT_TOKEN на токен вашего бота
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

def forward_poll(bot, update):
    channel_id = update.message.text.split()[1]
    message_id = update.message.text.split()[2]

    forwarded_message = bot.forward_message(chat_id=update.message.chat_id, from_chat_id=channel_id, message_id=message_id)
    poll_message_id = forwarded_message.message_id

    if 'votes' not in bot:
        bot['votes'] = {}
    bot['votes'][poll_message_id] = {'chat_id': update.message.chat_id, 'channel_id': channel_id}

def vote(bot, update):
    option = update.message.text.split()[1]
    poll_message_id = None

    for message_id, vote_data in bot.get('votes', {}).items():
        if vote_data['chat_id'] == update.message.chat_id:
            poll_message_id = message_id
            channel_id = vote_data['channel_id']
            break

    if poll_message_id is None:
        bot.send_message(chat_id=update.message.chat_id, text='Голосование не найдено.')
        return

    bot.send_chat_action(chat_id=channel_id, action=telegram.ChatAction.TYPING)
    bot.send_poll_answer(chat_id=channel_id, message_id=poll_message_id, option_ids=[int(option)])

updater = Updater(token='YOUR_BOT_TOKEN')
forward_poll_handler = CommandHandler('forward_poll', forward_poll)
vote_handler = MessageHandler(Filters.text, vote)

updater.dispatcher.add_handler(forward_poll_handler)
updater.dispatcher.add_handler(vote_handler)
updater.start_polling()
updater.idle()
