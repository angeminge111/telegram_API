# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import time
import requests
from PIL import Image
import random

# Определяем функцию-обработчик сообщений.
# У нее два параметра, сам бот и класс updater, принявший сообщение.
def help(bot, updater):
    updater.message.reply_text('Здравствуйте и спасибо за то, что Вы зашли ко мне!\n'
                               ' Ведь если Вы здесь и читаете этот текст, значит,\n'
                               ' Вы неравнодушны к моиму труду,\n'
                                'а это очень много. Потому что проблемы решаются,\n'
                                ' мир устанавливается и жизнь \n'
                                   'продолжается только благодаря неравнодушным людям — \n'
                               'таким как Вы! \n'
                               'Ниже вы можите увидеть все мои функции:\n'
                                'Так же хочу сказать, что я ещё \n'
                                'развиваюсь, и не стоит судить строго', reply_markup=markup)

def trans(bot, updater, user_data):
    newFile = bot.get_file(updater.message['photo'][-1]['file_id'])
    newFile.download('11.jpg')
    print(newFile)
    newFile = bot.get_file(updater.message['photo'][-3]['file_id'])
    newFile.download('111.jpg')
    newFile = bot.get_file(updater.message['photo'][-2]['file_id'])
    newFile.download('123.jpg')
    updater.message.reply_text('Что ты хочешь?\n'
                               'если ты хочешь объеденить нажми объеденить после каждого добавления фото', reply_markup=markup)


def obmen(bot, updater):
    updater.message.reply_text('Одна из ваших фотографий поступила на обработку \n'
                               'Для совмещения нужно две :)\n'
                               'После отправления второй фотографии нажми /Obedinenie')

    im = Image.open("11.jpg")
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = r,g,b
    im.save('1234.jpg')

def Obedinenie(bot, updater):
    updater.message.reply_text('Вторая твоя фоторгафия поступила на обработку:)\n'
                               'Эта функция пока не работает ')
    im = Image.open("11.jpg")
    ik = Image.open("1234.jpg")
    x, y = im.size  # ширина (x) и высота (y) изображения
    x1, y1 = ik.size
    print(x,x1,y,y1)
    if x > x1:
        if y > y1:
            for i in range(x1):
                for j in range(y1):
                    im = Image.open("11.jpg")
                    ik = Image.open("1234.jpg")
                    x, y = im.size  # ширина (x) и высота (y) изображения
                    x1, y1 = ik.size
                    r, g, b = pixels[i, j]
                    r2, g2, b2 = pixels2[i, j]
                    pixels[i, j] = int(r / 2 + r2 / 2), int(g / 2 + g2 / 2), int(b / 2 + b2 / 2)

            im.save('22.jpg')
            bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
            updater.message.reply_text('Спасибо за ожидание')
        else:
            for i in range(x1):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    r2, g2, b2 = pixels2[i, j]
                    pixels[i, j] = int(r / 2 + r2 / 2), int(g / 2 + g2 / 2), int(b / 2 + b2 / 2)
                im.save('22.jpg')
                bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
                updater.message.reply_text('Спасибо за ожидание')
    else:
        if y > y1:
            for i in range(x):
                for j in range(y1):
                    print('3')
                    r, g, b = pixels[i, j]
                    r2, g2, b2 = pixels2[i, j]
                    pixels[i, j] = int(r / 2 + r2 / 2), int(g / 2 + g2 / 2), int(b / 2 + b2 / 2)

            im.save('22.jpg')
            bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
            updater.message.reply_text('Спасибо за ожидание')
        else:
            for i in range(x):
                for j in range(y):
                    print('4')
                    r, g, b = pixels[i, j]
                    r2, g2, b2 = pixels2[i, j]
                    pixels[i, j] = int(r / 2 + r2 / 2), int(g / 2 + g2 / 2), int(b / 2 + b2 / 2)

            im.save('22.jpg')
            bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
            updater.message.reply_text('Спасибо за ожидание')



def Negativ(bot, updater):
    updater.message.reply_text('Ваша фотография поступила на обработку \n'
                               'Дождитесь ответа:)')
    im = Image.open('11.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = 255-r, 255-g, 255-b
    im.save('22.jpg')
    bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
    updater.message.reply_text('Спасибо за ожидание')


def CHB(bot, updater ):
    updater.message.reply_text('Ваша фотография поступила на обработку \n'
                               'Дождитесь ответа:)')
    im = Image.open('11.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            sym = (r + g + b)//3
            pixels[i, j] = sym, sym, sym
    im.save('22.jpg')
    bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
    updater.message.reply_text('Спасибо за ожидание')

def ping(bot, updater ):
    updater.message.reply_text('Ваша фотография поступила на обработку \n'
                               'Дождитесь ответа:)')
    im = Image.open('11.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = r+30, g, b+10
    im.save('22.jpg')
    bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
    updater.message.reply_text('Спасибо за ожидание')

def Sepia(bot, updater):
    updater.message.reply_text('Ваша фотография поступила на обработку \n'
                               'Дождитесь ответа:)')
    im = Image.open('11.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            sym = (r + g + b) // 3
            pixels[i, j] = sym + 2*20, sym + 20, sym
    im.save('22.jpg')
    bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
    updater.message.reply_text('Спасибо за ожидание')


def Shum(bot, updater):


    updater.message.reply_text('Ваша фотография поступила на обработку \n'
                               'Дождитесь ответа:)')
    im = Image.open('111.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            rand = random.randint(-100, 100)
            r, g, b = pixels[i, j]
            pixels[i, j] = r + rand, g + rand, b + rand
    im.save('22.jpg')
    bot.send_photo(chat_id=updater.message.chat_id, photo=open('22.jpg', 'rb'))
    updater.message.reply_text('Спасибо за ожидание')



# Напишем соответствующие функции. Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def main():

    updater = Updater("561830471:AAG64nMhr9uaU7y1g5-x_y1hXPsgkoUFg_s")
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("Негатив", Negativ))
    dp.add_handler(CommandHandler("Ч/Б", CHB))
    dp.add_handler(CommandHandler("Сепия", Sepia))
    dp.add_handler(CommandHandler("Шум", Shum))
    dp.add_handler(CommandHandler('Розовый', ping))
    dp.add_handler(CommandHandler("Объединение", obmen))
    dp.add_handler(CommandHandler("Obedinenie", Obedinenie))
    dp.add_handler(MessageHandler(Filters.all, trans, pass_user_data=True))



    updater.start_polling()
    updater.idle()

reply_keyboard = [['/Негатив'],
                  ['/Ч/Б'],
                  ['/Сепия'],
                  ['/Шум'],
                  ['/Объединение'],
                  ['/Розовый']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
