# 16. Ввести с клавиатуры трехзначное число и перевернуть его.

print("\n")

num = int(input("Введите трехзначное число: "))
print("\n==========================\n")

# Вариант 1 с использованием арифметики
new_num = (num % 10 * 100) + (num % 100 // 10 * 10) + (num // 100)
print(f"Изначальное число: {num} \nПеревернутое число: {new_num}")
print("\n==========================\n")

# Вариант 2 с использованием строк
new_num = str(num)
new_num = new_num[2] + new_num[1] + new_num[0]
print(f"Изначальное число: {num} \nПеревернутое число: {new_num}")

print("")
