import telebot

# import sticker

bot = telebot.TeleBot('')


# Отслеживание команд
@bot.message_handler(commands=['start','sticker','video'])
def start_message(message):
    mass = f'Привет,<b>{message.from_user.first_name} {message.from_user.last_name}</b> попробуй "test" или "video"'  # .format(message.from_user,bot.get_me())
    bot.send_message(message.chat.id, mass, parse_mode='html')
    sti = 'CAACAgIAAxkBAAEGNvBjWnimnAVWFbVj1Y6LR4JyWTaM4QACOwMAAm2wQgMDgo__5XFPdSoE'
    bot.send_sticker(message.chat.id, sti)


@bot.message_handler(content_types=["text", "sticker", "video"])
def ww(message):
    if message.text == 'test':
        stir = 'CAACAgIAAxkBAAEGNvJjWnjPZJpTS3i72t01g_BxisxYPQACRwMAAm2wQgNSVSv5NcWAgioE'
        # sti = open('sticker.webm', 'rb')
        bot.send_sticker(message.chat.id, stir)

    elif message.text == 'video':
        video = 'ssstwitter.com_1664785349211.mp4'
        bot.send_video(message.chat.id, video)
    else:
        mass = f'Пиши правильно <b>{message.from_user.first_name} </b>  "test" '
        bot.send_message(message.chat.id, mass, parse_mode='html')

bot.polling(non_stop=True)
