import telebot
from telebot import types
import requests
import time 
import json

try:
    with open("api.json", "r", encoding="utf-8") as file:
        bot_token = json.load(file)["gif_bot_api"]
    with open("api.json", "r", encoding="utf-8") as file:
        api = json.load(file)["giphy_api"]
except:
    print("Вставьте api вручную или создайте файл с такими же параметрами")

params = {"api_key" : api, "raiting":"r"}

bot = telebot.TeleBot(bot_token)

def logging(message,res):
    passer = 0
    log = {"gif": {}}
    try:
        with open("Logs.json", "r") as r:
            log_1=json.load(r)
    except:
            log_1={"gif" : {}}
    user = str(message.from_user.id)
    timenow = time.ctime(time.time())
    log["gif"][user]={timenow : {message.text : res}}
    if user in log_1["gif"]:
        log_1["gif"][user].update(log["gif"][user])
    else:
        log_1.update(log)
    with open("Logs.json", "w") as w:
        json.dump(log_1, w, indent=4) 

@bot.message_handler(commands=["start"])
def starter(message):
    params = {"api_key" : api, "raiting":"r", "s" : "hello"}
    res = requests.get("http://api.giphy.com/v1/gifs/translate", params=params).json()
    logging(message, res["data"]["images"]["original"]["url"])
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Рандомная гиф")
    btn2 = types.KeyboardButton("Гиф по тегу")
    btn3 = types.KeyboardButton("Рандомная гиф по тегу")
    btn4 = types.KeyboardButton("Список команд")
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])
    bot.send_message(message.chat.id, text=f"Приветствую, {message.from_user.first_name}", reply_markup=kb)
    



@bot.message_handler(content_types=["text"])

def func(message):
    if message.text == "Гиф по тегу":
        sent = bot.send_message(message.chat.id, text="Введите тег")
        logging(message, "Введите тег")
        bot.register_next_step_handler(sent, gif_tag)
    
    elif message.text == "Рандомная гиф по тегу":
        sent = bot.send_message(message.chat.id, "Введите тег")
        logging(message, "Введите тег")
        bot.register_next_step_handler(sent, gif_rand_tag)

    elif message.text == "Рандомная гиф":
        params = {"api_key" : api, "raiting":"r"}
        res = requests.get("http://api.giphy.com/v1/gifs/random", params=params).json()
        logging(message, res["data"]["images"]["original"]["url"])
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В начало")
        kb.add(btn1)
        bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"], reply_markup=kb)

    elif message.text == "Список команд":
        logging(message, "Гайд")
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В начало")
        kb.add(btn1)
        bot.send_message(message.chat.id, text = "Гиф по тегу - кидаю самую релевантную гифку \nРандомная гиф - кидаю рандомную гифку\nРандомная гиф по тегу - кидаю рандомную гифку по названию", reply_markup=kb)

    elif message.text == "В начало":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Рандомная гиф")
        btn2 = types.KeyboardButton("Гиф по тегу")
        btn3 = types.KeyboardButton("Рандомная гиф по тегу")
        btn4 = types.KeyboardButton("Список команд")
        kb.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Выберите команду", reply_markup=kb)

def gif_rand_tag(message):
    params = {"api_key" : api, "raiting":"r", "tag" : message.text}
    res = requests.get("http://api.giphy.com/v1/gifs/random", params=params).json()
    logging(message, res["data"]["images"]["original"]["url"])
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("В начало")
    kb.add(btn1)
    bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"], reply_markup=kb)

def gif_tag(message):
    params = {"api_key" : api, "raiting":"r", "s" : message.text}
    res = requests.get("http://api.giphy.com/v1/gifs/translate", params=params).json()
    logging(message, res["data"]["images"]["original"]["url"])
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("В начало")
    kb.add(btn1)
    bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"], reply_markup=kb)
















# @bot.message_handler(commands=["info"])
# def info(message):
#     logging(message, "/find text - кидаю самую релевантную гифку /random - кидаю рандомную гифку /randtxt text - кидаю рандомную гифку по названию")
#     bot.send_message(message.chat.id, text = "/find text - кидаю самую релевантную гифку \n/random - кидаю рандомную гифку\n/randtxt text - кидаю рандомную гифку по названию")


# @bot.message_handler(commands=["find"])
# def find(message):
#     try:
#         text = message.text.split(maxsplit = 1)[1]
#         params = {"api_key" : api, "raiting":"r", "s" : text}
#         res = requests.get("http://api.giphy.com/v1/gifs/translate", params=params).json()
#         logging(message, res["data"]["images"]["original"]["url"])
#         bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])
#     except:
#         logging(message, "Упс... Такой гифки у меня нет :(")
#         bot.send_message(message.chat.id, "Упс... Такой гифки у меня нет :(")

# @bot.message_handler(commands=["random"])
# def random(message):
#     params = {"api_key" : api, "raiting":"r"}
#     res = requests.get("http://api.giphy.com/v1/gifs/random", params=params).json()
#     logging(message, res["data"]["images"]["original"]["url"])
#     bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])

# @bot.message_handler(commands = ["randtxt"])
# def randtxt(message):
#     try:
#         text = message.text.split(maxsplit=1)[1]
#         params = {"api_key" : api, "raiting":"r", "tag" : text}
#         res = requests.get("http://api.giphy.com/v1/gifs/random", params=params).json()
#         logging(message, res["data"]["images"]["original"]["url"])
#         bot.send_video(message.chat.id, res["data"]["images"]["original"]["url"])
#     except:
#         logging(message, "Упс... Такой гифки у меня нет :(")
#         bot.send_message(message.chat.id, "Упс... Такой гифки у меня нет :(")







bot.polling()