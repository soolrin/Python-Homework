# 12. В кинотеатре M рядов по N мест в каждом. В списке списков хранится информация
# о проданных билетах. Число 1 означает, что билет на это место уже продан,
# число 0 означает, что место свободно. Поступил запрос на продажу билетов
# K на соседние места в одном ряду. Определите, можно ли выполнить этот запрос.
# Количество занятых мест и какие места заняты к моменту запроса определяется
# случайным образом. Вывести исходный список на экран консоли.

print("\n===================================\n")

import random

rows = 5
columns = 8
request = 3

places = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]

for row in places:
    print(row)

free_places = {}
free_places_row = []

for i in range(rows):
    count = 0
    free_places_row.clear()
    for j in range(columns):
        if places[i][j] == 0:
            count += 1
            free_places_row.append(j + 1)
        else:
            if count >= request:
                if i + 1 in free_places.keys():
                    free_places[i + 1].extend(free_places_row)
                else:
                    free_places[i + 1] = free_places_row.copy()
            free_places_row.clear()
            count = 0

print("\n===================================\n")

if free_places:
    print(
        f"Можно продать {request} билета(ов) подряд в одном ряду."
        "\nПодходящии доступные места"
    )
    for i in free_places.keys():
        print(f"Ряд {i}: {", ".join(map(str, free_places[i]))}")
else:
    print(f"Невозможно продать {request} билета(ов) подряд в одном ряду.")

print("\n===================================\n")
