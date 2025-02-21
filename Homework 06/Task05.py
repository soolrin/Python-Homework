# 5. Даны 2 списка размером M и N соответственно. Необходимо переписать в третий
# список общие элементы двух первых списков без повторений.
import random

print("\n===================================\n")

numbers1 = [random.randint(0, 100) for _ in range(75)]
numbers2 = [random.randint(0, 100) for _ in range(50)]
all_numbers = numbers1 + numbers2

all_numbers.sort()

i = 0
while i < len(all_numbers) - 1:
    if all_numbers[i] == all_numbers[i + 1]:
        all_numbers.pop(i + 1)
    else:
        i += 1
print(all_numbers)

print("\n===================================\n")
