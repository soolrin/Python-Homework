# 2. Создать список из 20 случайных чисел. Вывести все элементы массива
# с четными индексами.
import random

print("\n===================================\n")

numbers = [random.randint(0, 100) for _ in range(20)]

print(f"Список: {numbers}")
print(f"Элементы с четными индексами: {numbers[::2]}")

print("\n===================================\n")
