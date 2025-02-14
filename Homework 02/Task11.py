# 11. Ввести с клавиатуры два трёхзначных числа и поменять в них средние цифры.

print("\n")

num1 = int(input("Введите первое трёхзначное число: "))
num2 = int(input("Введите второе трёхзначное число: "))
print("\n==========================\n")

# Вариант 1 с использованием вывода
print(f"Число 1: {num1} теперь = {num1 // 100}{num2 % 100 // 10}{num1 % 10}")
print(f"Число 2: {num2} теперь = {num2 // 100}{num1 % 100 // 10}{num2 % 10}")
print("\n==========================\n")

# Вариант 2 с использованием арифметики
print(f"Число 1 было: {num1}")
print(f"Число 2 было: {num2}")
print("")

temp = num1 % 100 // 10 * 10  # Сохраняем среднюю цифру первого числа
num1 = (num1 // 100 * 100) + (num2 % 100 // 10 * 10) + (num1 % 10)
num2 = (num2 // 100 * 100) + temp + (num2 % 10)

print(f"Число 1 стало: {num1}")
print(f"Число 2 стало: {num2}")
print("\n==========================\n")

# вариант 3 с использованием строк
num1 = str(num1)
num2 = str(num2)
temp = num1[1]

print(f"Число 1 было: {num1}")
print(f"Число 2 было: {num2}")
print("")

num1 = num1[0] + num2[1] + num1[2]
num2 = num2[0] + temp + num2[2]

print(f"Число 1 стало: {num1}")
print(f"Число 2 стало: {num2}")

print("")
