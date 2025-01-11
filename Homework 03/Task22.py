# 22. Пользователь вводит с клавиатуры время начала и завершения телефонного разговора.
# Подсчитать стоимость разговора, если стоимость минуты 15 копеек.

print("\n")

start_time = input("Введите время начала разговора в формате (чч:мм): ")
start_hour = int(start_time[:2])
start_minute = int(start_time[3:])

end_time = input("Введите время завершения разговора в формате (чч:мм): ")
end_hour = int(end_time[:2])
end_minute = int(end_time[3:])

print("\n==========================\n")

if 0 <= start_hour <= 23 and 0 <= end_hour <= 23:
    if 0 <= start_minute <= 59 and 0 <= end_minute <= 59:

        total_start_time = start_hour * 60 + start_minute
        total_end_time = end_hour * 60 + end_minute

        if total_end_time > total_start_time:

            cost_of_call = (total_end_time - total_start_time) * 15

            print(
                f"Длительность разговора: "
                f"{(total_end_time - total_start_time) // 60} Часов "
                f"{(total_end_time - total_start_time) % 60} Минут."
                f"  ({(total_end_time - total_start_time)} мин)"
            )

            print(
                f"Стоимость разговора: {cost_of_call // 100} Гривен. "
                f"{cost_of_call % 100} Копеек.  ({cost_of_call} коп)"
            )

        elif total_end_time < total_start_time:

            total_end_time += 24 * 60
            cost_of_call = (total_end_time - total_start_time) * 15

            print(
                f"Длительность разговора: "
                f"{(total_end_time - total_start_time) // 60} Часов "
                f"{(total_end_time - total_start_time) % 60} Минут."
                f"  ({(total_end_time - total_start_time)} мин)"
            )

            print(
                f"Стоимость разговора: {cost_of_call // 100} Гривен. "
                f"{cost_of_call % 100} Копеек.  ({cost_of_call} коп)"
            )
    else:
        print("Минуты должны быть от 0 до 60")
else:
    print("Часы должны быть от 0 до 23")

print("\n==========================\n")
