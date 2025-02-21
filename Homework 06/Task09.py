# 9. Создать список списков размером M х N, заполненный случайными числами из диапазона
# от -10 до 10. Определить количество положительных, отрицательных и нулевых элементов.

import random

print("\n===================================\n")

rows = 5
cols = 5
numbers = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

pos_neg = {"negative": 0, "zero": 0, "positive": 0}

for row in numbers:
    for elem in row:
        print(f"{elem:3}", end=" ")
        if elem < 0:
            pos_neg["negative"] += 1
        elif elem == 0:
            pos_neg["zero"] += 1
        else:
            pos_neg["positive"] += 1
    print()

print("\n===================================\n")

print("Количество нулевых:", pos_neg["zero"])
print("Количество положительных:", pos_neg["positive"])
print("Количество отрицательных:", pos_neg["negative"])

print("\n===================================\n")
