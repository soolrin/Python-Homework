# 3. Пользователь вводит с клавиатуры массу в тоннах (дробное число).
# Вывести количество тонн, килограммов, граммов.
# (Например, ввести 126.456789т – вывести 126т 456кг 789г).

print("\n")

mass = float(input("Введите массу в тоннах: "))

print("\n==========================\n")

t = int(mass)
kg = int((mass - t) * 1000)
g = int(((mass - t) * 1000 - kg) * 1000)

print(f"{t} Тон \n{kg} Килограмм \n{g} Грамм")

print("\n==========================\n")
