from database import *

while True:
    print("\n===== БИБЛИОТЕКА =====")
    print("1. Добавить книгу")
    print("2. Показать книги")
    print("3. Удалить книгу")
    print("4. Добавить пользователя")
    print("5. Показать пользователей")
    print("6. Выход")

    choice = input("Выберите: ")

    if choice == "1":
        title = input("Название: ")
        author = input("Автор: ")
        genre = input("Жанр: ")
        year = int(input("Год: "))
        pages = int(input("Страниц: "))
        add_book(title, author, genre, year, pages)
        print("Книга добавлена")

    elif choice == "2":
        books = show_books()
        for book in books:
            print(book)

    elif choice == "3":
        book_id = int(input("ID книги: "))
        delete_book(book_id)
        print("Удалено")

    elif choice == "4":
        name = input("Имя: ")
        age = int(input("Возраст: "))
        phone = input("Телефон: ")
        add_user(name, age, phone)
        print("Пользователь добавлен")

    elif choice == "5":
        users = show_users()
        for user in users:
            print(user)

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Неверный выбор!")