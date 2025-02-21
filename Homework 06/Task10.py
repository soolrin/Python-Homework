# 10. Создать список списков размером M х N, заполненный случайными числами
# из диапазона от 0 до 20. Определить сумму для каждой строки и каждого столбца.

import random

print("\n===================================\n")

rows = 5
cols = 7
numbers = [[random.randint(0, 20) for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    sum_row = 0
    for j in range(cols):
        print(f"{numbers[i][j]:3}", end=" ")
        sum_row += numbers[i][j]
    print("|", sum_row, end=" ")
    print()

print(f"-" * (cols * 4))

for i in range(cols):
    sum_col = 0
    for j in range(rows):
        sum_col += numbers[j][i]
    print(f"{sum_col:3}", end=" ")

print("\n\n===================================\n")
