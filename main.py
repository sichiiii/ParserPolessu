import telebot, os
from flask import Flask
from selen import Selen

bot = telebot.TeleBot('5138730854:AAGyih7KeGdZk4UcUvs93fganmbOs5oiCGw')
selen = Selen()

week_name, group_name = '0', '0'

@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.send_message(message.chat.id, 'Enter group or week')
    bot.register_next_step_handler(message, getMessage)

def getMessage(message):
    global week_name
    global group_name
    splited_message = message.text.split('-')
    if week_name == '0' or group_name == '0':
        print(splited_message[0][:2])
        if len(splited_message) == 2:
            if splited_message[0][:2].isnumeric() == True and splited_message[1].isnumeric() == True:
                group_name = message.text
                if week_name == '0':
                    bot.send_message(message.chat.id, 'Enter week: ')
                bot.register_next_step_handler(message, getMessage)
        elif len(splited_message) == 1:
            if splited_message[0].isnumeric() == True:
                week_name = message.text
                if group_name == '0':
                    bot.send_message(message.chat.id, 'Enter group: ')
                bot.register_next_step_handler(message, getMessage)
        else:
            bot.send_message(message.chat.id, 'Enter correct data!')
            bot.register_next_step_handler(message, getMessage)
    if week_name != '0' and group_name != '0':
        getScreen(week_name, group_name, message)
        week_name = '0' 
        group_name = '0'
        bot.register_next_step_handler(message, startMessage)
        

def getScreen(week_name, group_name, message):
    try:
        selen(week_name, group_name)
        bot.send_photo(message.chat.id, open('my_screenshot.png', 'rb'))
    except Exception as ex:
        print(str(ex))
        bot.send_message(message.chat.id, 'Oops! Something went wrong! Try another group or week: /start')

server = Flask(__name__)

@server.route("/bot", methods=['POST'])
def bot_route():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.polling(none_stop=True)
    return "?", 200
server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
