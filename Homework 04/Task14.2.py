# 13. Написать программу, которая выводит на экран ромб.

print("\n")

while True:
    up = input("Введите высоту роба (Не четную): ")
    if up.isdigit():
        up = int(up)
        if up > 1 and up % 2 != 0:
            break
        else:
            print("Высота должна быть больше 1 и не четная\n")
    else:
        print("Некорректный ввод! Введи число\n")

print("\n==========================\n")

n = 14
m = 10

for i in range(m):
    print(" " * i + "*" * n + "\n")


for i in range(m):
    print(" " * (i * 2) + "***")
    print(" " * (i * 2 + 2) + "*")

for i in range(m * 2):
    if i % 2 == 0:
        print(" " * i + "***")
    else:
        print(" " * (i + 1) + "*")


print("\n==========================\n")
