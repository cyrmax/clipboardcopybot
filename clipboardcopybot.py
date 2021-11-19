import telebot
from telebot import types
from time import time
import clipboard
import winsound
import configparser
import json

startTime = time()
config = configparser.ConfigParser()
config.read("config.ini")

usernames = []
usernames.append(config.get("bot", "username"))
usernames += json.loads(config.get("bot", "additionalUsers"))

bot = telebot.TeleBot(config.get("bot", "token"))

@bot.message_handler(content_types=["text"])
def getTextMessage(message):
  if message.date < startTime: return
  if message.from_user.username in usernames:
    clipboard.copy(message.text)
    winsound.PlaySound("sounds/copied.wav", winsound.SND_FILENAME)
    bot.send_message(message.from_user.id, "Copied!")


bot.polling(non_stop=True)