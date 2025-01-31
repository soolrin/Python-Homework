# 7. Напишите программу, которая будет печатать ромбовидный рисунок на основе
# введенной строки (максимальная длина - 50 символов).
# Пример вывода, если строка «testing»

import re

print(f"\n{"Инициализация":=^35}\n")

while True:
    text = input("Напишите ваш текст (От 3 до 50 символов): ")

    if len(text) <= 50 and len(text) >= 3:
        break
    else:
        print("Текст должен быть от 3 до 50 символов\n")
        continue

print("\n===================================\n")

for i in range(len(text)):
    print(" " * (len(text) - i - 1) + text[: i + 1])

for i in range(1, len(text)):
    print(text[i:])

print("\n===================================\n")
