# 4. Написать программу, вычисляющую факториал введенного числа.

print("\n")

factorial = int(input("Факториал какого числа вы хотите узнать? : "))

print("\n==========================\n")

if factorial == 0 or factorial == 1:
    print(f"Факториал числа {factorial}! = 1")
elif factorial > 1:
    fact = 1
    for i in range(1, factorial + 1):
        fact *= i
    print(f"Факториал числа {factorial}! = {fact}")
else:
    print("Введенное число не является положительным целым числом")


print("\n==========================\n")
