stock = "42"
min_stock = "10"
current = int(stock)
min_stock2 = int(min_stock)
if current >= min_stock2:
    print("Пополнения не требуется")
    print(f"Сейчас на складе {current} шт.")
elif current < min_stock2:
    print("нужно пополнить")

orders = ["o21", "o22", "o23", "o24", "o25"]
orders_new = orders[:4]
number = 1
for i in orders_new:
    print(f"Шаг {number}: {i}")
    number += 1

weights = ["2.5", "1.2", "3.0", "2.5", "1.2"]
print(f'Вес 2.5 встречается {weights.count("2.5")} раз(а)')
summa = 0
for i in weights:
    summa += float(i)
cp_summa = summa / len(weights)
print(f"Средний вес {cp_summa}")
