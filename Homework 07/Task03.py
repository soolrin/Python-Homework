# 3. Написать функцию, которая проверяет, передано ли ей число простым
# (и возвращает True или False). Число называется простым, если оно
# делится без остатка только на себя и единицу.

print("\n===================================\n")


def prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:
            return False
    return True


def main():
    print("Простое") if prime_number(7) else print("Не простое")


main()

print("\n===================================\n")
