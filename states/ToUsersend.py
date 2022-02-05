from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class ToUsersend(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    xabar = State() #ism
    nechta = State() #email
    kimga = State() #Tel raqami