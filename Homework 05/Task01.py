# 1. Подсчитать среднюю длину слова во введенном тексте.

import re

print("\n===================================\n")

text = input("Напишите ваш текст: ")

print("\n===================================\n")

# Простой и короткий но надо учитывать знаки препинания
word_count = text.count(" ") + 1
new_text = text.replace("\n", "").replace(" ", "").replace(",", "").replace(".", "")
length = len(new_text)

print(f"Средняя длина слова в тексте: {length / word_count:.2f}")

print(f"\n{"Через регулярные выражения":=^35}\n")

words = re.findall(r"[а-яА-ЯёЁ́-]+(?:-[а-яА-ЯёЁ]+)*", text)

avg_num_words = 0
if words:
    for word in words:
        word = re.sub(r"[^а-яА-ЯёЁ]+", "", word)
        avg_num_words += len(word)

    avg_num_words /= len(words)
else:
    print("В тексте нет слов")
print(f"Средняя длина слова в тексте: {avg_num_words:.2f}")

print(f"\n{"Через стандартные методы":=^35}\n")

new_text = ""
avg_num_words = 0

for symbol in text:  # в "" там символ ударения
    if symbol.isalpha() or symbol == "-" or symbol == "́":
        new_text += symbol
    else:
        new_text += " "

new_text = new_text.split()

for word in new_text:  # в "" там символ ударения
    avg_num_words += len(word.replace("-", "").replace("́", ""))

avg_num_words /= len(new_text)
print(f"Средняя длина слова в тексте: {avg_num_words:.2f}")

print("\n===================================\n")
