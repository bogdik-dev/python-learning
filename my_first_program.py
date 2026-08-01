tasks = []
while True:
    text_zadan = input("Добавь задачу ")
    tasks.append(text_zadan)

    ece = input("Хочешь добавить еще одну задачу (да/нет)")
    if ece == "нет":
        break

if len(tasks) == 0:
    print("Задач нет")
else:
    print("Твои задачи")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")