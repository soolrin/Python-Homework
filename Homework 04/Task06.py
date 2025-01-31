# 6. С клавиатуры вводится целое число. Вывести на экран все числа, на которые
# введенное число делится без остатка.

print("\n")

while True:
    num = input("Введите число: ").lstrip("-")

    if num.isdigit() and int(num) != 0:
        num = int(num)
        break
    else:
        print("Введите целое число")

print("\n==========================\n")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, -i)

print("\n==========================\n")
