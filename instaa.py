import telebot
import api
import os
import instaloader
from PIL import Image

test = instaloader.Instaloader()
API_KEY = api.apireturn()
bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello ...\nEnter the user account")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
        acc = message.text
        test.download_profile(acc, profile_pic_only=True)
        path = (os.path.join(os.getcwd(), acc))
        for i in os.listdir(path):
            if "jpg" in i or "jpeg" in i:
                path = os.path.join(path, i)
                break
        im = Image.open(path)
        bot.send_photo(message.chat.id, im, "Profile picture")

bot.polling()
