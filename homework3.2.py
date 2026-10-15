
'''
list1 = [1, 3, 10]
list2 = [2, 5, 6]
sum1 = sum(list1)
sum2 = sum(list2)
if sum1 > sum2:
    print("первый больше")
else:
    print("второй больше")

doom = [1, "GARAGE", 4, 5, "hooom", "joker"]
hmm = 0
for i in doom:
    if type(i) == int:
        hmm = hmm + i
print(hmm)

count = 100
while count < 201:
    print(count)
    count = count + 1

quests = []
quests.append("Гарик")
quests.append("Антошка")
quests.append("Вова")
for name in quests:
    print(f"Привет {name}, ты приглашен на свадьбу!")

lol = [2, 4, 3, 5, 6, 88, 30]
#sum = 0
for i in lol:
    if i % 2 == 0:
      #sum = sum + i
#print(sum)
      print(i)

name = input("Как тебя зовут?")
age = input("Сколько тебе лет?")
city = input("Где ты живешь?")
id = f"меня зовут {name}, мне {age}, я живу в {city}"
print(id)
'''
def max_of_two(a,b):
    a = 22
    b = 21
    if a > b:
      print(a)
    else:
      print(b)
max_of_two(22, 21)

nun = 10
while nun >= 1:
    print(nun)
    nun = nun - 1

guests = []
guests.append("Коля")
guests.append("Витя")
guests.append("Зачем?")
for name in guests:
        print(f"Привет, {name}, ты приглашен!")

numbers = [2, 10, 33, 35, 66, 1, 80, 23]
su = 0
for i in numbers:
    if i % 2 != 0:
        su = su + i
print(su)

login = 1234
email = "1qazxc"
age = 45
user = [login, email, age]
print(user[1])

def is_positive(n):
    if n > 0:
        return True
    else:
        return False
print(is_positive(-5))
