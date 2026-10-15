'''
my_list = []
for i in range(10,100):
  my_list.append(i)
print(my_list)

list = []
for i in range(100,1000):
    if i % 9 == 0:
      list.append(i)
print(list)

dxd = []
for i in range(10,100):
  x = i // 10
  y = i % 10
  z = x + y
  if z % 2 == 0:
    dxd.append(i)
print(dxd)

list = []
count = 0
while count <= 10:
    list.append(count)
    count = count + 1
print(list)
'''
total = 0
while True:
    num = int(input("Введи число"))
    if num == 0:
        break
    else:
        total = total + num
print(total)
