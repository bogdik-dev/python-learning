#Памятка: if-else vs if-elif-else

#===пример1===

age = 17
if age >=18:
  print("скуф")
else:
  print("пиздюк")

#===пример2===

score = 45
if score >= 60:
  print("Проходной балл")
else:
  print("Не сдал")

#===пример3===

temp = 20
if temp >= 33:
  print("смэрть")
elif temp >= 22:
  print("газ на речку")
elif temp >= 15:
  print("кайф")

#===пример4===

Toyota_Mark_II = 100
if Toyota_Mark_II >=90:
    print ("в столб")
else:
  if Toyota_Mark_II >=80:
      print = ("jz 2 amg")
  else:
      if Toyota_Mark_II >=70:
          print("турбо тачка")

Toyota_Mark = 80
if Toyota_Mark >= 90:
    print("в столб")
elif Toyota_Mark >= 80:
    print("2jz gte")

#Памятка: while + if — как они работают 
#===пример1===
count = 0
while count < 5:
    if count % 2 == 0:
      print(count, "четное")
    count += 1

#===пример2===
i = 1
while i <= 7:
  if i % 3 == 0:
    print(i, "делится на 3")
  i += 1

#===пример3===
attempt = 1
while attempt <= 5:
    guess = input("Угадай число (1–10): ")
    if guess == "7":
      print("Угадал!")
      break
    else:
      print("Не угадал, попытка", attempt)
      attempt += 1

#===пример4===
total = 0
while True:
    num = input("Введи число (0 = стоп): ")
    num = int(num)

    if num == 0:
        break

    if num > 0:
        total += num
    else:
        print("Отрицательное число пропущено")

print("Сумма положительных:", total)
