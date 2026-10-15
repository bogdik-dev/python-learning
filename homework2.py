#====метод .append()====

#===Пример1===

fruits = []
fruits.append('банан')
print(fruits)

#===Пример2===
numbers = [10, 20]
numbers.append(5)
numbers.append(15)
numbers.append(25)
print(numbers)

#===Пример3===
mixed = [1, "два", "$$$"]
mixed.append(True)                 #это лигическое значение
mixed.append("True")               #а это уже как слово
print(mixed)

#===Пример4===
'''
while True:                       #бесконечно привет
  print("Привееет!")
'''


name = input("Как тебя зовут?")   #спросит текст и этот текст станет его переменной
print("Привет,", name)


text = " Анна   "
text = text.split()               
print(text)
  #или                            #cтирает пробелы
text = " Анна   "
print(text.split())


text = "СТОП"
print(text.lower())               #Большие буквы становятся маленькими


age = 20
if age >= 18:
   print("взрослый")
else:
   print("ребенок")


while True:
  print( "работаю...") #break останавливает цикл
  break

names = []
while True:
  name = input("Введите имя (или 'стоп' для завершения):").strip()
  if name.lower() == "стоп":
    break
  names.append(name)
print("собранные имена:", names)


#===Пример5===
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("Квадраты чисел:", squares)

scores = []
for _ in range(3):
    score = int(input("Введите балл:"))
    scores.append(score)
print("Средний балл:", sum(scores) / len(scores))

users = []
users.append({"id": 1, "name": "Алекс", "age": 25})
users.append({"id": 2, "name": "Мария", "age": 31})
print(users)



#===Памятка индексы в python===
#===пример1===

animals = ["комп", "мышка", "гитара", "аххахаха"]
print(animals[1])
print(animals[-3])

#===пример2===

products = ["корм для собак", "милфа", "лололошка", "пыщ пыщ",
"витамины"]
print(products[1])
print(products[-2]) 
print(products[3])

#===пример3===

name = "ножницы"
print(name[0])
print(name[-1])
print(name[2:5]) 
cart = ["ква", "мяу", "гав", "ах"]
print(cart[1]) 
print(cart[0:3])

#===пример4===

goods = ["корм для кошек", "игрушка", "акм", "наполнитель", "витамины для собак"]
for i in range(len(goods)):
    if "акм" in goods[i]:
      print(f"Найден товар 'акм' на позиции {i}")
    if "кошка" in goods[i] or "собак" in goods[i]:
      print(f"Товар для животных на позиции {i}: {goods[i]}")


#===срезы строк в Pyhton===
#===пример1===

l = "333-тритритри"
print(l[0:3]) 
print(l[4:7])

#===пример2===

word = "макака"
print(word[2:6]) 
print(word[:5]) 
print(word[:3])

#===пример3===

text = "ЖоскаПиваХочу"
print(text[-4:]) 
print(text[::-1]) 
print(text[5::]) 
print(text[1:8:2])

#===пример4===

code = "АКМ-2026-XYZ-789"
prefix = code[:3]
year = code[4:8]
number = code[-3:]
print("Префикс:", prefix)
print("Год:", int(year))
print("Номер:", number)

clean = code.replace("-", "")
print("Первые 7 символов без дефисов азаазз:", clean[:7])

