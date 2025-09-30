import math
from collections import Counter

def exercise1(numbers):
    def gcd_list(lst):
        return math.gcd(*lst)

    def lcm(a, b):
        return a * b // math.gcd(a, b)

    def lcm_list(lst):
        result = lst[0]
        for x in lst[1:]:
            result = lcm(result, x)
        return result

    return gcd_list(numbers), lcm_list(numbers)


def exercise2(sentences):
    return sum(any(ch.isdigit() for ch in s) for s in sentences)



def exercise3(s, k):
    top = k * (len(s) + 2)
    bottom = k * (len(s) + 2)
    mid = k + s + k
    rez = ""
    rez = top + "\n" + mid + "\n" + bottom
    return rez


def exercise4(inp):
    return Counter(inp.lower())



def exercise5(text, shift=3):
    alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rez = ''
    for i in text.lower():
        if i in alp:
            idx = (alp.index(i) + shift) % len(alp)
            rez += alp[idx]
        else:
            rez += i
    return rez


def exercise5_decode(text, s=3):
    return exercise5(text, -s)



def exercise6(*args):
    negatives = []
    pos = []

    for number in args:
        if number < 0:
            negatives.append(number)
        else:
            pos.append(number)

    negatives.sort(reverse=True)
    pos.sort()
    rez = (negatives, pos)
    return rez



def exercise7(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]



def exercise8():
    low, high = 1, 100
    at = 0
    while low <= high:
        mid = (low + high) // 2
        at += 1
        print(f"Твое число равно, меньше или больше, чем {mid}?")
        ans = int(input("(1=равно, 2=больше, 3=меньше): "))
        if ans == 1:
            print(f"Угадал за {at} попыток!")
            break
        elif ans == 2:
            low = mid + 1
        elif ans == 3:
            high = mid - 1



def to_decimal(num_str, b):
    return int(num_str, b)


def from_decimal(num, b):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    res = ""
    while num > 0:
        res = digits[num % b] + res
        num //= b
    return res


def exercise9(num_str, from_b, to_b):
    if not (2 <= from_b <= 16 and 2 <= to_b <= 16):
        raise ValueError("от 2 до 16 сделай очнование!")
    dec = to_decimal(num_str, from_b)
    return from_decimal(dec, to_b)



def is_magic_date(day, month, year):
    return day * month == year % 100


def exercise10():
    magic_dates = []
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    if is_magic_date(day, month, year):
                        magic_dates.append((day, month, year))
                except:
                    continue
    return magic_dates


if __name__ == "__main__":
    print("1:", exercise1([12, 18, 24]))
    print("2:", exercise2(["Привет", "Тест123", "Нет цифр"]))
    print("3:\n", exercise3("Никитосик", "*"))
    print("4:", exercise4("Привет от Мисиса!"))
    print("5 шифр:", exercise5("Пока"))
    print("5 дешифр:", exercise5_decode(exercise5("Пока")))
    print("6:", exercise6(-1, 0, 5, -3, 8))
    print("7:", exercise7("Nikita"))
    print("9:", exercise9("1F", 16, 2))
    print("10:", exercise10()[:5])
