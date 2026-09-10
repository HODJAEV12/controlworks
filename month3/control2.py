# ВЕСЬ КОД ПИСАЛ Я, НЕ ИИ

import asyncio
import sqlite3
from token_ import token
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = token
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

connect = sqlite3.connect("students.db")
cursor = connect.cursor()

cursor.execute("""
create table if not exists students (
    id integer primary key autoincrement,
    telegram_id integer,
    name text,
    age integer,
    city text
)
""")
connect.commit()

class AddStudent(StatesGroup):
    name = State()
    age = State()
    city = State()

def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard = [
            [ InlineKeyboardButton(text="➕ Добавить студента", callback_data="add_student") ],
            [ InlineKeyboardButton(text="👨‍🎓 Список студентов", callback_data="show_students") ],
            [ InlineKeyboardButton(text="🗑 Удалить студента", callback_data="delete_student") ]
        ]
    )

@dp.message(F.text == "/start")
async def start(message : Message):
    await message.answer("<b>👋 Привет! Это TG-бот студентов. Выбери кнопку</b>", reply_markup=main_menu())

@dp.callback_query(F.data == "add_student")
async def get_name(callback : CallbackQuery, state : FSMContext):
    await callback.answer()

    await callback.message.answer("<b>✏️ Напиши имя студента:</b>")

    await state.set_state(AddStudent.name)

@dp.message(AddStudent.name)
async def get_age(message : Message, state : FSMContext):
    await state.update_data(name=message.text)

    await message.answer("<b>✏️ Напиши возраст студента:</b>")
    
    await state.set_state(AddStudent.age)

@dp.message(AddStudent.age)
async def get_city(message : Message, state : FSMContext):
    await state.update_data(age=message.text)

    await message.answer("<b>✏️ Напиши город студента:</b>")

    await state.set_state(AddStudent.city)

@dp.message(AddStudent.city)
async def add_student(message : Message, state : FSMContext):
    data = await state.get_data()

    name = data["name"]
    age = data["age"]
    city = message.text
    telegram_id = message.from_user.id

    cursor.execute("insert into students(telegram_id, name, age, city) values(?, ?, ?, ?)", (telegram_id, name, age, city))
    connect.commit()

    await state.clear()

    await message.answer(
        "<b>✅ Студент сохранён.</b>\n\n"
        f"Имя: {name}\n"
        f"Возраст: {age}\n"
        f"Город: {city}\n",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data == "show_students")
async def show_students(callback : CallbackQuery):
    telegram_id = callback.from_user.id

    cursor.execute("select id, name, age, city from students where telegram_id = ?", (telegram_id,))
    students = cursor.fetchall()

    if not students:
        await callback.answer()
        await callback.message.answer("❌ Студентов пока нет.")
        return

    text = "<b>👨‍🎓 Студенты:</b>\n\n"

    for student in students:
        student_id, name, age, city = student

        text += (
            f"ID: {student_id}\n"
            f"Имя: {name}\n"
            f"Возраст: {age}\n"
            f"Город: {city}\n"
            "------------------------\n"
        )

    await callback.answer()
    await callback.message.answer(text, reply_markup=main_menu())

@dp.callback_query(F.data == "delete_student")
async def show_buttons(callback : CallbackQuery):
    telegram_id = callback.from_user.id

    cursor.execute("select id, name from students where telegram_id = ?", (telegram_id,))
    students = cursor.fetchall()

    if not students:
        await callback.answer()
        await callback.message.answer("❌ Студентов пока нет.")
        return

    buttons = []

    for student_id, name  in students:
        buttons.append( [ InlineKeyboardButton(text=name, callback_data=f"delete:{student_id}") ] )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    await callback.answer()
    await callback.message.answer("Выберите студента:", reply_markup=keyboard)
    
@dp.callback_query(F.data.startswith("delete:"))
async def delete(callback : CallbackQuery):
    telegram_id = callback.from_user.id
    student_id = callback.data.split(":")[1]

    cursor.execute("delete from students where id = ? and telegram_id = ?", (student_id, telegram_id))
    connect.commit()

    await callback.answer()
    await callback.message.answer("✅ Студент удалён.", reply_markup=main_menu())

@dp.message()
async def unknown(message : Message):
    await message.answer("Напиши /help для помощи")

@dp.message(F.text == "/help")
async def help(message : Message):
    await message.answer("/start - меню\n/help - помощь")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: 
        asyncio.run(main())
    finally:
        connect.close()

# Ответы на вопросы
# 1. Linux - это операционная система как Windows, MacOS, которую можно настроить под себя
# 2. Aiogram нужен для создания и работы с tg ботом
# 3. Callback - это обратный вызов программы
# 4. FSM нужен для для того чтобы временно запоминать данные
# 5. База данных - это место где хранятся данные в виде таблиц
# 6. SQLite - это библиотека с помощью которой можно "общаться" c языком БД SQL
# 7. INSERT - добавляет данные, SELECT - получает данные, UPDATE - изменяет данные, DELETE - удаляет данные
# 8. JOIN - команда, которая объединяет таблицы
# 9. Inline кнопки нужны для создания кнопок в tg боте
# 10. Tg бот связан с python с помощью aiogram, SQL связан с python с помощью sqlite3