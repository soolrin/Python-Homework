# 12. Ввести четырехзначное число и подсчитать сумму первой и третьей цифры и
# разницу между второй и четвертой цифрой.

print("\n")

num = int(input("Введите четырёхзначное число: "))
print("\n==========================\n")

# Вариант 1 с использованием арифметики
sum = num // 1000 + num % 10
diff = num % 1000 // 100 - num % 10

print(f"Сумма первой и последней цифры числа {num} равна: {sum}")
print(f"Разность второй и последней цифры числа {num} равна: {diff}")
print("\n==========================\n")

# Вариант 2 с использованием конвертации
num = str(num)
sum = int(num[0]) + int(num[3])
diff = int(num[1]) - int(num[3])

print(f"Сумма первой и последней цифры числа {num} равна: {sum}")
print(f"Разность второй и последней цифры числа {num} равна: {diff}")

print("")
