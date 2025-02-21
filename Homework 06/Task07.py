# Создайте список строк на 3999 элементов. Заполнить его римскими числами
# от 1 до 3999 г., показать на экране все элементы.

print("\n===================================\n")

ROMAN_NUMBERS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

roman_numbers = []
for num in range(1, 4000):
    roman_num = ""
    for value in ROMAN_NUMBERS:
        while num >= value:
            roman_num += ROMAN_NUMBERS[value]
            num -= value
    roman_numbers.append(roman_num)

print(roman_numbers)

print("\n===================================\n")
