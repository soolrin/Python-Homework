# 22. Написать программу, которая генерирует и выводит календарь на любой год
# указанный с клавиатуры.

print("\n==========================\n")

while True:
    year = input("Введите год (цифрами): ")

    if year.isdigit() and int(year) >= 1583:
        year = int(year)
        break
    else:
        print(
            "Некорректный ввод года / Год должен быть не меньше 1583. Повторите попытку.\n"
        )
        continue

total_day = 0

for past_y in range(1583, year):
    if (past_y % 4 == 0 and past_y % 100 != 0) or past_y % 400 == 0:
        total_day += 366
    else:
        total_day += 365

day = 0
count = 0

for m in range(1, 12 + 1):
    if m == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day = 29
        else:
            day = 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        day = 30
    else:
        day = 31

    if m == 1:
        m_name = "Январь"
    elif m == 2:
        m_name = "Февраль"
    elif m == 3:
        m_name = "Март"
    elif m == 4:
        m_name = "Апрель"
    elif m == 5:
        m_name = "Май"
    elif m == 6:
        m_name = "Июнь"
    elif m == 7:
        m_name = "Июль"
    elif m == 8:
        m_name = "Август"
    elif m == 9:
        m_name = "Сентябрь"
    elif m == 10:
        m_name = "Октябрь"
    elif m == 11:
        m_name = "Ноябрь"
    elif m == 12:
        m_name = "Декабрь"

    print("\n")  # отображение рамок календаря
    print("=" * 32)
    print(f"|  {m_name:^26}  |")
    print("=" * 32)
    print(f"|  {"Пн":<4}{"Вт":<4}{"Ср":<4}{"Чт":<4}{"Пт":<4}{"Сб":<4}{"Вс":<4}|")
    print(f"|  ", end="")

    for d in range(1, day + 1):  # вывод самого календаря
        if d == 1:
            print("    " * ((total_day + 5) % 7), end="")
            count = (total_day + 5) % 7
            total_day += day

        print(f"{d:<4}", end="")
        count += 1

        if count % 7 == 0:
            print("|")
            print(f"|  ", end="")
            count = 0

    count = (7 - count) * 4  # отображение рамок календаря
    print(" " * count, end="|")
    print()
    print("=" * 32)

print("\n==========================\n")
