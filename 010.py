
def my_len(word):
    c = 0
    for i in word:
        c = c + 1
    return "число символов " + str(c)
print(my_len("Кириллл"))