# 1. Напишите функцию draw_line, которую можно будет использовать так: draw_line(20, '@', правда)
# и при этом нащупывать горизонтальную линию, которая складируется из 20 «собачек».
# Я должен указать в оставшемся параметре false — линия становится вертикальной.

print("\n===================================\n")


def draw_line(quantity=5, symbol="*", display=True):
    if display:
        print(str(symbol) * quantity)
    else:
        print(f"{(str(symbol) + '\n') * quantity}")


def main():
    draw_line(10, "@", True)


main()

print("\n===================================\n")
