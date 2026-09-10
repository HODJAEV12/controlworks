import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery

TOKEN = "8592541479:AAG02F7sXIxvPN58EcV8tBanibY2ZtThgZo"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message : Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = [
            [ InlineKeyboardButton(text="🐍Python", callback_data="python") ],
            [ InlineKeyboardButton(text="⚙️SQL", callback_data="sql") ],
            [ InlineKeyboardButton(text="🐧Linux", callback_data="linux") ]
        ]
    )
    await message.answer("🧠Выбери тему:", reply_markup=keyboard)

@dp.callback_query(F.data == "python")
async def python(callback : CallbackQuery):
    await callback.answer("🐍Python!")
    await callback.message.answer("🐍Python — это популярный и очень простой язык программирования.")

@dp.callback_query(F.data == "sql")
async def sql(callback : CallbackQuery):
    await callback.answer("⚙️SQL!")
    await callback.message.answer("⚙️SQL— это специальный язык программирования, который используют для общения с базами данных.")

@dp.callback_query(F.data == "linux")
async def linux(callback : CallbackQuery):
    await callback.answer("🐧Linux!")
    await callback.message.answer("🐧Linux — это бесплатная операционная система, похожая на Windows или macOS.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    asyncio.run(main())