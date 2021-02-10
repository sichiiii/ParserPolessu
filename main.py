import telebot, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.options import Options 

bot = telebot.TeleBot('1605853735:AAGYGN3uWIGJO4MY3vCTMX1qnAjNL80U8UY')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
bot.polling(none_stop=True, interval=0)
