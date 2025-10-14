from datetime import datetime

# 1 — Класс Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"



# 2 — Класс Rectangle

class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        # предполагается: p1 - левый нижний, p2 - правый верхний
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))

    def perimeter(self):
        return 2 * (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))

    def contains(self, point: Point):
        return (self.p1.x <= point.x <= self.p2.x) and (self.p1.y <= point.y <= self.p2.y)



# 4 — Десятичный счётчик

class Counter:
    def __init__(self, start=0):
        self.value = max(0, start)

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

    def get_counter(self):
        return self.value



# 5–6 — Класс Clock

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def add_hour(self):
        self.hours = (self.hours + 1) % 24

    def add_minute(self):
        self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.add_hour()

    def add_second(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.add_minute()

    def __add__(self, other):
        total_seconds = (self.hours + other.hours) * 3600 + \
                        (self.minutes + other.minutes) * 60 + \
                        (self.seconds + other.seconds)
        h = (total_seconds // 3600) % 24
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return Clock(h, m, s)

    def __repr__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"



# 7 — Животное и Трава

class Grass:
    def __init__(self, nutrition):
        self.nutrition = nutrition


class Herbivore:
    def __init__(self, name, hunger=100):
        self.name = name
        self.hunger = hunger

    def eat(self, grass: Grass):
        if self.hunger > 0:
            self.hunger -= grass.nutrition
            if self.hunger < 0:
                self.hunger = 0
            return True
        return False


# 8 — Элементы

class Element:
    def __add__(self, other):
        return None


class Water(Element):
    def __add__(self, other):
        if isinstance(other, Air): return Storm()
        if isinstance(other, Fire): return Steam()
        if isinstance(other, Earth): return Mud()


class Air(Element):
    def __add__(self, other):
        if isinstance(other, Fire): return Lightning()
        if isinstance(other, Earth): return Dust()
        if isinstance(other, Water): return Storm()


class Fire(Element):
    def __add__(self, other):
        if isinstance(other, Water): return Steam()
        if isinstance(other, Air): return Lightning()
        if isinstance(other, Earth): return Lava()


class Earth(Element):
    def __add__(self, other):
        if isinstance(other, Water): return Mud()
        if isinstance(other, Air): return Dust()
        if isinstance(other, Fire): return Lava()



class Storm: name = "Шторм"
class Steam: name = "Пар"
class Mud: name = "Грязь"
class Lightning: name = "Молния"
class Dust: name = "Пыль"
class Lava: name = "Лава"


class Ice(Element):
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Air):
            return Snow()
        return None


class Snow: name = "Снег"
