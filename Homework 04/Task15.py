# 15. Елка со слайда в конце презентации.

level = 6
section = 5

print("\n==========================\n")

for i in range(level):
    for j in range(section):
        if i < level - 1:
            print(" " * (section + section - j - i) + "@" * (j * 2 + 1 + (i * 2)))
        else:
            print(" " * (section + section - 1) + "#" * 3)

print("\n==========================\n")
