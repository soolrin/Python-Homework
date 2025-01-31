# 21. Пользователь вводит дату (по отдельности день, месяц, год).
# Определить день недели, соответствующий введенной дате.

print("\n==========================\n")

while True:
    day = input("Введите день (цифрами): ").lstrip("0")
    month = input("Введите месяц (цифрами): ").lstrip("0")
    year = input("Введите год (цифрами): ")

    if not day.isdigit():
        print("Некорректный ввод дня. Повторите попытку.\n")
        continue

    if not month.isdigit() or not (1 <= int(month) <= 12):
        print("Такого месяца не существует. Повторите попытку.\n")
        continue

    if not year.isdigit() or len(year) != 4 or int(year) < 1583:
        print(
            "Некорректный ввод года / Год должен быть не меньше 1583. Повторите попытку.\n"
        )
        continue

    day = int(day)
    month = int(month)
    year = int(year)

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    if month == 2:  # Февраль
        if leap_year and 1 <= day <= 29:
            break  # Если високосный и в диапазоне месяца
        elif not leap_year and 1 <= day <= 28:
            break  # Если не високосный и в диапазоне месяца
        else:
            print("В этом месяце нет такого дня. Повторите.\n")
            continue

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 0 and day <= 30:  # Апрель, Июнь, Сентябрь, Ноябрь
            break  # Если в диапазоне месяца
        else:
            print("В этом месяце нет такого дня. Повторите.\n")
            continue

    else:  # Январь, Март, Май, Июль, Август, Октябрь, Декабрь
        if day > 0 and day <= 31:
            break  # Если в диапазоне месяца
        else:
            print("В этом месяце нет такого дня. Повторите.\n")
            continue

total_day = 0

for past_y in range(1583, year):
    if (past_y % 4 == 0 and past_y % 100 != 0) or past_y % 400 == 0:
        total_day += 366
    else:
        total_day += 365

for past_m in range(1, month):
    if past_m == 2:
        if leap_year:
            total_day += 29
        else:
            total_day += 28
    elif past_m == 4 or past_m == 6 or past_m == 9 or past_m == 11:
        total_day += 30
    else:
        total_day += 31

total_day += day

weekday = (total_day - 1) % 7

print(f"\nВведенная дата: {day:02}.{month:02}.{year}")
print("День недели в эту дату был:", end=" ")
if weekday == 0:
    print("Суббота")
elif weekday == 1:
    print("Воскресенье")
elif weekday == 2:
    print("Понедельник")
elif weekday == 3:
    print("Вторник")
elif weekday == 4:
    print("Среда")
elif weekday == 5:
    print("Четверг")
else:
    print("Пятница")

print("\n==========================\n")
