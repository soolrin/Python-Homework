# 6. Написать функцию, показывающую на экране минимум и максимум
# (значение и индекс) среди элементов переданного ей списка.

print("\n===================================\n")


def min_max(list_num=[]):
    if not list_num:
        return print("Список пуст")

    min_val = min(list_num)
    max_val = max(list_num)
    min_index = [i for i in range(len(list_num)) if list_num[i] == min_val]
    max_index = [i for i in range(len(list_num)) if list_num[i] == max_val]

    print(f"Минимальное значение: {min_val}, индексы: {min_index}")
    print(f"Максимальное значение: {max_val}, индексы: {max_index}")


def main():
    min_max([1, 22, 34, 25, 1])


main()

print("\n===================================\n")
