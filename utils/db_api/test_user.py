import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvali yaratilyabdi...")
    # await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("mehrinoz", "mehrinoz2604", 123456789)
    await db.add_user("abdulaziz", "alevcoder", 12341123)
    await db.add_user("marjona", "marjona", 131231)
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")


asyncio.run(test())