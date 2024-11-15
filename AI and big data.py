result = []

def divider(a, b):
    if a < b:
        raise ValueError("a повинно бути більше або дорівнювати b")
    if b > 100:
        raise IndexError("b не повинно бути більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль для ключа {key}")
    except TypeError:
        print(f"Помилка: Некоректний тип даних для ключа {key}")
    except ValueError as ve:
        print(f"Помилка значення: {ve}")
    except IndexError as ie:
        print(f"Помилка індексу: {ie}")

print(result)
