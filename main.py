import.os
import telebot

bot =telebot.Telebot("5004453399:AAEdu0ltefjVzehpriBSgaUos6TnmU73_Ds")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello I'am Gimhan Geek Chat Bot")

@bot.message_handler(commands="How")
def send_message(message):
    bot.send_message(message, "htps://youtube.com/c/GimhanGeek")

bot.polling() 