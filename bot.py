
import random
import telebot
import config
import os
import io
from count import count
from citiestest import word
from rate import rate
from rename import rename
#count(str(message.chat.id), '.random')

random.seed()
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    #bot.send_message(message.chat.id, "Команды, поддерживаемые ботом: \n /help \n /reset \n /report_exist \n /report_unexist \nДля начала игры отправь любое слово")
    q = io.open('word/rating/players.txt', 'r', encoding='utf-8')
    text3 = q.read()
    c3 = text3.count(str(message.chat.id))
    q.close()
    if c3 == 0:
         bot.send_message(message.chat.id, "Позволь сначала узнать твой ник (необходимо для формирования рейтинговой таблицы)")
         q1 = io.open('word/'+str(message.chat.id)+'R.txt', 'w', encoding='utf-8')
         q1.write('1')
         q1.close()
    else:
         bot.send_message(message.chat.id, "Для вызова справки отправь мне команду /help \nДля начала игры отправь любое слово")
    count(str(message.chat.id), '.start')
    return

@bot.message_handler(commands=['rename'])
def handle_rename(message):
    q = io.open('word/rating/players.txt', 'r', encoding='utf-8')
    text4 = q.read()
    c3 = text4.count(str(message.chat.id))
    q.close()
    if c3 == 0:
        bot.send_message(message.chat.id, "Ты ещё не вводил свой ник. Самое время! Как назовёшь себя?")
    else:
        bot.send_message(message.chat.id, "Введи новый ник\nЕсли передумаешь менять ник, нажми /cancel")
    q1 = io.open('word/'+str(message.chat.id)+'.entering_name.txt', 'w', encoding='utf-8')
    q1.write('1')
    q1.close()  
    return

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Это бот для игры в слова. Для начала игры просто напиши любое слово. Если ты нашёл ошибку - напиши @Vertonger.\nДля сброса игры нажми /reset\nДля вывода рейтинга нажми /rating\nДля смены ника нажми /rename \nЧтобы оповестить админа, что бот использует несуществующее слово, нажми /report_exist после этого слова \nЧтобы оповестить админа, что бот не знает слова, которое ты ему отправил, нажми /report_unexist после отправки слова \n\n\nПриятной игры! ")
    count(str(message.chat.id), '.help')
    return

@bot.message_handler(commands=['rating'])
def handle_rating(message):
    rate()
    f = io.open('word/rating/rating.txt', 'r', encoding='utf-8')
    rating = f.read()
    f.close()
    bot.send_message(message.chat.id, rating)
    count(str(message.chat.id), '.rating')
    return

@bot.message_handler(commands=['reset'])
def handle_reset(message):
    bot.send_message(message.chat.id, "Игра началась заново, называй слово")
    s1 = io.open('word/'+str(message.chat.id)+'.txt', 'w', encoding='utf-8')
    s1.write(' ')
    s1.close()
    s2 = io.open('word/'+str(message.chat.id)+'LAST.txt', 'w', encoding='utf-8')
    s2.write(' ')
    s2.close()
    os.remove('word/'+str(message.chat.id)+'.txt')
    os.remove('word/'+str(message.chat.id)+'LAST.txt')
    count(str(message.chat.id), '.reset')
    return

@bot.message_handler(commands=['report_exist'])
def handle_report_existe(message):
    bot.send_message(message.chat.id, "Спасибо за помощь! Чтобы изменения вступили в силу, нужно время на модерацию. \nПока можешь продолжить игру")
    s1 = io.open('word/'+str(message.chat.id)+'LAST.txt', 'r', encoding='utf-8')
    text = s1.read()
    s1.close()
    e1 = io.open('reports/exist.txt', 'a', encoding='utf-8')
    e1.write(str(message.chat.id)+':\n'+text+'\n')
    e1.close()
    count(str(message.chat.id), '.report.exist')
    return

@bot.message_handler(commands=['report_unexist'])
def handle_report_unexiste(message):
    bot.send_message(message.chat.id, "Спасибо за помощь! \nЧтобы изменения вступили в силу, нужно время на модерацию. \nПока можешь продолжить игру")
    s2 = io.open('word/'+str(message.chat.id)+'FOR.REPORT.txt', 'r', encoding='utf-8')
    text = s2.read()
    s2.close()
    e2 = io.open('reports/unexist.txt', 'a', encoding='utf-8')
    e2.write(str(message.chat.id)+':\n'+text+'\n')
    e2.close()
    count(str(message.chat.id), '.report.unexist')
    return

@bot.message_handler(commands=['cancel'])
def handle_cancel(message):
    if os.path.exists('word/'+str(message.chat.id)+'.entering_name.txt'):
        bot.send_message(message.chat.id, "Ник не изменился. Можешь продолжить игру")
        os.remove('word/'+str(message.chat.id)+'.entering_name.txt')
        count(str(message.chat.id), '.cancel')
    else:  bot.send_message(message.chat.id, "Нет действий для отмены")
    return

@bot.message_handler(content_types=["text"])
def play(message):
    if  os.path.exists('word/'+str(message.chat.id)+'R.txt'):
        q2 = io.open('word/rating/players.txt', 'a', encoding='utf-8')
        q2.write(str(message.text)+ ' = '+str(message.chat.id)+'\n')
        q2.close()
        os.remove('word/'+str(message.chat.id)+'R.txt')
        bot.send_message(message.chat.id, "А я Евпатий, рад знакомству. Для начала игры отправь любое слово, для вызова справки - отправь мне команду /help")
    elif os.path.exists('word/'+str(message.chat.id)+'.entering_name.txt'):
        rename(str(message.text), str(message.chat.id))
        os.remove('word/'+str(message.chat.id)+'.entering_name.txt')
        bot.send_message(message.chat.id, "Ник изменён! Можешь продолжить игру")
    else:
        bot.send_message(message.chat.id, word(message.text, message.chat.id))
        count(str(message.chat.id), '.word')
    return



if __name__ == '__main__':
    bot.polling(none_stop=True)