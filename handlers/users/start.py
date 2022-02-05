import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.start_buttons import start_reply
from loader import dp, db, bot
from data.config import ADMINS, OWNER



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    if str(message.from_user.id) == OWNER:
        await message.reply('Salom Mehrinoz men sizning do`stingizman 😊', reply_markup=start_reply)
    else:
        await message.answer(f"Salom, {message.from_user.full_name}, men Mehrinozning do`stiman!", reply_markup=start_reply)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nMehrinoz Do`stlarimiz soni {count} ta bo`ldi."
    print(msg)
    await bot.send_message(chat_id=ADMINS, text=msg)