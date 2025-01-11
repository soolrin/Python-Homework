# 13. Ввести с клавиатуры шестизначный номер трамвайного (или троллейбусного)
# билета и определить, счастлив ли он (сумма трех первых цифр равна сумме трех последних).

print("\n")

ticket = input("Введите номер билета: ")

print("\n==========================\n")

# Способ через строку
num1 = int(ticket[0])
num2 = int(ticket[1])
num3 = int(ticket[2])
num4 = int(ticket[3])
num5 = int(ticket[4])
num6 = int(ticket[5])

if num1 + num2 + num3 == num4 + num5 + num6:
    print("Билет счастливый")
else:
    print("Билет несчастливый")

print("\n==========================\n")

# Способ через арифметику
num = int(ticket) // 1000
sum_first3 = (num // 100) + (num // 10 % 10) + (num % 10)

num = int(ticket) % 1000
sum_last3 = (num // 100) + (num // 10 % 10) + (num % 10)

if sum_first3 == sum_last3:
    print("Билет счастливый")
else:
    print("Билет несчастливый")

print("\n==========================\n")
