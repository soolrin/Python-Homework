# 1. Пользователь вводит с клавиатуры два дробных числа. Вывести на экран
# сумму целых частей и сумму дробных. К примеру, для чисел 12.34 и 56.78
# это будет 68 и 1.12

print("\n")


num1 = float(input("Введите первое дробное число: "))
num2 = float(input("Введите второе дробное число: "))

print("\n==========================\n")

sum_int = int(num1) + int(num2)
sum_float = num1 - int(num1) + num2 - int(num2)
print(f"Сумма целых чисел: {sum_int} Сумма дробных чисел: {sum_float:.2f}")

print("\n==========================\n")
