# 23. Ввести любую дату (день, месяц, год) и проверить корректность вводимых значений.
# Вывести дату на следующий день.

print("\n")

data = input("Введите дату в формате ( дд.мм.гггг ): ")


print("\n==========================\n")

if len(data) == 10:

    day = data[0:2]
    month = data[3:5]
    year = data[6:]

    if day.isdigit() and month.isdigit() and year.isdigit():

        day = int(day)
        month = int(month)
        year = int(year)

        next_day = 0
        next_month = 0
        next_year = year
        # Високосный ли год
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_year = True
        else:
            leap_year = False

        if 1 <= month <= 12:
            match month:
                # Январь
                case 1:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 2
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В январе нет {day} дня."
                            f"В январе максимум 31 дней."
                        )
                # Февраль
                case 2:
                    if 0 < day <= (29 if leap_year else 28):
                        if day == (29 if leap_year else 28):
                            next_day = 1
                            next_month = 3
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В феврале нет {day} дня. "
                            f"В феврале максимум {29 if leap_year else 28} дней."
                        )
                # Март
                case 3:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 4
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В марте нет {day} дня. "
                            f"В марте максимум 31 дней."
                        )
                # Апрель
                case 4:
                    if 0 < day <= 30:
                        if day == 30:
                            next_day = 1
                            next_month = 5
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В апреле нет {day} дня. "
                            f"В апреле максимум 30 дней."
                        )
                # Май
                case 5:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 6
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В мае нет {day} дня. " f"В мае максимум 31 дней."
                        )
                # Июнь
                case 6:
                    if 0 < day <= 30:
                        if day == 30:
                            next_day = 1
                            next_month = 7
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В июне нет {day} дня. "
                            f"В июне максимум 30 дней."
                        )
                # Июль
                case 7:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 8
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В июле нет {day} дня. "
                            f"В июле максимум 31 дней."
                        )
                # Август
                case 8:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 9
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В августе нет {day} дня. "
                            f"В августе максимум 31 дней."
                        )
                # Сентябрь
                case 9:
                    if 0 < day <= 30:
                        if day == 30:
                            next_day = 1
                            next_month = 10
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В сентябре нет {day} дня. "
                            f"В сентябре максимум 30 дней."
                        )
                # Октябрь
                case 10:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 11
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В октябре нет {day} дня. "
                            f"В октябре максимум 31 дней."
                        )
                # Ноябрь
                case 11:
                    if 0 < day <= 30:
                        if day == 30:
                            next_day = 1
                            next_month = 12
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В ноябре нет {day} дня. "
                            f"В ноябре максимум 30 дней."
                        )
                # Декабрь
                case 12:
                    if 0 < day <= 31:
                        if day == 31:
                            next_day = 1
                            next_month = 1
                            next_year = year + 1
                        else:
                            next_day = day + 1
                            next_month = month
                    else:
                        print(
                            f"Ошибка: В декабре нет {day} дня. "
                            f"В декабре максимум 31 дней."
                        )
        else:
            print(f"Ошибка: Неизвестный месяц {month}. В году максимум 12 мес.")

        if next_day and next_month:
            print(
                f"Дата на следующий день: {next_day:02}.{next_month:02}.{next_year:04}"
            )

    else:
        print(f"Неверно введена дата {data} нужный формат ( дд.мм.гггг )")
else:
    print(f"Неверно введена дата {data} нужный формат ( дд.мм.гггг )")

print("\n==========================\n")
