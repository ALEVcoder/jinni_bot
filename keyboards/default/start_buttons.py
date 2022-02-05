from aiogram import Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


start_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xabarni ko`paytirish"),
            KeyboardButton(text="Ob havo"),
        ]
    ],
    resize_keyboard=True
)