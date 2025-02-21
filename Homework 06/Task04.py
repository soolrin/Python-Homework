# 4. Создать список из 200 случайных чисел в диапазоне от 0 до 200.
# Определить количество однозначных, двузначных и трехзначных чисел в соотношении.
import random

print("\n===================================\n")

numbers = [random.randint(0, 200) for _ in range(200)]

one = sum(1 for num in numbers if num >= 0 and num <= 9)
two = sum(1 for num in numbers if num >= 10 and num <= 99)
three = sum(1 for num in numbers if num >= 100 and num <= 199)

print(f"Количество однозначных чисел: {one} - {one / 200 * 100:.2f}%")
print(f"Количество двузначных чисел: {two} - {two / 200 * 100:.2f}%")
print(f"Количество трехзначных чисел: {three} - {three / 200 * 100:.2f}%")

print("\n===================================\n")
