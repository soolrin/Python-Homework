# 17. Введите число с клавиатуры и проверьте, принадлежит ли это число диапазона от 0 до 100 (включительно).

print("\n")

num = int(input("Введите число: "))

print("\n==========================\n")

print("Число в диапазоне") if num >= 0 and num <= 100 else print("Число не в диапазоне")

print("\n==========================\n")
