# 4. Определить, какая буква в тексте встречается чаще всего.

import re

print(f"\n{"Инициализация":=^35}\n")

text = input("Напишите свой текст: ")

text = re.sub(r"[^а-яА-ЯёЁ]", "", text)
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

print(f"\n{"Вариант через словарь":=^35}\n")
if text:
    dict_alphabet = {c: 0 for c in alphabet}

    for char in text:
        dict_alphabet[char] += 1

    max_v = max(dict_alphabet.values())

    list_char = [char for char in dict_alphabet if dict_alphabet[char] == max_v]

    print(f"Буква(ы) {list_char} встречается чаще всего: {max_v} раз(а)")
else:
    print("Текст пустой")

print(f"\n{"Вариант через перебор букв":=^35}\n")

list_char.clear()
count = 0

if text:
    for char in alphabet:
        if count < text.count(char):
            count = text.count(char)
            letter = char
    list_char.append(letter)

    for char in alphabet:
        if count == text.count(char) and char != letter:
            list_char.append(char)

    print(f"Буква(ы) {list_char} встречается чаще всего: {count} раз(а)")
else:
    print("Текст пустой")

print("\n===================================\n")
