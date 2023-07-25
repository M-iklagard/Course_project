"""Для корректної роботи потрібно:
 pip install googletrans==4.0.0-rc1
 pip install art
 pip install openai
 pip install pyjokes
 pip install pyTelegramBotAPI
"""


import random
import openai
import art
import pyjokes
import telebot
from googletrans import Translator
from telebot import types

API_TOKEN = "тут повинен бути ваш апі"
bot = telebot.TeleBot(API_TOKEN)

random_nums = [str(random.randint(1, 15)) for _ in range(0, 9)]
right_num = random_nums[random.randint(0, 8)]
print(right_num)


@bot.message_handler(commands=["start"])
def start(message):
    button_bar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but_1 = types.KeyboardButton("Пожартуй😂")
    but_2 = types.KeyboardButton("Випадковий ASCI арт🎭")
    but_3 = types.KeyboardButton("Випадковий фільм🎬")
    but_4 = types.KeyboardButton("Гра🎮")
    but_5 = types.KeyboardButton("Книги📕")
    but_6 = types.KeyboardButton("Переклад")

    button_bar.add(but_1, but_2, but_3, but_4, but_5, but_6)

    first = message.from_user.first_name
    last = "" if message.from_user.last_name == first or message.from_user.last_name is None \
        else message.from_user.last_name
    repl = f"Привіт {first} {last}\nЩоб поспілкуватись з chat-GPT, перед реплікою введіть gpt:"

    bot.send_message(message.chat.id, text=repl, reply_markup=button_bar)


@bot.message_handler(content_types=["text"])
def fun(message):
    global random_nums, right_num

    if message.text == "Пожартуй😂":
        translator = Translator()
        joke = pyjokes.get_joke(language="en", category="chuck")
        translation = translator.translate(joke, dest="uk")
        bot.send_message(message.chat.id, text=translation.text)

    elif message.text == "Випадковий фільм🎬":
        link_bar = types.InlineKeyboardMarkup()
        link_line = types.InlineKeyboardButton(text="Випадковий фільм", url="https://gidonline.io/random/")
        link_bar.add(link_line, row_width=1)
        bot.send_message(message.chat.id, text="Перейдіть за посиланням нижче 👇", reply_markup=link_bar)

    elif message.text == "Випадковий ASCI арт🎭":
        bot.send_message(message.chat.id, text=f"{art.randart()}")

    elif message.text == "Гра🎮":
        game_bar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        but_1 = types.KeyboardButton(random_nums[0])
        but_2 = types.KeyboardButton(random_nums[1])
        but_3 = types.KeyboardButton(random_nums[2])
        but_4 = types.KeyboardButton(random_nums[3])
        but_5 = types.KeyboardButton(random_nums[4])
        but_6 = types.KeyboardButton(random_nums[5])
        but_7 = types.KeyboardButton(random_nums[6])
        but_8 = types.KeyboardButton(random_nums[7])
        but_9 = types.KeyboardButton(random_nums[8])
        game_bar.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9)
        bot.send_message(message.chat.id, text="Вгадай число", reply_markup=game_bar)

    elif message.text in random_nums:

        if message.text == right_num:
            bot.send_message(message.chat.id, text=f"Вірна здогадка 🫵🥳")
            start(message)
            random_nums = [str(random.randint(1, 15)) for _ in range(0, 9)]
            right_num = random_nums[random.randint(0, 8)]
            print(right_num)

        elif int(message.text) < int(right_num):
            bot.send_message(message.chat.id, text="Загадане число більше")

        elif int(message.text) > int(right_num):
            bot.send_message(message.chat.id, text="Загадане число меньше")

    elif message.text == "Книги📕":
        book_shelf = types.InlineKeyboardMarkup(row_width=1)
        book = types.InlineKeyboardButton(text="📓",
                                          url="https://starylev.com.ua/mort")
        book_shelf.add(book)
        bot.send_photo(chat_id=message.chat.id,
                       photo="https://img.imageboss.me/vsl/width/922/2021-10-09/rjaqpqzjygefnxd2zbw7.png",
                       caption="""
Роман «Морт»
циклу «Смерть» відкриває цикл серії «Дискосвіт», у якому головним персонажем є Смерть.
Та це не означає, що книжка моторошна, адже у світі Террі Пратчетта Смерть рибалить, філософує, любить кошенят
і смачні страви, мріє про відпустку і врешті просто виконує свою роботу: доправляє душі в інший світ. Думки про
відпочинок спонукають Смерть обрати собі в підмайстри сільського хлопця Морта
""")
        bot.send_message(message.chat.id, text="Книга за посиланям", reply_markup=book_shelf)
        book_shelf_2 = types.InlineKeyboardMarkup(row_width=1)
        book_2 = types.InlineKeyboardButton(text="📓",
                                            url="https://book-ye.com.ua/catalog/naukova-fantastyka/pisni-giperiona-"
                                                "knyha-1-giperion-chumatskyj-shlyakh/")
        book_shelf_2.add(book_2)
        bot.send_photo(chat_id=message.chat.id,
                       photo="https://book-ye.com.ua/upload/resize_cache/iblock/062/520_860_1/0eac02d3_0e4d_11e7_80c5_"
                             "000c29ae1566_a18d0d68_666a_11ed_8175_0050568ef5e6.jpg",
                       caption="""
Роман «Гіперіон»
Мине якихось вісімсот років, і до загадкових Гробниць часу, що порушують закони Ньютона та загальну теорію 
відносності, на абсолютно провінційну планету Гіперіон вирушить дивна делегація дивного культу, який боготворить
невблаганного монстра. Католицький священник, полковник військово-космічних сил, геніальний поет-лихослов, 
тамплієр, що водить зореліт-дерево, тихий філософ, приватний детектив та безіменний дипломат – кожен із 
них має заповітне бажання і потаємну ціль, від яких може залежати майбутнє не тільки кільканадцяти мільярдів 
людей на двох сотнях планет, а й штучних інтелектів та загадкової постлюдської раси Вигнанців. В епіцентрі 
пристрастей та політичних інтриг — Гіперіон
        """)
        bot.send_message(message.chat.id, text="Книга за посиланям", reply_markup=book_shelf_2)

    elif message.text == "Переклад":
        bot.send_message(message.chat.id, text="""
Введіть текст для перекладу,
у форматі- zz_translate:хххххххх

zz - мова перекладу 
                    af afrikaans
                    sq albanian
                    am amharic
                    ar arabic
                    hy armenian
                    az azerbaijani
                    eu basque
                    be belarusian
                    uk ukrainian

хххх - текст для перекладу""")
    elif "_translate:" in message.text:
        translator = Translator()
        translated_text = translator.translate(text=message.text[13:], dest=message.text[:2])
        bot.send_message(message.chat.id, text=translated_text.text)

    elif "gpt:" in message.text:
        openai.api_key = "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"
        messages = [{"role": "user", "content": message.text[4:]}]
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message["content"]
        bot.send_message(message.chat.id, text=reply)
        messages.append({"role": "assistant", "content": reply})


bot.polling()
