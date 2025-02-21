# 2. Написать функцию draw_rectangle, выводящую на экран прямоугольник.
# Функция принимает следующие параметры: ширина, высота, символ рамки, символ заполнения.
# Функции должны содержать параметры по умолчанию.

print("\n===================================\n")


def draw_rectangle(width=15, height=5, border="*", fill="@"):
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(str(border), end="")
            else:
                print(str(fill), end="")
        print()


def main():
    draw_rectangle(30, 10, "*", "-")


main()

print("\n===================================\n")
