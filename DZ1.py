import math
import time

# 1
def exercise1():
    print("Рижский Никита Владиславович")
    print("123456, Москва, ул. Пушкина, дом колотушкина")

# 2
def exercise2():
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}!")

# 3
def exercise3():
    length = float(input("Введите длину комнаты в метрах: "))
    width = float(input("Введите ширину комнаты метрах: "))
    print(f"Площадь комнаты: {length * width:.2f} м²")

# 4
def exercise4():
    length = float(input("Введите длиину участка в футах: "))
    width = float(input("Введите ширину участка в футах: "))
    acres = (length * width) / 43560
    print(f"Площадь участка: {acres:.4f} акров")

# 5
def exercise5():
    small_bottle = int(input("Введите количество бутылок <=1л: "))
    big_bottle = int(input("Введите количество бутылок >1л: "))
    total = small_bottle * 0.10 + big_bottle * 0.25
    print(f"Выручка: ${total:.2f}")

# 6
def exercise6():
    order = float(input("Введите сумму заказа: "))
    nal = order * 0.05
    tea = order * 0.18
    total = order + nal + tea
    print(f"Налог: {nal:.2f}, ча1: {tea:.2f}, итог: {total:.2f}")

# 7.
def exercise7():
    n = int(input("Введите n: "))
    s = n * (n + 1) // 2
    print(f"Сумма = {s}")

# 8
def exercise8():
    s = int(input("Введите количество сувениров: "))
    b = int(input("Введите количество безделушек: "))
    total = s * 75 + b * 112
    print(f"Общий вес посылки: {total} г")

# 9
def exercise9():
    deposit = float(input("Введите сумму депозита: "))
    for year in range(1, 4):
        deposit *= 1.04
        print(f"Сумма через {year} год(а): {deposit:.2f}")

# 10
def exercise10():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print("a+b =", a+b)
    print("a-b =", a-b)
    print("a*b =", a*b)
    print("a/b =", a/b)
    print("a%b =", a%b)
    print("log10(a) =", math.log10(a))
    print("a^b =", a**b)

# 11
def exercise11():
    ras = float(input("Введите расход: "))
    l = 235.215 / ras
    print(f"{ras} расход {l:.2f} литров/100км")

# 12
def exercise12():
    t1 = math.radians(float(input("Введите широту 1: ")))
    g1 = math.radians(float(input("Введите долготу 1: ")))
    t2 = math.radians(float(input("Введите широту 2: ")))
    g2 = math.radians(float(input("Введите долготу 2: ")))
    dist = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) +
                               math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    print(f"Расстояние: {dist:.2f} км")

# 13
def exercise13():
    cents = int(input("Введите сдачу: "))
    toonies = cents // 200; cents %= 200
    loonies = cents // 100; cents %= 100
    quarters = cents // 25; cents %= 25
    dimes = cents // 10; cents %= 10
    nickels = cents // 5; cents %= 5
    pennies = cents
    print(f"2$:{toonies}, 1$:{loonies}, 25c:{quarters}, 10c:{dimes}, 5c:{nickels}, 1c:{pennies}")

# 14
def exercise14():
    tall = int(input("Введите рост в футах: "))
    d = int(input("Введите дюймы: "))
    cm = (tall*12 + d) * 2.54
    print(f"Рост = {cm:.1f} см")

# 15
def exercise15():
    feet = float(input("Введите расстояние в футах: "))
    inches = feet*12
    yards = feet/3
    miles = feet/5280
    print(f"{feet} футов = {inches} дюймов, {yards:.2f} ярдов, {miles:.4f} миль")

# 16
def exercise16():
    r = float(input("Введите радиус: "))
    area = math.pi*r**2
    vol = 4/3*math.pi*r**3
    print(f"Площадь круга: {area:.2f}, объем шара: {vol:.2f}")

# 17
def exercise17():
    m = float(input("Масса воды (мл): "))
    dT = float(input("T: "))
    C = 4.186
    q = m*C*dT
    print(f"Энергия: {q:.2f} Дж")
    kwh = q/3.6e6
    cost = kwh*0.089
    print(f"Стоимость нагрева: {cost:.4f} $")

# 18
def exercise18():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    vol = math.pi*r**2*h
    print(f"Объем цилиндра: {vol:.1f}")

# 19
def exercise19():
    h = float(input("Введите высоту (м): "))
    v = math.sqrt(2*9.8*h)
    print(f"Скорость при падении: {v:.2f} м/с")

# 20
def exercise20():
    P = float(input("Введите давление (Па): "))
    V = float(input("Введите объем (л): "))
    T = float(input("Введите температуру (C): ")) + 273.15
    R = 8.314
    n = (P*V)/(R*T)
    print(f"Количество вещества: {n:.2f} моль")

# 21
def exercise21():
    b = float(input("Введите основание: "))
    h = float(input("Введите высоту: "))
    print(f"Площадь = {b*h/2:.2f}")

# 22
def exercise22():
    a = float(input("Введите сторону 1: "))
    b = float(input("Введите сторону 2: "))
    c = float(input("Введите сторону 3: "))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Площадь = {area:.2f}")

# 23
def exercise23():
    s = float(input("Введите длину стороны: "))
    n = int(input("Введите число сторон: "))
    area = (n*s**2)/(4*math.tan(math.pi/n))
    print(f"Площадь = {area:.2f}")

# 24
def exercise24():
    d = int(input("Введите дни: "))
    h = int(input("Введите часы: "))
    m = int(input("Введите минуты: "))
    s = int(input("Введите секунды: "))
    total = d*86400 + h*3600 + m*60 + s
    print(f"Всего секунд: {total}")

# 25
def exercise25():
    total = int(input("Введите секунды: "))
    d = total//86400; total%=86400
    h = total//3600; total%=3600
    m = total//60; s=total%60
    print(f"{d}:{h:02}:{m:02}:{s:02}")

# 26
def exercise26():
    print("Текущее время:", time.asctime())

# 27
def exercise27():
    year = int(input("Введите год: "))
    a = year%19
    b = year//100
    c = year%100
    d = b//4
    e = b%4
    f = (b+8)//25
    g = (b-f+1)//3
    h = (19*a+b-d-g+15)%30
    i = c//4
    k = c%4
    l = (32+2*e+2*i-h-k)%7
    m = (a+11*h+22*l)//451
    month = (h+l-7*m+114)//31
    day = 1+((h+l-7*m+114)%31)
    print(f"Пасха: {day}.{month}.{year}")

# 28
def exercise28():
    h = float(input("Введите рост (см): "))/100
    w = float(input("Введите вес (кг): "))
    bmi = w/(h*h)
    print(f"BMI = {bmi:.2f}")

# 29
def exercise29():
    c = float(input("Введите температуру (C): "))
    f = c*9/5+32
    k = c+273.15
    print(f"{c}C = {f:.1f}F = {k:.2f}K")

# 30
def exercise30():
    kpa = float(input("Введите давление в кПа: "))
    psi = kpa*0.145038
    mmhg = kpa*7.50062
    atm = kpa/101.325
    print(f"{kpa} кПа = {psi:.2f} PSI, {mmhg:.2f} мм рт.ст., {atm:.3f} атм")

# 31
def exercise31():
    n = input("Введите 4-значное число: ")
    s = "+".join(n)
    print(f"{s} = {sum(int(d) for d in n)}")

# 32
def exercise32():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    nums = [a,b,c]
    nums.sort()
    print(nums)

# 33
def exercise33():
    qty = int(input("Введите количество вчерашних буханок: "))
    price = 3.49
    discount = 0.6
    total = qty * price * (1 - discount)
    print(f"Цена за буханку: ${price:.2f}")
    print(f"Цена со скидкой: ${price*(1-discount):.2f}")
    print(f"Общая стоимость: ${total:.2f}")






def main():
    tasks = {i: globals()[f"exercise{i}"] for i in range(1,34)}
    print("Выберите номер упражнения (1–33): ")
    num = int(input("> "))
    if num in tasks:
        tasks[num]()
    else:
        print("Нет такого задания!")

if __name__ == "__main__":
    main()
