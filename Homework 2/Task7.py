# 7. Напишите приложение, которое предлагает пользователю ввести радиус
# окружности, а затем вычисляет площадь и длину этой окружности. Число Pi
# задается в программе как действительная константа.

print("\n")

R = float(input("Введите радиус окружности: "))
PI = 3.14
S = PI * R**2
L = 2 * PI * R

print("\n")

print("Площадь окружности: ", S)
print("Длина окружности: ", L)

print("\n")
