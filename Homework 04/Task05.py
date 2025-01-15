# 5. С клавиатуры вводится целое число хоть какой разрядности.
# Определить количество цифр в нем и их сумму.

print("\n")

while True:
    num = input("Введите число: ").lstrip("-")

    if num.isdigit():
        break
    else:
        print("Введите целое число")

sum = 0

print("\n==========================\n")

for i in range(len(num)):
    sum += int(num[i])

print(f"Сумма цифр введенного числа {num} = {sum}")

print("\n==========================\n")