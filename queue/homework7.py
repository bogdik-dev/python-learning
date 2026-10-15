
def convert(price, qty):
    price = int(price)
    qty = int(qty)
    total = price * qty
    return total
result = convert("150", "3")
print(f"{result} ({type(result)})")


weights = [2, 5, 1]
def delivery_cost(weight, rate, base_price):
    return base_price + weight * rate

for weight in weights:
    total = delivery_cost(weight, 50, 100)
    print(f"Посылка {weight} кг; Стоимость {total} руб.")


log = "ORDER-2024-00458-DELIVERED"
nove_log = log.split("-")
odno = nove_log[2][:4]
statys = nove_log[3]
print(f"Номер заказа(срез):{odno}")
print(f"Статус: {statys}")

count = 10
new_orders = "5"
orders = int(new_orders)
count += orders
print(f"Всего заказов: {count} {type(count)}")

statuses = ["active", "inactive", "active", "active", "inactive"]
def count_active(statuses):
    i2 = 0
    for i in statuses:
        if i == "active":
            i2 += 1
    return i2
stat = statuses[:3]
print(f"Первые три: {stat}")
print(f"Активных пользователей: {count_active(statuses)}")

stock = ["Книга", "Ручка", "Тетрадь"]
item = "Карандаш"
try:
    if item not in stock:
        raise ValueError("Товара ныма")
    print("Товар на базе")
except ValueError as e:
    print(e)

toys = 10
boyers = 0
try:
    share = toys / boyers
    print(share)
except ZeroDivisionError:
    print("мяу")

input_price = "two_hundred"
try:
    price = int(input_price)
    print(price)
except ValueError:
    print("ошибочка по типу данных")

shelf = ["akm_cat_bowl", "akm_dog_bed"]
try:
    item = shelf[10]
    print(item)
except IndexError:
    print("номера нет в списке")

warehouse = {"akm_fish_food": 50}
try:
    amount = warehouse["akm_turtle_food"]
    print(amount)
except KeyError:
    amount = 0
    print("товар отсутствует")
    print(f"готово к упаковке: {amount}")

try:
    price = int("сузуки")
except ValueError as err:
    print(f"ошибка: {err}")

warehouse = {"кол-во чая": 10}
try:
    count = warehouse["кефир"]
except KeyError as err:
    print(f"сегодня без:{err}")

cage_list = ["печаль", "грусть"]
try:
    selected = cage_list[2]
except IndexError as err:
    print(f"ошибка: {err}")

client_record = {"name": "ivan", "age": "twenty"}
try:
    client_age = int(client_record["age"])
    print(f"скидка:{client_age * 0.1}%")
except (ValueError, TypeError) as err:
    print(f"ошибка:{err}")

for i in range(3):
    print(f"время идет {i+1}")

toys = ["паша", "маша", "света"]
for i in toys:
    print(f"дежурный: {i}")

sku_label = "хуй"
for i in sku_label:
    print(f"символ: {i}")

orders = ["юпитер", "планета", "восход", "юпитер", "минск"]
cage_count = 0
for order in orders:
    if order == "юпитер":
        cage_count += 1
print(f"Всего юпитеров: {cage_count}")

orders = ["ORD1", "ORD2", "ORD4", "ORD5", "ORD6"]
order1 = orders[0::2]
order2 = orders[::-1]
print(f"Через один: {order1}")
print(f"Обратный порядок: {order2}")