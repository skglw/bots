import telebot, random, sqlite3
from random import randrange

db = sqlite3.connect('pity.db', check_same_thread = False)
sql = db.cursor()
bot = telebot.TeleBot('6407657113:AAEFy9vSRJ7cVsFFXNsjsRQSLbiEElLCAfc')

def get_sticker():
    id = randrange(28)
    sql.execute(f"SELECT tg_id FROM stickers WHERE id = {id}")
    sticker = sql.fetchone()
    return sticker[0]

def get_message():
    id = randrange(4)
    sql.execute(f"SELECT phrase FROM replies WHERE id = {id}")
    reply = sql.fetchone()
    return reply

def is_im_alone(message):
    sql.execute(f"SELECT id FROM im_alone WHERE phrase = '{message}'")
    if sql.fetchone() is None:
        return False
    else:
        return True

def is_whos_alone(message):
    sql.execute(f"SELECT id FROM whos_alone WHERE phrase = '{message}'")
    if sql.fetchone() is None:
        return False
    else:
        return True
    
def is_user_alone(message):
    message = message.lower()
    
    if is_im_alone(message):
        return {'res': True, 'mes': get_message(), 'pic': get_sticker()}
    
    elif is_whos_alone(message):
        return {'res': True, 'mes': 'никто не один бро', 'pic': get_sticker()}
    
    elif message == 'я не один?' or message == 'я не один??' or message == 'я не один' or message == 'я не один.':
        return {'res': True, 'mes': 'да бро ты не один', 'pic': get_sticker()}
    
    elif message == 'я не одна?' or message == 'я не одна??' or message == 'я не одна' or message == 'я не одна.':
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