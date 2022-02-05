from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
OWNER = env.str("OWNER")  # bot egasi
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
api_key = env.str("API_KEY")  # Weather api

IP = env.str("ip")  # Xosting ip manzili

weather_data = {
    "clear sky": "☀️ Ochiq havo",
    "few clouds": "🌤Ozroq bulutli",
    "scattered clouds": "☁️Bulutli",
    "shower rain": "🌦Yomg`ir yog`yapti",
    "rain": "🌧Yomg`irli",
    "thunderstorm": "⚡️Chaqmoqli",
    "snow": "❄️ Qorli",
    "mist": "\U0001F32B Tumanli",
    "fog": "🌁Tumanli"
}


DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")