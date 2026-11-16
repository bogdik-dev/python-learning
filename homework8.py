
numbers = [x for x in range(2,11)] + ["Валет", "Дама", "Король", "Туз"]
masti = ["♠", "♥", "♦", "♣"]
kart = []
for i in masti:
    for i2 in numbers:
        kart.append(f"{i2}{i}")
kart.append("🔴 Джокер")
kart.append("⚫ Джокер")
print(kart)


code = "AB--12--CD"
number = code.count("-")
print(f"Дефисов найдено {number}")
while "-" in code:
    code = code.replace("-", "", 1)
print(code)
dlina = len(code)
print(f"Длина {dlina}")

stock_a = ["книга", "ручка"]
stock_b = ["тетрадь", "карандаш"]
if "ручка" in stock_a:
    print(True)
else:
    print(False)
print(stock_a + stock_b)

warehouses = [["Книга", "Ручка"], ["Тетрадь", "Карандаш", "Ластик"]]
for sklad in warehouses:
    for tovar in sklad:
        print(tovar)
for sklad in warehouses:
    print(sklad[:2])
