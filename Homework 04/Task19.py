# 19. Написать программу, которая выводит на экран все простые
# числа в диапазоне от 2 до 10.000.000.

import math

# Можно и не использовать math, но тогда вывод всех чисел займет очень много время.
# Варианты без использования math будут ниже в комментариях.

print("\n==========================\n")

line_count = 0
for i in range(2, 10000000):
    is_prime = True

    for j in range(2, int(math.sqrt(i)) + 1):  # range(2, i) или же range(2, i // 2)
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        line_count += 1
        print(i, end=" ")
        if line_count % 10 == 0:
            print()

print("\n==========================\n")

