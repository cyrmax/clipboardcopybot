import configparser
import json
import sys
from time import time
import winsound

import clipboard
import telebot
from telebot import types

config = configparser.ConfigParser()
config.read("config.ini")
if not config.has_section("bot"):
    sys.exit("please, create config file \"config.ini\" before running the program")

startTime = time() if not config.getboolean("bot", "handle_offline_messages") else 0

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
