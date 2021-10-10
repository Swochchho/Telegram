import telebot

API_Key = "2020906583:AAEU3u405rf6MwrF_blHQbkFTaUlM3DbCdU"
bot = telebot.TeleBot(API_Key)

@bot.message_handler(commands=['hey', 'Hey'])
def greet(message):
    bot.send_message(message.chat.id, "Whats updog?")

@bot.message_handler(commands=['WhoRU', 'whoRU'])
def Who(message):
    bot.send_message(message.chat.id, "I am Prison Mike!")

@bot.message_handler(commands=['run', 'Run'])
def run(message):
    bot.send_message(message.chat.id, "Shatatatatata")

@bot.message_handler(commands=['fight', 'Fight'])
def run(message):
    bot.send_message(message.chat.id, "I know tons of 14 year old girl who can beat you")

bot.polling()
