# 4. Написать функцию, которая получает в качестве параметров 2 целые числа
# и возвращает сумму чисел из диапазона между ними.

print("\n===================================\n")


def range_sum(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    return sum(range(num1, num2 + 1))


def main():
    print(range_sum(0, 2))


main()

print("\n===================================\n")
