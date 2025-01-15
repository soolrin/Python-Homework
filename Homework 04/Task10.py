# 10. Написать игру «Угадай число». Пользователь мысленно загадывает
# число от 0 до 1000, компьютер угадывает его за минимальное количество попыток.

print("\n")

print("\n==========================\n")

left = 0
right = 1000
count = 0

while left <= right:
    count += 1
    mid_range = (left + right) // 2

    print(f"Наверно ваше число: {mid_range}")
    print(
        "1) Ваше число больше? ( 1 или > )\n"
        "2) Ваше число меньше? ( 2 или < )\n"
        "3) Это ваше число?    ( 3 или = )\n"
    )

    answer = input("Ваш ответ: ")

    if answer == "1" or answer == ">":
        left = mid_range + 1
    elif answer == "2" or answer == "<":
        right = mid_range - 1
    elif answer == "3" or answer == "=":
        print(f"Я угадал за {count} попытку(ок)")
        break

print("\n==========================\n")
