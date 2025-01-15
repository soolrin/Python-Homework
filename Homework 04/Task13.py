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

mid = up // 2 + 1
for i in range(1, up + 1):

    if i <= mid:
        space = " " * (mid - i)
        star = "*" * (i * 2 - 1)
        print(space + star)
    else:
        space = " " * (i - mid)
        star = "*" * ((up - i) * 2 + 1)
        print(space + star)

print("\n==========================\n")
