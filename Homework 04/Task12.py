# 12. Показать на экране равнобедренный треугольник высотой N.

print("\n")

while True:
    up = input("Введите высоту треугольника: ")
    if up.isdigit():
        up = int(up)
        break
    else:
        print("Некорректный ввод! Введи число.")

print("\n==========================\n")

# Сложно читаемый
for i in range(1, up + 1):
    print(" " * (up - i) + "*" * (i * 2 - 1))

# Тоже самое только через переменные
for i in range(1, up + 1):
    space = " " * (up - i)
    star = "*" * (i * 2 - 1)
    print(space + star)

print("\n==========================\n")
