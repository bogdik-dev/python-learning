'''
weight = 900
distance = 340
content = ["мотоцикл", "компьютер", "стол", "песок"]
def tok(weight, distance, content):
    result = []
    if "мотоцикл" in content:
        result.append("Хрупкое: спецотдел")
    if weight > 20:
        result.append("Тяжелое: грузовой отдел")
    if distance > 500:
        result.append("Дальнее: авиаотдел")
    if distance < 500:
        result.append("Обычное: стандартный отдел")
        return result
print(tok(weight, distance, content))

tislo = int(input("Введите целое, положительное число: "))
result = []
for i in range(tislo, 0, -1):
    result.append(i)
print(result)
'''
quests = ["Богдан", "Алексей", "Федор", "Доминик"]
for i in quests:
    print(f"{i}: состоит из {len(i)} букв")
print(f"Всего гостей в доме: {len(quests)}")
