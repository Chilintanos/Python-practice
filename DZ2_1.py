# 1
def task1():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]

    a.extend(b)
    count5 = a.count(5)
    print(f"при первом объединении: {count5}")
    while 5 in a:
        a.remove(5)

    a.extend(c)
    count3 = a.count(3)
    print(f"при втором объединении: {count3}")
    print(f"Итог: {a}")


# 2
def task2():
    class1 = list(range(160, 177, 2))
    class2 = list(range(162, 181, 3))
    merged = sorted(class1 + class2)
    print(f"Отсортированный список: {merged}")


# 3
def task3():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    name = input('Введи название детали: ').lower()
    sum_price = sum(price for item, price in shop if item == name)
    count = sum(1 for item, price in shop if item == name)
    print(f"Кол-во деталей — {count}")
    print(f"Общая стоимость — {sum_price}")


#  4
def task4():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    while True:
        print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
        action = input('Гость пришёл или ушёл? ').lower()
        if action == 'пора спать':
            print('Вечеринка закончилась, все легли спать.')
            break
        name = input('Имя гостя: ')
        if action == 'пришёл':
            if len(guests) < 6:
                guests.append(name)
                print(f"Привет, {name}!")
            else:
                print(f"Прости, {name}, но мест нет.")
        elif (action == 'ушёл' or action == 'ушел'):
            if name in guests:
                guests.remove(name)
                print(f"Пока, {name}!")


# 5
def task5():
    violator_songs = [
        ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56], ['Halo', 4.9],
        ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]
    ]

    n = int(input('Сколько песен выбрать? '))
    total = 0
    for i in range(1, n + 1):
        title = input(f'Название {i}-й песни: ')
        for song in violator_songs:
            if song[0].lower() == title.lower():
                total += song[1]
                break
    print(f'Общее время звучания песен: {round(total, 2)} минуты')


# 6
def task6():
    list1 = [int(input(f'Введите {i+1}-е число для первого списка: ')) for i in range(3)]
    list2 = [int(input(f'Введите {i+1}-е число для второго списка: ')) for i in range(7)]
    list1.extend(list2)
    unique = list(set(list1))
    print(f'Первый список: {list1[:3]}')
    print(f'Второй список: {list2}')
    print(f'Новый первый список с уникальными элементами: {unique}')


# 7
def task7():
    n = int(input('Кол-во коньков: '))
    skates = [int(input(f'Размер {i+1}-й пары: ')) for i in range(n)]
    k = int(input('Кол-во людей: '))
    people = [int(input(f'Размер ноги {i+1}-го человека: ')) for i in range(k)]
    skates.sort()
    people.sort()
    count = 0
    for size in people:
        for skate in skates:
            if skate >= size:
                count += 1
                skates.remove(skate)
                break
    print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')


# Задача 8
def task8():
    n = int(input('Кол-во человек в игре: '))
    k = int(input('Какое число в считалке? '))
    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        print(f'Выбывает человек под номером {people[index]}')
        people.pop(index)
    print(f'Остался человек под номером {people[0]}')


#  9
def task9():
    n = int(input('Кол-во друзей: '))
    k = int(input('Долговых расписок: '))
    balance = [0] * n
    for i in range(k):
        print(f'\n{i+1}-я расписка')
        to_ = int(input('Кому: ')) - 1
        frm = int(input('От кого: ')) - 1
        amount = int(input('Сколько: '))
        balance[to_] -= amount
        balance[frm] += amount
    print('\nБаланс друзей:')
    for i, val in enumerate(balance, 1):
        print(f'{i}: {val}')


#  10
def task10():
    n = int(input('Кол-во чисел: '))
    seq = [int(input('Число: ')) for _ in range(n)]
    for i in range(n):
        if seq[i:] == seq[i:][::-1]:
            add = seq[:i][::-1]
            break
    print(f'Последовательность: {seq}')
    print(f'Нужно приписать чисел: {len(add)}')
    print(f'Сами числа: {add}')


def main():
    tasks = {i: globals()[f"task{i}"] for i in range(1,11)}
    print("Выберите номер упражнения (1–10): ")
    num = int(input("> "))
    if num in tasks:
        tasks[num]()
    else:
        print("Нет такого задания!")

if __name__ == "__main__":
    main()