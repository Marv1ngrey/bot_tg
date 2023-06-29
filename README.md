# bot_tg
Простой бот для голосования в публичных тг каналах. 
  1 бот (bot.py) работает по заданным в ручную пораметрам (ссылка на канал, чат, сообщение, вариант ответа)
  2 бот (bot(bop).py) работает проще, вы пересылаете ему голосование и отправляете правильный вариант ответа и он сам уже голосует, если вы отправите ему голосование которого уже нету, то он просто вам вадаст ошибку.
  Для того, чтобы бот начал работать достаточно заменить YOUR_BOT_TOKEN на токен вашего бота и запустит программу. Емли будут вопросы, гугл в помощь)

# пояснения по второму файлу
 в данном коде предусмотрены две команды для работы с ботом: /forward_poll и /vote.

Команда /forward_poll позволяет пересылать опросы из одного чата в другой. Для того чтобы воспользоваться этой командой, вам нужно написать в чат, где находится ваш бот, следующее сообщение:

/forward_poll <channel_id> <message_id>

где channel_id - это идентификатор канала, из которого вы хотите переслать опрос, а message_id - это идентификатор сообщения с опросом в этом канале.

Например, если вы хотите переслать опрос из канала с идентификатором @my_channel и идентификатором сообщения 123, вы можете написать следующее сообщение в чат:

/forward_poll @my_channel 123

Бот перешлет этот опрос в текущий чат.

Команда /vote позволяет проголосовать в опросе. Для этого вам нужно написать в чат, где находится ваш бот, следующее сообщение:

/vote <option_id>

где option_id - это идентификатор варианта ответа в опросе, за который вы хотите проголосовать.

Например, если в опросе есть три варианта ответа с идентификаторами 1, 2 и 3, и вы хотите проголосовать за вариант 2, вы можете написать следующее сообщение в чат:

/vote 2

Бот отправит ваш голос в опросе.

Надеюсь, это помогло вам понять, как использовать этот бот. Если у вас есть дополнительные вопросы, не стесняйтесь задавать их.
