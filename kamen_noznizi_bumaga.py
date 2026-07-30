
import random

moves = ["камень", "ножницы", "бумага"]
player = input("камень/ножницы/бумага, Выбирай!").strip().lower()
computer = random.choice(moves)
print(f"Компьютер выбрал: {computer}")

if player == computer:
    print("Ничья!")
elif (player == "камень" and computer == "ножницы") or \
    (player == "ножницы" and computer == "бумага") or \
    (player == "бумага" and computer == "камень"):
    print("ТЫ ВЫЫЫИГРАЛ")
else:
    print("Компьюер выиграл")


import random
moves = ["камень", "ножницы", "бумага"]
while True:
    player = input("Выбирай - камень/ножницы/бумага ").lower().strip()
    computer = random.choice(moves)
    print(f"Соперник выбрал {computer}")
    if player == computer:
        print("Ничья")
    elif  player == "камень" and computer == "бумага" or\
          player == "ножницы" and computer == "камень" or\
          player == "бумага" and computer == "ножницы":
          print("ты лох")
    else:
        print("любой может выиграть компьютер")
    stop = input("Будешь играть еще? n - нет: ").strip().lower()
    if stop == "n":
        break