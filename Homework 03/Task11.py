# 11. Пользователь задает координаты верхнего левого и нижнего правого угла
# прямоугольника, а также координаты точки (X, Y).
# Проверить, принадлежит ли точка этому прямоугольнику.

print("\n")

left_up_x = int(input("Введите координату X верхнего левого угла: "))
left_up_y = int(input("Введите координату Y верхнего левого угла: "))

right_down_x = int(input("\nВведите координату X нижнего правого угла: "))
right_down_y = int(input("Введите координату Y нижнего правого угла: "))

x = int(input("\nВведите координату X точки: "))
y = int(input("Введите координату Y точки: "))

print("\n==========================\n")

if left_up_x <= x <= right_down_x and left_up_y <= y <= right_down_y:
    print("Точка принадлежит прямоугольнику")
else:
    print("Точка не принадлежит прямоугольнику")

print("\n==========================\n")
