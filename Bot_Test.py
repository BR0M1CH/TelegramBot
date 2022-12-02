import telebot
import requests
import time 
import json

bot_token = '5860981337:AAFBshSLiRCdMPkYwqKgZd5oYf3VB0IpGtc'

api = 'BwkihOWSNtBL91h3fWKRIN6l4BBa5YQI'

params = {"api_key" : api, "raiting":"r"}

bot = telebot.TeleBot(bot_token)

def logging(message,res):
    passer = 0
    log = {}
    try:
        with open("Logs.json", "r") as r:
            log_1=json.load(r)
    except:
            log_1={}
    user = str(message.from_user.id)
    timenow = time.ctime(time.time())
    log[user]={timenow : {message.text : res}}
    print("LOG", log)
    if user in log_1:
        log_1[user].update(log[user])
    else:
        log_1.update(log)
    print(log_1)
    with open("Logs.json", "w") as w:
        json.dump(log_1, w, indent=4) 

@bot.message_handler(commands=["start"])
def starter(message):
    params = {"api_key" : api, "raiting":"r", "s" : "hello"}
    res = requests.get("http://api.giphy.com/v1/gifs/translate", params=params).json()
    logging(message, res["data"]["images"]["original"]["url"])
    bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])
    bot.send_message(message.chat.id, text=f"Приветствую, {message.from_user.first_name}\n Введите /info чтобы получить мануал")

@bot.message_handler(commands=["info"])
def info(message):
    logging(message, "/find text - кидаю самую релевантную гифку \n/random - кидаю рандомную гифку\n/randtxt text - кидаю рандомную гифку по названию")
    bot.send_message(message.chat.id, text = "/find text - кидаю самую релевантную гифку \n/random - кидаю рандомную гифку\n/randtxt text - кидаю рандомную гифку по названию")


@bot.message_handler(commands=["find"])
def find(message):
    try:
        text = message.text.split(maxsplit = 1)[1]
        params = {"api_key" : api, "raiting":"r", "s" : text}
        res = requests.get("http://api.giphy.com/v1/gifs/translate", params=params).json()
        logging(message, res["data"]["images"]["original"]["url"])
        bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])
    except:
        logging(message, "Упс... Такой гифки у меня нет :(")
        bot.send_message(message.chat.id, "Упс... Такой гифки у меня нет :(")

@bot.message_handler(commands=["random"])
def random(message):
    params = {"api_key" : api, "raiting":"r"}
    res = requests.get("http://api.giphy.com/v1/gifs/random", params=params).json()
    logging(message, res["data"]["images"]["original"]["url"])
    bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])

@bot.message_handler(commands = ["randtxt"])
def randtxt(message):
    try:
        text = message.text.split(maxsplit=1)[1]
        params = {"api_key" : api, "raiting":"r", "tag" : text}
        res = requests.get("http://api.giphy.com/v1/gifs/random", params=params).json()
        logging(message, res["data"]["images"]["original"]["url"])
        bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])
    except:
        logging(message, "Упс... Такой гифки у меня нет :(")
        bot.send_message(message.chat.id, "Упс... Такой гифки у меня нет :(")







bot.polling()