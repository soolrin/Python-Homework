# 3. Напишите программу, которая генерирует пароль указанной длины.

import random

print("\n===================================\n")

while True:
    pass_len = input("Укажите длину пароля (не меньше 10): ")

    if pass_len.isdigit() and int(pass_len) >= 10:
        pass_len = int(pass_len)
        break
    else:
        print("Введите целое число больше или равное 10\n")

# Чтобы не подключать string
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "@#$%^&*()-_=+[]{}|;."

symbol = lower + upper + digits + special

print("\n===================================\n")

password = "".join(random.choice(symbol) for _ in range(pass_len))
password = list(password)

part = int(pass_len / 3)  # 1/3 от числа
temp = 0
# Гарантированно добавляем буквы верхнего регистра/цифры/спецсимволы 1/3 2/3 3/3
password[random.randint(temp, part)] = random.choice(upper)
temp = part
password[random.randint(temp, 2 * part)] = random.choice(digits)
temp = 2 * part
password[random.randint(temp, 3 * part)] = random.choice(special)

password = "".join(password)
print(password)

print("\n===================================\n")
