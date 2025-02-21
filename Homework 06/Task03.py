# 3. Написать приложение, которое предлагает пользователю ввести число и затем
# подсчитывает, сколько раз это число встречается в списке из 100 случайных элементов.
import random

print("\n===================================\n")

user_input = int(input("Введите число от 0 до 10: "))
numbers = [random.randint(0, 10) for _ in range(100)]
count = numbers.count(user_input)

print(f"\nСписок: {numbers}")
print(f"\nЧисло {user_input} встречается {count} раз(а).")

print("\n===================================\n")

j = 1
for i in range(len(numbers)):
    if numbers[i] == user_input:
        print(f"{j}) Индекс числа {user_input}: {i}")
        j += 1

print("\n===================================\n")
