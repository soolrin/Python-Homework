# 2. Пользователь вводит с клавиатуры два числа. Первое число – это значение,
# второе число – процент, который нужно сосчитать. Надо вывести на экран процент

print("\n")

num = float(input("Введите число: "))
percent = float(input("Введите процент: ")) / 100

print("\n")

percentage_value = num * percent
print("Процент от числа", num, "составил", percentage_value)

print("\n")
