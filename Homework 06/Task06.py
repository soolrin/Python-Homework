# 6. Реализовать программу-лотерею. Программа задает 5 случайных уникальных чисел
# в диапазоне от 1 до 42, но не показывает их на экран. Пользователь пытается
# угадать их – вводит свои 5 чисел с клавиатуры. Назначить призы за совпадения:
# например, если пользователь угадал три числа – приз 100 гривен,
# если 4 – 500 гривен, если 5 – 2500 гривен.
import random

print("\n===================================\n")

user_numbers = []
print("Введите число от 1 до 42 (не повторяющиеся)\n")
while len(user_numbers) < 5:
    user_num = int(input(f"{(len(user_numbers) + 1)}) "))
    if user_num <= 42 and user_num >= 1 and user_num not in user_numbers:
        user_numbers.append(user_num)
    else:
        print(
            f"\n{"-" *25}\nЧисло {user_num} не удовлетворяет условиям. Повторите ввод.\n{"-" *25}"
        )
        print("Введите число от 1 до 42 (не повторяющиеся)\n")

numbers = []
while len(numbers) < 5:
    num = random.randint(1, 42)
    if num not in numbers:
        numbers.append(num)

count = 0
print("\nВы угадали:", end=" ")
for num in user_numbers:
    if num in numbers:
        count += 1
        print(num, end=" ")

if count == 1:
    print(f"\nВы угадали {count} число. Спасибо за участие")
elif count == 2:
    print(f"\nВы угадали {count} числа. Приз: 50 гривен")
elif count == 3:
    print(f"\nВы угадали {count} числа. Приз: 100 гривен")
elif count == 4:
    print(f"\nВы угадали {count} числа. Приз: 500 гривен")
elif count == 5:
    print(f"\nВы угадали {count} чисел. Приз: 2500 гривен")
else:
    print(f"-------\nВы не угадали число.")

print(numbers)

print("\n===================================\n")
