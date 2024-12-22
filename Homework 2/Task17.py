# 17. Рассчитать общую массу всех планет солнечной системы. Вычислить среднее
# арифметическое масс планет. Затем – массу каждой планеты в процентном
# соотношении, если взять за 100% общую массу всех планет. Во сколько раз
# масса самой большой планеты больше суммы масс всех остальных планет?
# Все результаты – показать на экране.

print("\n")

mercury = 3.301e23
venus = 4.867e24
earth = 5.972e24
mars = 6.417e23
jupiter = 1.899e27
saturn = 5.685e26
uranus = 8.682e25
neptune = 1.024e26

total_mass = mercury + venus + earth + mars + jupiter + saturn + uranus + neptune

average_mass = total_mass / 8


print("\n==========================\n")

print(f"Общая масса всех планет: {total_mass} кг")
print(f"Средняя масса планет: {average_mass} кг")

print(f"\nМасса Меркурия в процентном соотношении: {round(mercury / total_mass * 100, 3)} %")
print(f"Масса Венеры в процентном соотношении: {round(venus / total_mass * 100, 3)} %")
print(f"Масса Земли в процентном соотношении: {round(earth / total_mass * 100, 3)} %")
print(f"Масса Марса в процентном соотношении: {round(mars / total_mass * 100, 3)} %")
print(f"Масса Юпитера в процентном соотношении: {round(jupiter / total_mass * 100, 3)} %")
print(f"Масса Сатурна в процентном соотношении: {round(saturn / total_mass * 100, 3)} %")
print(f"Масса Урана в процентном соотношении: {round(uranus / total_mass * 100, 3)} %")
print(f"Масса Нептуна в процентном соотношении: {round(neptune / total_mass * 100, 3)} %")
print("")

total_mass -= jupiter
print(
    f"Масса самой большой планеты больше суммы масс всех остальных планет в",
    f"{round(jupiter / total_mass, 2)} раза",
) # в 2.5 раза больше если убрать round то 2.467...

print("\n==========================\n")
