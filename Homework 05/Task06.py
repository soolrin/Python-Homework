# 6. Написать программу, которая подсчитывает количество слов, а также гласных
# и согласных букв в строке, введенной пользователем. Дополнительно вывести
# количество знаков препинания, цифр и других символов. Учесть, что между
# словами (а также до и после слов) может быть более одного пробела.
# Пример вывода программы: Всего символов в строке текста - 38, из них:
# Слов - 6 Гласных букв - 12 Согласных букв - 21 Знаков препинания - 2 Цифр - 0
# Других символов - 3

print(f"\n{"Инициализация":=^35}\n")

text = input("Введите текст: ").lower()

vowels = list("ауоиэыяюеё")
consonants = list("бвгджзйклмнпрстфхцчшщ")
punctuation = list(".,!?:—…«’»„“();-/'\\*“”‘\"")
digits = list("0123456789")

char_dict = {}

print("\n===================================\n")

for char in text:
    char_dict[char] = char_dict.get(char, 0) + 1

vowels_sum = sum(char_dict.get(key, 0) for key in vowels)
consonants_sum = sum(char_dict.get(key, 0) for key in consonants)
punctuation_sum = sum(char_dict.get(key, 0) for key in punctuation)
digits_sum = sum(char_dict.get(key, 0) for key in digits)
others_sum = len(text) - (vowels_sum + consonants_sum + punctuation_sum + digits_sum)

print(f"Всего символов в строке текста - {len(text)}")
print(f"Количество символов в тексте без пробелов - {len(text.replace(" ", ""))}")
print(f"Слов - {len(text.split())}")
print(f"Гласных букв - {vowels_sum}")
print(f"Согласных букв - {consonants_sum}")
print(f"Знаков препинания - {punctuation_sum}")
print(f"Цифр - {digits_sum}")
print(f"Других символов (Без пробелов) - {others_sum - char_dict.get(" ", 0)}")
print(f"Других символов (С пробелами) - {others_sum}")

print("\n===================================\n")
