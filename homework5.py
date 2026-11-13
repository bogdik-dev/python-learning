'''
print([x for x in range(10)])

print([x for x in range(10) if x % 2 == 0])

print([x**2 for x in range(10)])

print([x*y for x in range(3) for y in range(3)])

print([char.upper() for char in "hello"])

name = "Бодян"
age = 20
greeting = f"Привет, {name}! Тебе {age} лет)"
print(greeting)

x = 5
y = 13
result = f"Сумма {x} и {y} равна {y + x}"
print(result)

pi = 3.1415926535
formatted = f"Значение pi примерно {pi:.2f}"
print(formatted)

from datetime import datetime
now = datetime.now()
time_str = f"Текущее премя:{now}"
print(time_str)

a = 10
b = 20
multiline = f"""Это многострочная строка.
Максимум из {a} и {b} - {max(a, b)}.
Минимум - {min(a, b)}."""
print(multiline)

languages = ["Python", "JavaScript", "Java", "C+", "C"]
print([f"{i}: {languages[i]}" for i in range(len(languages))])

items = ["молоток", "дрель", "топор", "рулетка", "пила"]
print([f"{i}: {items[i]}" for i in range(len(items))])

alphabet = "abcaoeinvosdfjlvn"
print([alphabet[i] for i in range(3)])
'''


alphabet = "abcdefghijklmnopqrstuvwxyz"
print([alphabet[i] for i in range(3)])

items = ["молоток", "пила", "дрель", "топор", "рулетка"]
print([str(i) + ": " + items[i] for i in range(len(items))])

languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]
print([f"{i}: {languages[i]}" for i in range(len(languages))])