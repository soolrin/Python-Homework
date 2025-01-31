# 14.3 Выполнить все три практики в конце презентации по циклам.
# Пользователь указывает с клавиатуры нечетное число. Рисуется фигура с заданной стороной

print("\n")
while True:
    size = input("Введите размер фигуры (нечетное > 5): ")

    if size.isdigit():
        size = int(size)
        if size % 2 != 0 and size > 5:
            break
        else:
            print("Размер должен быть нечетным и больше 5\n")
    else:
        print("Некорректный ввод! Введи число\n")


print("\n==========================\n")

# Фигура 1
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (i - 1) + "*" + " " * (size - i - 2) + "*")

print("\n==========================\n")
# Фигура 2
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - i - 2) + "*" + " " * (i - 1) + "*")

print("\n==========================\n")
# Фигура 3
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size // 2 - 1) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 4
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")

print("\n==========================\n")
# Фигура 5
for i in range(size):
    if i == 0:
        print("*" * (size // 2 + 1))
    elif i == size - 1:
        print(" " * (size // 2) + "*" * (size // 2 + 1))

    if i >= 1 and i <= size // 2 - 1:
        print("*" + " " * (i - 1) + "*")
    elif i > size // 2 and i < size - 1:
        print(" " * (i) + "*" + " " * (size - i - 2) + "*")
    elif i == size // 2:
        print("*" + " " * (size // 2 - 1) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 6
for i in range(size):
    if i == 0:
        print(" " * (size // 2) + "*" * (size // 2 + 1))
    elif i == size - 1:
        print("*" * (size // 2 + 1))

    if i >= 1 and i <= size // 2 - 1:
        print(" " * (size - i - 1) + "*" + " " * (i - 1) + "*")
    elif i > size // 2 and i < size - 1:
        print("*" + " " * (size - i - 2) + "*")
    elif i == size // 2:
        print("*" + " " * (size // 2 - 1) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 7
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    elif i < size // 2:
        print(
            "*"
            + " " * (i - 1)
            + "*"
            + " " * (size - i - i - 2)
            + "*"
            + " " * (i - 1)
            + "*"
        )
    elif i > size // 2:
        print(
            "*"
            + " " * (size - i - 2)
            + "*"
            + " " * (i + i - size)
            + "*"
            + " " * (size - i - 2)
            + "*"
        )
    else:
        print("*" + " " * (size // 2 - 1) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 8
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" + " " * (size - 2) + "*")
    elif i < size // 2:
        print(
            "*"
            + " " * (i - 1)
            + "*"
            + " " * (size - i - i - 2)
            + "*"
            + " " * (i - 1)
            + "*"
        )
    elif i > size // 2:
        print(
            "*"
            + " " * (size - i - 2)
            + "*"
            + " " * (i + i - size)
            + "*"
            + " " * (size - i - 2)
            + "*"
        )
    else:
        print("*" + " " * (size // 2 - 1) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 9
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    elif i < size // 2:
        print(" " * (i) + "*" + " " * (size - i - i - 2) + "*")
    elif i > size // 2:
        print(" " * (size - i - 1) + "*" + " " * (i + i - size) + "*")
    else:
        print(" " * (size // 2) + "*")


print("\n==========================\n")
# Фигура 10
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("*" * size)
    else:
        print("*" + " " * (size // 2 - 1) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 11
for i in range(size):
    if i == 0:
        print(" " + "*" * (size // 2 - 1))
    elif i == size - 1:
        print(" " * (size // 2 + 1) + "*" * (size // 2 - 1))
    elif i < size // 2:
        print("*" + " " * (size // 2 - 1) + "*")
    elif i == size // 2:
        print(" " + "*" * (size // 2 - 1) + " " + "*" * (size // 2 - 1))
    elif i > size // 2:
        print(" " * (size // 2) + "*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
# Фигура 12
for i in range(size):
    if i == 0:
        print(" " * (size // 2 + 1) + "*" * (size // 2 - 1))
    elif i == size - 1:
        print(" " + "*" * (size // 2 - 1))
    elif i < size // 2:
        print(" " * (size // 2) + "*" + " " * (size // 2 - 1) + "*")
    elif i == size // 2:
        print(" " + "*" * (size // 2 - 1) + " " + "*" * (size // 2 - 1))
    elif i > size // 2:
        print("*" + " " * (size // 2 - 1) + "*")

print("\n==========================\n")
