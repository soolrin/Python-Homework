# 6. Пользователь вводит с клавиатуры дробное число с длинным хвостом.
# Округлите его до двух знаков после точки.

print("\n")

num = float(input("Введите дробное число с длинным хвостом: "))

print("\n==========================\n")

print(f"Округленное число: {num:.2f}")
num = round(num, 2)
print(f"Округленное число: {num}")

print("\n==========================\n")
