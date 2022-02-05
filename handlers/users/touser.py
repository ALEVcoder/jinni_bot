

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from loader import dp, db, bot
from states.ToUsersend import ToUsersend



# /send komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text='Xabarni ko`paytirish', state=None)
async def enter_test(message: types.Message):
    await message.answer("Ko`paytirmoqchi bolgan xabaringiz", reply_markup=ReplyKeyboardRemove())
    await ToUsersend.xabar.set()


@dp.message_handler(state=ToUsersend.xabar)
async def answer_fullname(message: types.Message, state: FSMContext):
    xabar = message.text
    print(message.message_id)


    await state.update_data(
        {"xabar": xabar}
    )

    await message.answer("Nechta qilib beray")

    # await PersonalData.email.set()
    await ToUsersend.next()

@dp.message_handler(state=ToUsersend.nechta)
async def answer_email(message: types.Message, state: FSMContext):
    nechta = message.text

    await state.update_data(
        {"nechta": nechta}
    )

    await message.answer("Kimga yuboramiz, foydalanuvchi ID ni yozing")

    await ToUsersend.next()


@dp.message_handler(state=ToUsersend.kimga)
async def answer_phone(message: types.Message, state: FSMContext):
    kimga = message.text

    await state.update_data(
        {"kimga": kimga}
    )
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    xabar = data.get("xabar")
    nechta = data.get("nechta")
    kimga = data.get("kimga")





    # Xabarni Foydalanuvchiga yuborish
    try:
        for i in range(int(nechta)):
            await bot.send_message(chat_id=str(kimga), text=xabar)
        await message.reply('Yuborildi')
    except:
        await message.reply(text='Bu foydalanuvchi Mehrinozning do`stlari safiga kirmagan. /help \n\n Yuborilmadi.😔')





    # bormi = await db.select_all_users(kimga)
    # print(f"Foydalanuvchi: {bormi}")



    # State dan chiqaramiz
    # 1-variant

    await state.finish()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)