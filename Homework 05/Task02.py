# 2. Подсчитать, сколько раз определенное слово содержится в строке текста.

import re

print("\n===================================\n")

text = input("Напишите свой текст: ")
word = input("\nВведите слово для подсчета: ")

print(f"\n{"Через стандартные методы":=^35}\n")

while True:
    select = input(
        '"1" Для подсчета с учетом регистра\n'
        '"2" Для подсчета без учета регистра\n'
        "\nВыберите вариант: "
    )
    if select == "1":
        break
    elif select == "2":
        word = word.lower()
        text = text.lower()
        break

# Надо учитывать знаки препинания
list_text = text.replace("\n", " ").replace(",", "").replace(".", "").split()

print(f"\nСлово встречается в тексте: {list_text.count(word)}")

print(f"\n{"Через регулярные выражения":=^35}\n")

found = re.findall(r"\b" + word + r"\b", text)
print(f"Слово встречается в тексте: {len(found)}")
