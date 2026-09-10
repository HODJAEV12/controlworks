### Задание1

student = {
    "name": "Abdulloh",
    "age": 14,
    "group": "Geeks 41-1B020626",
    "average_mark": 4.8
}

print(student)
print(student["name"])
print(student["average_mark"])

### Задание2

products = {
    "Ноутбук": 75000,
    "Телефон": 43000,
    "Наушники": 5500,
    "Монитор": 18500,
    "Мышка": 2200
}

expensive_product = max(products, key=products.get)
cheapest_product = min(products, key=products.get)

total_price = sum(products.values())
average_price = total_price / len(products)

print(f"Самый дорогой товар: {expensive_product} ({products[expensive_product]})")
print(f"Самый дешёвый товар: {cheapest_product} ({products[cheapest_product]})")
print(f"Средняя цена товаров: {average_price}")

### Задание3

unique_words = set()

print("Введите 5 слов (после каждого слова нажимайте Enter):")

for i in range(5):
    word = input(f"Слово {i+1}: ").strip()
    unique_words.add(word)

print(f"Уникальные слова: {', '.join(unique_words)}")
print(f"Количество уникальных слов: {len(unique_words)}")

### Задание4

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

same = a & b
only_a = a - b
only_b = b - a
union = a | b

print(f"Общие элементы: {same}")
print(f"Только в a: {only_a}")
print(f"Только в b: {only_b}")
print(f"Объединение множеств: {union}")

### Задание5

students_mark = {
    "Abdulloh": [5, 3, 4],
    "Abubakr": [3, 2, 3],
    "Nurbolot": [4, 5, 2]
}

def average_mark(student_name):
    marks_sum = 0
    marks_count = 0

    for i in students_mark[student_name]:
        marks_count += 1
        marks_sum += i
    
    print(f"Средняя оценка {student_name} --> {round(marks_sum / marks_count, 3)}")

average_mark("Abdulloh")
average_mark("Abubakr")
average_mark("Nurbolot")

### Задание6

students_a = {"biology", "math", "chemistry", "english"}
students_b = {"chemistry", "russian", "IT", "math"}

same = students_a & students_b
only_a = students_a - students_b
only_b = students_b - students_a
union = students_a | students_b

print(f"Общие предметы: {same}")
print(f"Только у первого студента: {only_a}")
print(f"Только у второго студента: {only_b}")

### Задание7

numbers = [2, 4, 6, 8]
squares = list(map(lambda x : x ** 2, numbers))
print(squares)

### Задание8

number = int(input("Введите число: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")