# 8. Проверить, есть ли во введенном числе одинаковые цифры подряд.

print("\n")

while True:
    num = input("Введите число: ").lstrip("-")

    if num.isdigit() and len(num) > 1:
        break
    else:
        print("Введите целое число и длиной больше 1 символа")

print("\n==========================\n")

for i in range(len(num) - 1):
    if num[i] == num[i + 1]:
        print("Есть одинаковые цифры подряд")
        break
else:
    print("Нет одинаковых цифры подряд")

print("\n==========================\n")
