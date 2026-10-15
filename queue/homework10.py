prices = [250, 480, 150, 600, 90]
total = 0
for i in range(len(prices)):
    total += prices[i]
total = str(total)
print(f"Итого: {total} рублей")

sku = ["A10", "A11", "A12", "A13", "A14", "A15"]
nev_sku = sku[1:5]
iterator = iter(nev_sku)
for i in range(len(nev_sku)):   #for item in iterator:
    print(next(iterator))       #    print(item)

codes = ["D1", "D2", "D1", "D3", "D1", "D2"]
d1 = codes.count("D1")
if d1 % 2 == 0:
    print("четное")
else:
    print("не четное")
print(f"D1 встречается {d1} раз")