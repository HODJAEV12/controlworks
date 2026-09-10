from database import *

def add_new_book():
    title = input("Название: ")
    author = input("Автор: ")
    genre = input("Жанр: ")
    year = int(input("Год: "))
    pages = int(input("Страниц: "))

    add_book(title, author, genre, year, pages)


def show_all_books():
    for book in show_books():
        print(book)


def add_new_user():
    name = input("Имя: ")
    age = int(input("Возраст: "))
    phone = input("Телефон: ")

    add_user(name, age, phone)
    

def show_all_users():
    for user in show_users():
        print(user)