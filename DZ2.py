import math
from collections import Counter

# 0
def exercise0():
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")
    if len(s1) != len(s2):
        print("Нельзя получить циклическим сдвигом")
    else:
        if s2 in (s1+s1):
            print("Можно получить циклическим сдвигом")
        else:
            print("Нельзя получить циклическим сдвигом")

# 1
def exercise1():
    a = []
    b = []

    # операции со списками
    a.append(4.5)
    a.append(3.4)
    a.extend([8.7, 1.3])

    b.append(14.5)
    b.append(3.4)
    b.extend([8.7, 11.3])

    a.insert(1, 100)
    a.insert(3, 100)

    b.insert(0, 200)
    b.insert(2, 200)

    print("Исходные списки:")
    print("1-й:", a)
    print("2-й:", b)

    del a[0]
    del b[0]

    a.remove(100)
    b.remove(200)

    print("\nПосле удалений:")
    print("1-й:", a)
    print("2-й:", b)

    sa = set(a)
    sb = set(b)
    sa_and_sb = sa & sb

    print("\nУникальные элементы:")
    print("1-й:", sa)
    print("2-й:", sb)
    print("общие:", sa_and_sb)

    c = a + b
    c_asc = sorted(c)
    c_desc = sorted(c, reverse=True)

    sr_ar = sum(c[1::2]) / len(c[1::2])
    prod = 1
    for x in c[0::2]:
        prod *= x
    sr_geom = prod ** (1/len(c[0::2]))

    c_max = max(c)
    c_min = min(c)

    print("\nИтоговые:")
    print("3-й:", c)
    print("Сортировка (возр.):", c_asc)
    print("Сортировка (убыв.):", c_desc)
    print(f"Ср. арифм. = {sr_ar:.2f}, ср. геометр. = {sr_geom:.2f}")
    print("Макс. и мин.:", c_max, c_min)

# 2
def exercise2():
    info = {}
    info["фио"] = "Рижский Никита Владиславович"
    info["дата_рождения"] = "23/09/2003"
    info["место_рождения"] = "Москва"

    info["хобби"] = ["футбол", "формула 1"]
    info["хобби"].append("программирование")

    info["животные"] = ("кошка Мурка", "собака Шарик")

    info["ЕГЭ"] = {}
    info["ЕГЭ"]["Математика"] = 76
    info["ЕГЭ"]["Физика"] = 74
    info["ЕГЭ"]["Русский язык"] = 84
    info["ЕГЭ"]["Химия"] = 99
    del info["ЕГЭ"]["Химия"]

    info["вузы"] = {}
    info["вузы"]["МИРЭА"] = 244
    info["вузы"]["МИСИС"] = 215
    info["вузы"]["МГТУ им. Баумана"] = 265

    print("Данные:")
    print(info)

    exams = tuple(sorted(info["ЕГЭ"].keys()))
    print("Предметы:", ", ".join(exams))

    uni = tuple(sorted(info["вузы"].keys()))
    print("Вузы:", ", ".join(uni))

    print("\nОтветы на вопросы:")

    name = info["фио"].split()[1]
    starts_with_vowel = name[0].lower() in "аеёиоуыэюя"
    print("* мое имя начинается на гласную букву:", starts_with_vowel)

    month = int(info["дата_рождения"].split("/")[1])
    born_in_winter_or_summer = month in [12,1,2,6,7,8]
    print("* родился летом или зимой:", born_in_winter_or_summer)

    hobbies_count = len(info["хобби"])
    print(f"* у меня {hobbies_count} хобби, первое \"{info['хобби'][0]}\"")

    print(f"* после окончания школы сдавал {len(info['ЕГЭ'])} экз.")
    sum_mark = sum(info["ЕГЭ"].values())
    print(f"* сумма баллов = {sum_mark}")
    max_mark = max(info["ЕГЭ"].values())
    print(f"* макс. балл = {max_mark}")

    vuz_count = sum(int(sum_mark >= ball) for ball in info["вузы"].values())
    print(f"* кол-во вузов в которые прохожу: {vuz_count}")

# 3
def exercise3():
    db = [
        {"name":"Иванов Иван","birthday":"01/12/2000","height":170,"weight":70.5,"car":True,"languages":["C++","Python"]},
        {"name":"Сергеев Сергей","birthday":"01/06/2001","height":180,"weight":110.4,"car":False,"languages":["Pascal","Java"]},
        {"name":"Рижский Никиьа","birthday":"23/09/2003","height":178,"weight":57.2,"car":True,"languages":["Java","C++","Python"]}
    ]

    print(f"Содержимое базы данных ({len(db)}):")
    for i, person in enumerate(db, start=1):
        print(f"{i}.")
        print("Имя:", person["name"])
        print("День рождения:", person["birthday"])
        print("Рост (см.):", person["height"])
        print("Вес (кг.):", person["weight"])
        print("Есть машина:", person["car"])
        print("Языки программирования:", person["languages"])

# 4
def exercise4():
    d = {"a":2,"b":3,"c":4}
    prod = 1
    for v in d.values():
        prod *= v
    print("Произведение значений словаря =", prod)

# -5-
def exercise5():
    people = [
        {"name":"Никита","surname":"Рижский"},
        {"name":"Петр","surname":"Петров"},
        {"name":"Иван","surname":"Иванов"}
    ]
    target = input("Введите имя для поиска: ")
    result = [p for p in people if p["name"]==target]
    print("Результат:", result)

# 6
def count_it(sequence:str):
    counter = Counter(sequence)
    return dict(counter.most_common(3))

def exercise6():
    seq = input("Введите последовательность цифр: ")
    print("Топ-3:", count_it(seq))






def main():
    tasks = {i: globals()[f"exercise{i}"] for i in range(0,7)}
    print("Выберите номер задачи (0–6):")
    num = int(input("> "))
    if num in tasks:
        tasks[num]()
    else:
        print("Нет такой задачи!")

if __name__ == "__main__":
    main()
