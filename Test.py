import telebot
from telebot import types
import random

message_to_edit = ""

api = "5897382480:AAElanE4N3nj-_ouRyRKYVE30mShoXwi6Ls"

gb_dict = {1:"⬜️",2:"⬜️",3:"⬜️",4:"⬜️",5:"⬜️",6:"⬜️",7:"⬜️",8:"⬜️",9:"⬜️","X":"❌", "O":"⭕️"}
gb_list=[i for i in range(1,10)]
bot_list = [i for i in range(9)]
X_or_O = ["X", "O"]

player, boter = " ", " "


bot = telebot.TeleBot(api)
print(bot.__dict__)

def bot_turn(boter):
    global gb_list
    a = random.choice(bot_list)
    bot_list.remove(a)
    gb_list[a] = boter

def check_win():
    global gb_list
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
    if a == player: return("💥Вы выиграли!💥")
    elif a == boter: return("🎮Выиграл бот🎮")
    else: return(None)


@bot.message_handler(commands=["start"])
def start(message):
    global message_to_edit, gb_dict, gb_list, player, boter
    gb_XO = ["X", "O"]
    player = random.choice(gb_XO)
    if player == "X": 
        bot.send_message(message.chat.id, text = "Вы играете за ❌")
        boter = "O"
    else: 
        bot.send_message(message.chat.id, text = "Вы играете за ⭕️")
        boter = "X"
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
    message_to_edit = bot.send_message(message.chat.id, text="Начнем игру!", reply_markup=gb)

@bot.message_handler(content_types=["text"])
def newgame(message):
    global gb_list, message_to_edit, boter, player, bot_list
    gb_XO = ["X", "O"]
    player = random.choice(gb_XO)
    if player == "X": 
        bot.send_message(message.chat.id, text = "Вы играете за ❌")
        boter = "O"
    else: 
        bot.send_message(message.chat.id, text = "Вы играете за ⭕️")
        boter = "X"
    gb_list=[i for i in range(1, 10)]
    bot_list=[i for i in range(9)]
    if message.text == "🔄Начать новую игру🔄":
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
        message_to_edit = bot.send_message(message.chat.id, text="Начнем игру!", reply_markup=gb)
    else:
        regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
        regame.add(btn)
        bot.send_message(message.chat.id, text="Такой команды я не знаю", reply_markup=regame)


@bot.callback_query_handler(func = lambda callback: callback.data)
def callback_checker(callback):
    global message_to_edit, gb_dict, gb_list, player, boter, bot_list
    
    if callback.data == "1":
        gb_list[0] = player
        bot_list.remove(0)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "2":
        gb_list[1] = player
        bot_list.remove(1)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "3":
        gb_list[2] = player
        bot_list.remove(2)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "4":
        gb_list[3] = player
        bot_list.remove(3)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "5":
        gb_list[4] = player
        bot_list.remove(4)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "6":
        gb_list[5] = player
        bot_list.remove(5)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "7":
        gb_list[6] = player
        bot_list.remove(6)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "8":
        gb_list[7] = player
        bot_list.remove(7)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    elif callback.data == "9":
        gb_list[8] = player
        bot_list.remove(8)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Вы походили", reply_markup=gb)
        if check_win() != None:
            regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
            regame.add(btn)
            bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
        else:
            bot_turn(boter)
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
            bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text="Бот походил", reply_markup=gb)
            if check_win()!=None:
                regame = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn = types.KeyboardButton(text="🔄Начать новую игру🔄")
                regame.add(btn)
                bot.send_message(message_to_edit.chat.id, text=check_win(), reply_markup=regame)
            else:
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
                bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Твой ход", reply_markup=gb)

    else:
        print(callback.data)
        print(gb_list)
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
        bot.edit_message_text(chat_id=message_to_edit.chat.id, message_id=message_to_edit.message_id, text = "Не жульничать!", reply_markup=gb)





bot.polling()