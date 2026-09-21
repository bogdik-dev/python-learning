names = ["Богдан", "Кирилл", "Ева", "Вова", "Савелий"] 
for i in names:
    c = 0
    for i2 in i:
        if i2 == "а":
          c = c + 1
    if c > 0:
        print(i)