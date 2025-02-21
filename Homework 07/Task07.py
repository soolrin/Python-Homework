# 7*. Написать функцию, которая принимает две даты
# (т.е. функция принимает шесть параметров)
# и рассчитывает разницу в днях между этими датами.

print("\n===================================\n")


def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year(year):
        return 29
    return days_in_months[month - 1]


def calc_days(year, month, day):
    total_days = 0

    for y in range(1, year):
        total_days += 366 if leap_year(y) else 365

    for m in range(1, month):
        total_days += days_in_month(m, year)

    total_days += day

    return total_days


def date_difference(day1, month1, year1, day2, month2, year2):
    data1 = calc_days(year1, month1, day1)
    data2 = calc_days(year2, month2, day2)

    if data1 > data2:
        return data1 - data2
    else:
        return data2 - data1


def main():
    print("Прошло дней:", date_difference(4, 8, 1882, 10, 1, 2020))


main()


print("\n===================================\n")
