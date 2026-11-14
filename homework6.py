
ocenki = [5, 4, 4, 3, 2, 5, 5, 5, 1]
varianty = [1, 2, 3, 4, 5]
for i in varianty:
    count = ocenki.count(i)
    print(f"{i}: {count}")

text = input("Введи пж текст ")
glasnye = ["а", "е", "и", "о", "у"]
for i in glasnye:
    count = text.count(i)
    print(f"{i}: {count}")
