# 3. Загадать случайным образом 100 целых чисел в диапазоне от -100 до 100.
# Вычислить процент положительных чисел, процент отрицательных чисел
# и процент нулей, а также четных чисел и процент нечетных.

import random

positive = 0
negative = 0
zero = 0
even = 0
odd = 0

print("\n==========================\n")

# Решил сделать 1000 чтобы был смысл считать процент.
for i in range(1000):
    num = random.randint(-100, 100)

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

positive = positive / 1000 * 100
negative = negative / 1000 * 100
zero = zero / 1000 * 100
even = even / 1000 * 100
odd = odd / 1000 * 100

print(f"Процент четных чисел: {even:.1f}%")
print(f"Процент нечетных чисел: {odd:.1f}%")
print(f"Процент положительных чисел: {positive:.1f}%")
print(f"Процент отрицательных чисел: {negative:.1f}%")
print(f"Процент нулей: {zero:.1f}%")

print("\n==========================\n")
