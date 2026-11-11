order_str = "яблоко,груша,банан"
new_order = order_str.split(",")
def show_items(new_order):
    new_order = [x.upper() for x in new_order]
    print(new_order)
show_items(new_order)

import random
count = 0
while count < 5:
    random.randint(100,999)
    print("Заказ номер:", random.randint(100,999))
    count += 1

def calc_delivery(weight_str):
    try:
        weight_float = float(weight_str)
        save = weight_float * 50
        print("Стоимость доставки:", save)
    except ValueError:
        print("Ошибка: неверный вес")
calc_delivery(3.5)
calc_delivery('abc')

accepted = list()
qty_list = ["3", "0", "5", "-2"]
for i in range(len(qty_list)):
    i2 = int(qty_list[i])
    if i2 > 0:
        accepted.append(i2)
print(accepted)

codes = ["a1", "b2", "c3"]
upper_codes = list()
for i in range(len(codes)):
    upper_codes.append(codes[i].upper())
print(upper_codes)

stock = ["4", "0", "7"]
available = list()
for i in range(len(stock)):
    if int(stock[i]) > 0:
        available.append("В наличии")
    else:
        available.append("Нет в наличии")
print(available)