# 9. Определить, является ли введенное число палиндромом.
# Палиндром — это число, которое одинаково читается как слева направо,
# так и справа налево, например 1234321. В этой задаче (как и в других задачах)
# нельзя использовать строки и списки.

print("\n")

while True:
    num = input("Введите число: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Введите целое положительное число")

print("\n==========================\n")

original_num = num
reversed_num = 0

while num > 0:
    last_num = num % 10
    reversed_num = reversed_num * 10 + last_num
    num //= 10

if original_num == reversed_num:
    print(f"Число {original_num} является палиндромом.")
else:
    print(f"Число {original_num} не является палиндромом.")

print("\n==========================\n")
