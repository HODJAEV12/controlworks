from abc import ABC, abstractmethod


class LibraryItem(ABC):
    @abstractmethod
    def take(self):
        pass

    @abstractmethod
    def give_back(self):
        pass


class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def info(self):
        print(self.id, self.name, self.age)


class User(Person):
    def __init__(self, id, name, age, phone):
        super().__init__(id, name, age)
        self.__phone = phone
        self.__borrowed_books = []

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if value.startswith("+996"):
            self.__phone = value

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)

    def info(self):
        print(self.id, self.name, self.age, self.phone)


class Librarian(Person):
    def __init__(self, id, name, age, salary, position):
        super().__init__(id, name, age)
        self.salary = salary
        self.position = position

    def info(self):
        print(self.name, self.position, self.salary)


class Book(LibraryItem):
    created_books = 0

    def __init__(self, id, title, author, year, genre, pages):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.available = True
        Book.created_books += 1

    def info(self):
        print(self.title, self.author, self.year)

    def take(self):
        self.available = False

    def give_back(self):
        self.available = True

    @classmethod
    def get_created_books(cls):
        return cls.created_books

    def __str__(self):
        return f"{self.title} - {self.author}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title

    def __len__(self):
        return self.pages


class Downloadable:
    def download(self):
        print("Книга скачана")


class DigitalBook(Book, Downloadable):
    pass


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]

    def show_books(self):
        for b in self.books:
            print(b)

    def register_user(self, user):
        self.users.append(user)

    def show_users(self):
        for u in self.users:
            u.info()


def show_information(person):
    person.info()