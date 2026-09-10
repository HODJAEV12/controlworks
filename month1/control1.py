# # Задание1

# number1 = int(input("Первое число: "))
# number2 = int(input("Второе число: "))

# def function():
#     if number1 > 0 and number2 > 0:
#         print("Оба числа положительные")

# if number1 > number2:
#     print("Первое число равны")
#     function()
# elif number2 > number1:
#     print("Второе число больше")
#     function()
# elif number1 == number2:
#     print("Числа равны")
#     function()

# # Задание2

# num = int(input("Введите число: "))
# if 1 <= num <= 10:
#     print("Число в диапазоне 1–10")
# elif 11 <= num <= 100:
#     print("Число в диапазоне 11-100")
# else:
#     print("Число вне диапазона")

# # Задание3

# name = input("Введите имя: ")
# name_len = len(name)

# print(f"Длина имени: {name_len}")

# if name_len < 5:
#     print("Короткое имя")
# elif 5 < name_len < 8:
#     print("Среднее имя")
# elif name_len > 8:
#     print("Длинное имя")

# # Задание4

# numbers = [7, 3, 15, 2]

# print(numbers[1])
# print(numbers[-1])

# numbers[-1] = 7
# numbers[0] = 2

# print(numbers)

# # Задание5

# summa = int(input("Введите сумму покупки: "))

# if summa >= 5000:
#     print("Скидка 10%")
#     print(f"Итоговая сумма: {summa - summa / 100 * 10}")
# elif summa > 2000:
#     print("Скидка 5%")
#     print(f"Итоговая сумма: {summa - summa / 100 * 5}")
# else:
#     print("Скидки нет")