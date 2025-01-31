# 8. Определить, есть ли строка палиндрома.

import re

print(f"\n{"Инициализация":=^35}\n")

text = input("Проверьте текст на палиндром: ")

text = text.lower()
text = re.sub(r"[^а-я]", "", text)
reversed_text = text[::-1]

print("\n===================================\n")

if text == reversed_text:
    print("Это палиндромом.")
else:
    print("Это не палиндромом.")

print("\n===================================\n")
