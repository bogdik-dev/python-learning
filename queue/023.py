def f(data, index, div):
    try:
        val = data[index]
        res = val / div
        print(res)
    except Exception as error:
        print(f"Произошла ошибка {error}")
f([2026, 4, 26, 20_000], 2, 0)