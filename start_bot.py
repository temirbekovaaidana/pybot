import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=["start", "Hello"])
def get_start_message(message):
    full_name = f"{message.from_user.last_name} {message.from_user.first_name} !!!"
    text = f"Welcome {full_name}"
    bot.send_message(message.chat.id, text)
    bot.reply_to(message, text)

@bot.message_handler(content_types=["text"])
def get_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if message.text.lower() == "меню":
        text = "Выберите пожалуйста:"
        button1 = types.InlineKeyboardButton("чай", callback_data="tea")
        #button1 = types.InlineKeyboardButton("чай", url="https://www.google.com/search?q=tea&sxsrf=ALiCzsYn0Nu6SBiO31Bp65hNn51LrgWTIQ:1667537037440&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj5uZDG25P7AhUJ_CoKHdSpCOwQ_AUoAXoECAEQAw")
        button2 = types.InlineKeyboardButton("кофе", callback_data="coffee")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = ""
    if call.data == "tea":
        text = f"Выберите желаемый чай внизy:"
        btn1 =types.KeyboardButton("black")
        btn2 = types.KeyboardButton("blue")
        btn3 = types.KeyboardButton("green")
        murkup.add(btn1, btn2, btn3)
    if call.data == "coffee":
        text = f"Выберите желаемый кофе внизy:"
        btn1 = types.KeyboardButton("latte")
        btn2 = types.KeyboardButton("cappuchino")
        btn3 = types.KeyboardButton("espresso")
        murkup.add(btn1, btn2, btn3)

    bot.send_message(call.message.chat.id, text, reply_markup=murkup)



bot.polling()