# 11. Заполнить квадратную матрицу размером M х N по спирали. Число 1 ставится
# в центр матрицы, затем массив заполняется по спирали против часовой стрелки
# значениями по возрастанию.

print("\n===================================\n")

while True:
    size = input("Введите размер квадратной матрицы(3 и более и нечётное): ")

    if size.isdigit() and int(size) >= 3 and int(size) % 2 != 0:
        size = int(size)
        break
    else:
        print("Введите положительное больше 2х и нечётное\n")

num_list = [[0] * size for _ in range(size)]

x = y = size // 2
num_list[y][x] = 1

step = 0
counter_print = 1
i = 0
num = 1
for i in range(size * 2 - 1):
    if step % 2 == 0 and counter_print != size - 1 and step != 0:
        counter_print += 1

    if i % 4 == 0:
        step += 1
        for j in range(counter_print):
            num += 1
            x += 1
            num_list[y][x] = num
        continue
    if i % 4 == 1:
        step += 1
        for j in range(counter_print):
            num += 1
            y -= 1
            num_list[y][x] = num
        continue
    if i % 4 == 2:
        step += 1
        for j in range(counter_print):
            num += 1
            x -= 1
            num_list[y][x] = num
        continue
    if i % 4 == 3:
        step += 1
        for j in range(counter_print):
            num += 1
            y += 1
            num_list[y][x] = num
        continue

print("\n===================================\n")

for i in range(size):
    for j in range(size):
        print(f"{num_list[i][j]:3}", end=" ")
    print("\n")

print("===================================\n")
