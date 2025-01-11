# 8. Ввести три числа и найти меньшее из них.

print("\n")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

print("\n==========================\n")

if num1 < num2 and num1 < num3:
    print(f"Меньшее число: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"Меньшее число: {num2}")
else:
    print(f"Меньшее число: {num3}")

print("\n==========================\n")
