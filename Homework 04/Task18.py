# 18. Показать на экране все восьмизначные числа, цифры которых не повторяются
# и которые делятся на 12345 без остатка.

print("\n==========================\n")

number = 0
number_count = 0
line_count = 0

for one in range(1, 10):
    for two in range(10):
        if two == one:
            continue
        for three in range(10):
            if three == one or three == two:
                continue
            for four in range(10):
                if four == one or four == two or four == three:
                    continue
                for five in range(10):
                    if five == one or five == two or five == three or five == four:
                        continue
                    for six in range(10):
                        if (
                            six == one
                            or six == two
                            or six == three
                            or six == four
                            or six == five
                        ):
                            continue
                        for seven in range(10):
                            if (
                                seven == one
                                or seven == two
                                or seven == three
                                or seven == four
                                or seven == five
                                or seven == six
                            ):
                                continue
                            for eight in range(10):
                                if (
                                    eight == one
                                    or eight == two
                                    or eight == three
                                    or eight == four
                                    or eight == five
                                    or eight == six
                                    or eight == seven
                                ):
                                    continue

                                number += one * 10000000
                                number += two * 1000000
                                number += three * 100000
                                number += four * 10000
                                number += five * 1000
                                number += six * 100
                                number += seven * 10
                                number += eight * 1

                                if number % 12345 == 0:
                                    print(f"{number}", end=" ")
                                    line_count += 1
                                    number_count += 1
                                if line_count == 10:
                                    print("")
                                    line_count = 0
                                number = 0

print("\n\n==========================\n")

print(f"Всего таких чисел: {number_count}")

print("\n==========================\n")
