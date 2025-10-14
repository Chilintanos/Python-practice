
import unittest
from DZ4 import Point, Rectangle, Counter, Clock, Grass, Herbivore, Water, Air, Fire, Earth, Ice, Storm, Steam, Mud, Lightning, Dust, Lava

class TestPointAndRectangle(unittest.TestCase):
    def test_point(self):
        p = Point(1, 2)
        self.assertEqual((p.x, p.y), (1, 2))

    def test_rectangle_area_perimeter(self):
        r = Rectangle(Point(0,0), Point(3,4))
        self.assertEqual(r.area(), 12)
        self.assertEqual(r.perimeter(), 14)

    def test_contains(self):
        r = Rectangle(Point(0,0), Point(3,4))
        self.assertTrue(r.contains(Point(1,1)))
        self.assertFalse(r.contains(Point(4,5)))

class TestCounter(unittest.TestCase):
    def test_counter(self):
        c = Counter(1)
        c.increment()
        self.assertEqual(c.get_counter(), 2)
        c.decrement()
        self.assertEqual(c.get_counter(), 1)
        c.decrement()
        self.assertEqual(c.get_counter(), 0)
        c.decrement()  # should stay 0
        self.assertEqual(c.get_counter(), 0)

class TestClock(unittest.TestCase):
    def test_clock_add(self):
        t1 = Clock(10, 30, 45)
        t2 = Clock(3, 40, 20)
        t3 = t1 + t2
        self.assertEqual(str(t3), "14:11:05")

    def test_tick(self):
        t = Clock(23,59,59)
        t.add_second()
        self.assertEqual(str(t), "00:00:00")

class TestHerbivoreAndGrass(unittest.TestCase):
    def test_eat(self):
        grass = Grass(40)
        cow = Herbivore("Cow", hunger=50)
        result = cow.eat(grass)
        self.assertTrue(result)
        self.assertEqual(cow.hunger, 10)
        # eating when not hungry
        cow.hunger = 0
        result2 = cow.eat(grass)
        self.assertFalse(result2)

class TestElements(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual((Water()+Air()).name, "Шторм")
        self.assertEqual((Water()+Fire()).name, "Пар")
        self.assertEqual((Water()+Earth()).name, "Грязь")
        self.assertEqual((Air()+Fire()).name, "Молния")
        self.assertEqual((Air()+Earth()).name, "Пыль")
        self.assertEqual((Fire()+Earth()).name, "Лава")
        self.assertEqual((Ice()+Fire()).name, "Пар")
        self.assertEqual((Ice()+Air()).name, "Снег")

if __name__ == "__main__":
    unittest.main()
