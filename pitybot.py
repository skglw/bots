import telebot, random
bot = telebot.TeleBot('6407657113:AAEFy9vSRJ7cVsFFXNsjsRQSLbiEElLCAfc')

def get_sticker():
    stickers = [
        'CAACAgQAAxkBAAI4pGTB3K5fVGRx6-fd87OSbYXHpmhOAALBCwACSl-wUS7YsVA34l0hLwQ',
        'CAACAgQAAxkBAAI4pmTB3LMhnGnPvfEI7dRu2O0Ky5oVAAIiHQACUX0AAVBvNmHdUFijpS8E',
        'CAACAgQAAxkBAAI4qGTB3L-FRHMzc6H91IgOJVlbmKDlAALoCQACbQXpU3f0VcR0LKO4LwQ',
        'CAACAgQAAxkBAAI4qmTB3MqqUkXh5DJ-9JOjsMmTPFLZAAJXDAAC9qA4UvIEg365VMTtLwQ',
        'CAACAgIAAxkBAAI4rGTB3Nezqi4CybL0TYof81Ecd1-HAAJPHgACty44SFroRkiEtWuELwQ',
        'CAACAgIAAxkBAAI4rmTB3NpQjPaylq-2eNw9SEkwG7KhAAKBGwAC6WBBSMRU1kCjzsQ2LwQ',
        'CAACAgIAAxkBAAI4sGTB3PDvWcVP0nMMMc3Q3jZCTg8LAAL-FQACuKEoSKVpjcntejS8LwQ',
        'CAACAgIAAxkBAAI4smTB3PFx2SZMQ3MbnIg8Yiq6F-zNAAKKEwACuFwpSH8mgDz9uZaELwQ',
        'CAACAgIAAxkBAAI4tGTB3PnM1jNBaAYaLVdLJtOEjSdeAAItGgACO6ohSKWKglzs4mm-LwQ',
        'CAACAgIAAxkBAAI4uGTB3RLluHvrSBQquqsuaWiDExhoAAKPGAACC6z4SwAByuVFguHK0i8E',
        'CAACAgIAAxkBAAI4umTB3RmJ1RujXy1BdJXIQxB0xGX_AAKxFAACtFn5S2z5-pyuAoHGLwQ',
        'CAACAgIAAxkBAAI4vGTB3SLtiDpaaYgfBCD6HTJdz6rlAAJeGQAC9NxoSASxw0lAvIJQLwQ',
        'CAACAgIAAxkBAAI4vmTB3TJF6c5PTszPlNyCwUqn703LAAKEEwACOW7JS2ZVTlSwaykPLwQ',
        'CAACAgIAAxkBAAI4wGTB3TRGoawqDHGvv6OY5jqvpBwUAALtEgACgCTIS7ELWSqTwy0YLwQ',
        'CAACAgIAAxkBAAI4wmTB3UTLatuNIkF3HzHPko2vM3iEAALzFwACqkdJSC8ry4607EHCLwQ',
        'CAACAgIAAxkBAAI4xGTB3Uo0Mh-lrITWoOE2oBq6HX-YAAKMFAACGndJSHhnyYts9sZYLwQ'
    ]
    return random.choice(stickers)
def get_message():
    messages = [
        'нет мы все вместе',
        'нет бро мы с тобой',
        'нет мы все тоже'
    ]
    return random.choice(messages)

def is_user_alone(message):
    message = message.lower()
    im_alone = [
        'я один',
        'я один?',
        'я один??',
        'я один..?',
        'я один?..',
        'я одна',
        'я одна?',
        'я одна??',
        'я одна..?',
        'я одна?..',
        'интересно один ли я',
        'интересно я один',
        'интересно я один?',
        'интересно я один??',
        'интересно я один?..',
        'интересно одна ли я',
        'интересно я одна',
        'интересно я одна?',
        'интересно я одна??',
        'интересно я одна?..'
    ]
    if message in im_alone:
        return {'res': True, 'mes': get_message(), 'pic': get_sticker()}
    
    elif message == '/кто один' or message == 'кто один?'or message == 'кто один':
        return {'res': True, 'mes': 'никто не один бро', 'pic': get_sticker()}
    
    elif message == 'я не один?' or message == 'я не один??':
        return {'res': True, 'mes': 'да бро ты не один', 'pic': get_sticker()}
    
    elif message == 'я не одна?' or message == 'я не одна??':
        return {'res': True, 'mes': 'да любимка ты не одна', 'pic': get_sticker()}
    
    else:
        return {'res': False}

@bot.message_handler(content_types=["text"])
def handle_text(message):
    is_alone = is_user_alone(message.text)
    if is_alone['res']:
        bot.reply_to(message, is_alone['mes'])
        bot.send_sticker(message.chat.id, is_alone['pic'])

bot.polling(none_stop=True, interval=0)