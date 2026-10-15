
names = ["Гоша", "Святослав", "Дарина"]
#print(names[2].count("а"))


def my_count(let, word):
    c = 0
    for i in word:
        if i == let:
            c = c + 1
    return c
print(my_count("а", "Дарина"))
print(my_count("в", names[1]))