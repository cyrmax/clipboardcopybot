from platform import win32_is_iot
import telebot
from telebot import types
from time import time
import clipboard
import winsound

startTime = time()

bot = telebot.TeleBot("")

@bot.message_handler(content_types=["text"])
def getTextMessage(message):
  if message.date < startTime: return
  if message.from_user.username in ["cyrmax", "daniil_savenya", "gumerov_amir"]:
    clipboard.copy(message.text)
    winsound.PlaySound("sounds/copied.wav", winsound.SND_FILENAME)
    bot.send_message(message.from_user.id, "Copied!")


bot.polling(non_stop=True)