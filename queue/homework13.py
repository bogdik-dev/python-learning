coupon = 'sale10'
print(len(coupon))
if len(coupon) > 0:
    print(f"Купон применен {coupon}")
else:
    print("Купон не указан")

weights = ["1.5", "2.0", "0.8"]
it = iter(weights)
step = 1
for i in it:
    i_fload = float(i)
    print(f"{step}: вес {i_fload}кг")
    step += 1

qty_input = "15"
qty = int(qty_input)
if qty > 0:
    print(f"Колличество принято: {qty}шт")
else:
    print("Некорректное число")