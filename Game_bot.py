import telebot
from telebot import types
import random
import json
import time

message_to_edit = ""

try:
    with open ("api.json", "r", encoding="utf-8") as file:  #comment this 2 lines
        api = json.load(file)["game_bot_api"]               #for using your api
except:
    print("Добавьте вручную api или создайте файл с такими же конфигурациями")
gb_dict = {1:"🟦",2:"🟦",3:"🟦",4:"🟦",5:"🟦",6:"🟦",7:"🟦",8:"🟦",9:"🟦","X":"❌", "O":"⭕️"}
X_or_O = ["X", "O"]

player, boter = " ", " "
turn = 1
dif_lvl = 2

bot = telebot.TeleBot(api)                            #insert your api

def bot_rand(boter):
    global gb_list
    while True:
        try:
            a = random.choice(gb_list)
            if type(a) == int:
                gb_list[a-1] = boter
                return
            else:
                raise Exception
        except:
            pass


def bot_def_attack(mode):                                                       #atack or defence func for bot
    global gb_list, player, boter                                               #if mode == player - defence mode
    a = True                                                                    #if mode == boter - attack mode
    #first row
    if (gb_list[0] == mode) and (gb_list[1] == mode) and (type(gb_list[2]) == int):
        gb_list[2] = boter
    elif (gb_list[0] == mode) and (gb_list[2] == mode) and (type(gb_list[1]) == int):
        gb_list[1] = boter
    elif (gb_list[1] == mode) and (gb_list[2] == mode) and (type(gb_list[0]) == int):
        gb_list[0] = boter
    #second row
    elif (gb_list[3] == mode) and (gb_list[4] == mode) and (type(gb_list[5]) == int):
        gb_list[5] = boter
    elif (gb_list[3] == mode) and (gb_list[5] == mode) and (type(gb_list[4]) == int):
        gb_list[4] = boter
    elif (gb_list[4] == mode) and (gb_list[5] == mode) and (type(gb_list[3]) == int):
        gb_list[3] = boter
    #third row
    elif (gb_list[6] == mode) and (gb_list[7] == mode) and (type(gb_list[8]) == int):
        gb_list[8] = boter
    elif (gb_list[6] == mode) and (gb_list[8] == mode) and (type(gb_list[7]) == int):
        gb_list[7] = boter
    elif (gb_list[7] == mode) and (gb_list[8] == mode) and (type(gb_list[6]) == int):
        gb_list[6] = boter
    #first column
    elif (gb_list[0] == mode) and (gb_list[3] == mode) and (type(gb_list[6]) == int):
        gb_list[6] = boter
    elif (gb_list[0] == mode) and (gb_list[6] == mode) and (type(gb_list[3]) == int):
        gb_list[3] = boter
    elif (gb_list[3] == mode) and (gb_list[6] == mode) and (type(gb_list[0]) == int):
        gb_list[0] = boter
    #second column
    elif (gb_list[1] == mode) and (gb_list[4] == mode) and (type(gb_list[7]) == int):
        gb_list[7] = boter
    elif (gb_list[1] == mode) and (gb_list[7] == mode) and (type(gb_list[4]) == int):
        gb_list[4] = boter
    elif (gb_list[4] == mode) and (gb_list[7] == mode) and (type(gb_list[1]) == int):
        gb_list[1] = boter
    #third column
    elif (gb_list[2] == mode) and (gb_list[5] == mode) and (type(gb_list[8]) == int):
        gb_list[8] = boter
    elif (gb_list[2] == mode) and (gb_list[8] == mode) and (type(gb_list[5]) == int):
        gb_list[5] = boter
    elif (gb_list[5] == mode) and (gb_list[8] == mode) and (type(gb_list[2]) == int):
        gb_list[2] = boter
    #main diagonal
    elif (gb_list[0] == mode) and (gb_list[4] == mode) and (type(gb_list[8]) == int):
        gb_list[8] = boter
    elif (gb_list[0] == mode) and (gb_list[8] == mode) and (type(gb_list[4]) == int):
        gb_list[1] = boter
    elif (gb_list[4] == mode) and (gb_list[8] == mode) and (type(gb_list[0]) == int):
        gb_list[0] = boter
    #secondary diagonal
    elif (gb_list[2] == mode) and (gb_list[4] == mode) and (type(gb_list[6]) == int):
        gb_list[6] = boter
    elif (gb_list[2] == mode) and (gb_list[6] == mode) and (type(gb_list[4]) == int):
        gb_list[4] = boter
    elif (gb_list[4] == mode) and (gb_list[6] == mode) and (type(gb_list[2]) == int):
        gb_list[2] = boter
    else:
        a = False
    return(a)
    


def bot_medium(boter):                              #medium bot can do 3 things: attack, defend, random
    global player, gb_list
    if bot_def_attack(boter) == True:
        return
    elif bot_def_attack(player) == True:
        return
    else:
        bot_rand(boter)
        return


def bot_hard(boter):                                #hard bot thinks about his first 3 steps, after that he will attack and defend               
    global player, gb_list,turn                     #if situation allows it, else he will random his step
    if turn == 1:
        gb_list[4] = boter
    elif turn == 2:
        if gb_list[4] == player:
            gb_list[random.choice([0, 2, 6, 8])] = boter
        elif (gb_list[0] == player):
            gb_list[2] = boter
        elif (gb_list[2] == player):
            gb_list[4] = boter
        elif (gb_list[6] == player):
            gb_list[3] = boter
        elif (gb_list[8] == player):
            gb_list[5] = boter
        elif (gb_list[1] == player):
            gb_list[4] = boter
        elif (gb_list[3] == player):
            gb_list[4] = boter
        elif (gb_list[5] == player):
            gb_list[4] = boter
        elif (gb_list[7] == player):
            gb_list[4] = boter
    elif turn == 3:
        if gb_list[1] == player:
            gb_list[2] = boter
        elif gb_list[3] == player:
            gb_list[6] = boter
        elif gb_list[5] == player:
            gb_list[2] = boter
        elif gb_list[7]:
            gb_list[6] = boter
        elif gb_list[6] != player:
            gb_list[6] = boter
        else:
            gb_list[2] = boter
    else:
        if bot_def_attack(boter) == True:
            return
        elif bot_def_attack(player) == True:
            return
        else:
            bot_rand(boter)
            return

            
def btn_place():
    gb = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton(text = gb_dict[gb_list[0]], callback_data=gb_list[0])
    btn2 = types.InlineKeyboardButton(text = gb_dict[gb_list[1]], callback_data=gb_list[1])
    btn3 = types.InlineKeyboardButton(text = gb_dict[gb_list[2]], callback_data=gb_list[2])
    btn4 = types.InlineKeyboardButton(text = gb_dict[gb_list[3]], callback_data=gb_list[3])
    btn5 = types.InlineKeyboardButton(text = gb_dict[gb_list[4]], callback_data=gb_list[4])
    btn6 = types.InlineKeyboardButton(text = gb_dict[gb_list[5]], callback_data=gb_list[5])
    btn7 = types.InlineKeyboardButton(text = gb_dict[gb_list[6]], callback_data=gb_list[6])
    btn8 = types.InlineKeyboardButton(text = gb_dict[gb_list[7]], callback_data=gb_list[7])
    btn9 = types.InlineKeyboardButton(text = gb_dict[gb_list[8]], callback_data=gb_list[8])
    gb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    return(gb)


def bot_turn(boter):
    global gb_list, turn, dif_lvl
    if dif_lvl == 1:
        bot_rand(boter)
        return
    elif dif_lvl == 2:
        bot_medium(boter)
        return
    elif dif_lvl == 3:
        bot_hard(boter)
        return
    

def check_win(callback):                                            #every step checks board to one WIN line
    global gb_list, turn
    log_dic = {1:"easy", 2:"medium", 3:"hard"}
    a = None
    if gb_list[0]==gb_list[1]==gb_list[2]:
        a = gb_list[0]
    elif gb_list[3]==gb_list[4]==gb_list[5]:
        a = gb_list[3]
    elif gb_list[6]==gb_list[7]==gb_list[8]:
        a = gb_list[6]
    elif gb_list[0]==gb_list[3]==gb_list[6]:
        a = gb_list[0]
    elif gb_list[1]==gb_list[4]==gb_list[7]:
        a = gb_list[1]
    elif gb_list[2]==gb_list[5]==gb_list[8]:
        a= gb_list[2]
    elif gb_list[0]==gb_list[4]==gb_list[8]:
        a= gb_list[0]
    elif gb_list[2]==gb_list[4]==gb_list[6]:
        a = gb_list[2]
    elif turn == 10: 
        log = {"game" : {}}
        try:
            with open("Logs.json", "r") as r:
                log_1=json.load(r)
        except:
                log_1={"game" : {}}
        user = str(callback.from_user.id)
        timenow = time.ctime(time.time())
        log["game"][user]={timenow : f"draw {log_dic[dif_lvl]}"}
        if user in log_1["game"]:
            log_1["game"][user].update(log["game"][user])
        else:
            log_1.update(log)
        with open("Logs.json", "w") as w:
            json.dump(log_1, w, indent=4)
        return("🎈Ничья!🎈")                               #if no WIN lines, but 9 steps of game were maden: draw
    if a == player: 
        log = {"game" : {}}
        try:
            with open("Logs.json", "r") as r:
                log_1=json.load(r)
        except:
                log_1={"game": {}}
        user = str(callback.from_user.id)
        timenow = time.ctime(time.time())
        log["game"][user]={timenow : f"win {log_dic[dif_lvl]}"}
        if user in log_1["game"]:
            log_1["game"][user].update(log["game"][user])
        else:
            log_1.update(log)
        with open("Logs.json", "w") as w:
            json.dump(log_1, w, indent=4)
        return("💥Вы выиграли!💥")
    elif a == boter: 
        log = {"game" : {}}
        try:
            with open("Logs.json", "r") as r:
                log_1=json.load(r)
        except:
                log_1={"game" : {}}
        user = str(callback.from_user.id)
        timenow = time.ctime(time.time())
        log["game"][user]={timenow : f" lose {log_dic[dif_lvl]}"}
        if user in log_1["game"]:
            log_1["game"][user].update(log["game"][user])
        else:
            log_1.update(log)
        with open("Logs.json", "w") as w:
            json.dump(log_1, w, indent=4)
        return("🎮Выиграл бот🎮")
    else: return(None)


@bot.message_handler(commands=["start"])
def start(message):
    regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
    regame.add(btn)
    bot.send_message(message.chat.id, text="Давай начнем!", reply_markup=regame)

@bot.message_handler(content_types=["text"])
def newgame(message):
    global gb_list, message_to_edit, boter, player, turn, dif_lvl
    if message.text == "🔄Начать новую игру🔄":
        gb_XO = ["X", "O"]
        player = random.choice(gb_XO)
        if player == "X": 
            bot.send_message(message.chat.id, text = "Вы начинаете за ❌")
            boter = "O"
        else: 
            bot.send_message(message.chat.id, text = "Вы играете за ⭕️, бот начинает")
            boter = "X"
        gb_list=[i for i in range(1, 10)]
        turn = 1
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        light = types.KeyboardButton(text = "⏬Легкий⏬")
        medium = types.KeyboardButton(text = "◀️Средний▶️")
        hard = types.KeyboardButton(text = "⏫Сложный⏫")
        kb.add(light, medium, hard)
        bot.send_message(message.chat.id, text = "Выберите уровень сложности", reply_markup=kb)
    elif message.text == "⏬Легкий⏬":
        dif_lvl=1
        if boter == "X":
            bot_turn(boter)
            turn+=1
            message_to_edit = bot.send_message(message.chat.id, text="Бот уже походил, твоя очередь", reply_markup=btn_place())
        else:
            message_to_edit = bot.send_message(message.chat.id, text="Начнем игру!", reply_markup=btn_place())
    elif message.text == "◀️Средний▶️":
        dif_lvl=2
        if boter == "X":
            bot_turn(boter)
            turn+=1
            message_to_edit = bot.send_message(message.chat.id, text="Бот уже походил, твоя очередь", reply_markup=btn_place())
        else:
            message_to_edit = bot.send_message(message.chat.id, text="Начнем игру!", reply_markup=btn_place())
    elif message.text == "⏫Сложный⏫":
        dif_lvl = 3
        if boter == "X":
            bot_turn(boter)
            turn+=1
            message_to_edit = bot.send_message(message.chat.id, text="Бот уже походил, твоя очередь", reply_markup=btn_place())
        else:
            message_to_edit = bot.send_message(message.chat.id, text="Начнем игру!", reply_markup=btn_place())
    else:
        regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
        regame.add(btn)
        bot.send_message(message.chat.id, text="Такой команды я не знаю", reply_markup=regame)



@bot.callback_query_handler(func = lambda callback: callback.data)
def callback_checker(callback):
    global message_to_edit, gb_dict, gb_list, player, boter, bot_list, turn
    
    if callback.data == "1":
        gb_list[0] = player
        turn +=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "2":
        gb_list[1] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "3":
        gb_list[2] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "4":
        gb_list[3] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "5":
        gb_list[4] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "6":
        gb_list[5] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "7":
        gb_list[6] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "8":
        gb_list[7] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "9":
        gb_list[8] = player
        turn+=1
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=btn_place())
        if check_win(callback) != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
        else:
            bot_turn(boter)
            turn+=1
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил✅", reply_markup=btn_place())
            if check_win(callback)!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(callback), reply_markup=regame)
            else:
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход🔔", reply_markup=btn_place())

    elif callback.data == "X" or callback.data == "O":
        try:
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "⛔️Не жульничать!⛔️", reply_markup=btn_place())
        except:
            pass




bot.polling()