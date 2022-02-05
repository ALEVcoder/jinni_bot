import requests, json
from aiogram import Bot, types, executor
from aiogram.types import Message, CallbackQuery
from data.config import api_key, weather_data
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from loader import dp, db, bot
from datetime import datetime
from pprint import pprint

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


@dp.message_handler(text='Ob havo')
async def start_command(message: types.Message):
    await message.answer(f"Hurmatli {message.from_user.full_name} Ob-havo ma`lumotini bilishni hohlaysizmi? \n Quyidagi tugmalardan biriga bosing", reply_markup=viloyat)



viloyat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Samarqand"),
            KeyboardButton(text="Toshkent"),
        ],
        [
            KeyboardButton(text="Andijon"),
            KeyboardButton(text="Farg`ona"),
        ]
        ,
        [
            KeyboardButton(text="Jizzax"),
            KeyboardButton(text="Buxoro"),
        ],
        [
            KeyboardButton(text="Navoiy"),
            KeyboardButton(text="Surxandaryo"),
        ],
        [
            KeyboardButton(text="Qashqadaryo"),
            KeyboardButton(text="Namangan"),
        ],
        [
            KeyboardButton(text="Xorazim"),
            KeyboardButton(text="Sirdaryo"),
        ]
        ,
        [
            KeyboardButton(text="Nukus"),
            KeyboardButton(text="About us"),
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(regexp="Toshkent")
async def get_data(message: types.Message):
    data = 'Toshkent'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Samarqand")
async def get_data(message: types.Message):
    data = 'Samarqand'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404':  # Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]

                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695, 181), f"{message.text.upper()}", font=font, fill=(255, 255, 255))
                draw.text((665, 403), f"Harorat: {temp} C", font=font, fill=(23, 53, 113))
                draw.text((665, 484), f"Holat: {wd}", font=font, fill=(23, 53, 113))
                draw.text((665, 549), f"Shamol tezligi: {wind} m/s", font=font, fill=(23, 53, 113))
                draw.text((665, 620), f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}", font=font,
                          fill=(23, 53, 113))
                draw.text((665, 691), f"Quyosh botishi: {datetime.fromtimestamp(sunset)}", font=font,
                          fill=(23, 53, 113))
                draw.text((665, 746),
                          f"Kun davomiyligi: {datetime.fromtimestamp(sunset) - datetime.fromtimestamp(sunrise)} s",
                          font=font, fill=(23, 53, 113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n" \
                       f"Ob-havo: {wd}\n" \
                       f"Harorat:🌡 {temp} ℃\n" \
                       f"Shamol tezligi:🌬{wind} m/s\n" \
                       f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n" \
                       f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n" \
                       f"Kun davomiyligi: {datetime.fromtimestamp(sunset) - datetime.fromtimestamp(sunrise)}\n" \
                       f"Kuningiz hayrli o'tsin ☺️"

                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Andijon")
async def get_data(message: types.Message):
    data = 'Andijon'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404':  # Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]

                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695, 181), f"{message.text.upper()}", font=font, fill=(255, 255, 255))
                draw.text((665, 403), f"Harorat: {temp} C", font=font, fill=(23, 53, 113))
                draw.text((665, 484), f"Holat: {wd}", font=font, fill=(23, 53, 113))
                draw.text((665, 549), f"Shamol tezligi: {wind} m/s", font=font, fill=(23, 53, 113))
                draw.text((665, 620), f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}", font=font,
                          fill=(23, 53, 113))
                draw.text((665, 691), f"Quyosh botishi: {datetime.fromtimestamp(sunset)}", font=font,
                          fill=(23, 53, 113))
                draw.text((665, 746),
                          f"Kun davomiyligi: {datetime.fromtimestamp(sunset) - datetime.fromtimestamp(sunrise)} s",
                          font=font, fill=(23, 53, 113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n" \
                       f"Ob-havo: {wd}\n" \
                       f"Harorat:🌡 {temp} ℃\n" \
                       f"Shamol tezligi:🌬{wind} m/s\n" \
                       f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n" \
                       f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n" \
                       f"Kun davomiyligi: {datetime.fromtimestamp(sunset) - datetime.fromtimestamp(sunrise)}\n" \
                       f"Kuningiz hayrli o'tsin ☺️"

                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Farg`ona")
async def get_data(message:types.Message):
    data = 'Fargona'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Jizzax")
async def get_data(message:types.Message):
    data = 'Jizzax'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Buxoro")
async def get_data(message:types.Message):
    data = 'Buxoro'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Navoiy")
async def get_data(message:types.Message):
    data = 'Navoiy'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Surxandaryo")
async def get_data(message:types.Message):
    data = 'Termiz'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Qashqadaryo")
async def get_data(message:types.Message):
    data = 'Qashqadaryo'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)



@dp.message_handler(regexp="Namangan")
async def get_data(message:types.Message):
    data = 'Namangan'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Xorazim")
async def get_data(message:types.Message):
    data = 'Xiva'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Sirdaryo")
async def get_data(message:types.Message):
    data = 'Sirdaryo'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)


@dp.message_handler(regexp="Nukus")
async def get_data(message:types.Message):
    data = 'Nukus'
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}&units=metric"
        data = requests.get(url=url).json()
        if "cod" in data:
            if data['cod'] == '404': #Not found
                # print(True)
                await message.answer("Bu shaxarni tanimayman afsus !")
            if data['cod'] == 200:
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                wind = data['wind']['speed']
                sunset = data['sys']['sunset']
                sunrise = data['sys']['sunrise']
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                lat = data['coord']['lat']
                lon = data['coord']['lon']

                if description in weather_data:
                    wd = weather_data[description]
                    
                else:
                    wd = "Bilmadim, oynadan qarab ko'ringchi 😊"
                img = Image.open("handlers/users/pictures/nimadir.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("handlers/users/ttf/righteous/righteous.ttf", 32)
                draw.text((695,181),f"{message.text.upper()}",font=font, fill=(255,255,255))
                draw.text((665,403),f"Harorat: {temp} C",font=font, fill=(23,53,113))
                draw.text((665,484),f"Holat: {wd}",font=font, fill=(23,53,113))
                draw.text((665,549),f"Shamol tezligi: {wind} m/s",font=font, fill=(23,53,113))
                draw.text((665,620),f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}",font=font, fill=(23,53,113))
                draw.text((665,691),f"Quyosh botishi: {datetime.fromtimestamp(sunset)}",font=font, fill=(23,53,113))
                draw.text((665,746),f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)} s",font=font, fill=(23,53,113))
                img.save("handlers/users/pictures/to_send.jpg")
                text = f"\n*********{now} **********\n"\
                    f"Ob-havo: {wd}\n" \
                    f"Harorat:🌡 {temp} ℃\n" \
                    f"Shamol tezligi:🌬{wind} m/s\n"\
                    f"Quyosh chiqishi: {datetime.fromtimestamp(sunrise)}\n"\
                    f"Quyosh botishi: {datetime.fromtimestamp(sunset)}\n"\
                    f"Kun davomiyligi: {datetime.fromtimestamp(sunset)-datetime.fromtimestamp(sunrise)}\n"\
                    f"Kuningiz hayrli o'tsin ☺️"
                
                await message.answer_photo(open('handlers/users/pictures/to_send.jpg', 'rb'), caption=text)
                await message.answer_location(latitude=lat, longitude=lon)
    except Exception as e:
        print(e)

@dp.message_handler(regexp="About us")
async def first_lesson(message: types.Message):
    await message.answer(
        text="Our Phone Nomerber:  93 228 66 07"
    )



