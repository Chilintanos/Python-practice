
# Задача 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


class TaskManager:
    def __init__(self):
        self.stack = Stack()
        self.tasks = {}

    def new_task(self, task: str, priority: int):
        if priority not in self.tasks:
            self.tasks[priority] = []
        self.tasks[priority].append(task)
        self.stack.push((priority, task))

    def __str__(self):
        result = []
        for priority in sorted(self.tasks.keys()):
            tasks_str = "; ".join(self.tasks[priority])
            result.append(f"{priority} {tasks_str}")
        return "\n".join(result)


# Задача 2
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_data = OrderedDict()

    @property
    def cache(self):
        if self.cache_data:
            key = next(iter(self.cache_data))
            return (key, self.cache_data[key])
        return None

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = value
        if len(self.cache_data) > self.capacity:
            self.cache_data.popitem(last=False)

    def get(self, key):
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None

    def print_cache(self):
        print("LRU Cache:")
        for k, v in self.cache_data.items():
            print(f"{k} : {v}")
        print()


# Задача 3
def cache_decorator(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Задача 4
class Cell:
    def __init__(self, num):
        self.num = num
        self.value = " "

    def is_free(self):
        return self.value == " "


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def show(self):
        for i in range(0, 9, 3):
            print(f"{self.cells[i].value} | {self.cells[i+1].value} | {self.cells[i+2].value}")
            if i < 6:
                print("--+---+--")
        print()

    def make_move(self, position, symbol):
        if self.cells[position - 1].is_free():
            self.cells[position - 1].value = symbol
            return True
        return False

    def check_winner(self):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for pos in win_positions:
            if self.cells[pos[0]].value == self.cells[pos[1]].value == self.cells[pos[2]].value != " ":
                return self.cells[pos[0]].value
        return None

    def is_full(self):
        return all(not cell.is_free() for cell in self.cells)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


if __name__ == "__main__":
    # Проверка задач 1–3
    print("=== Задача 1 ===")
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("поиграть в PS4", 4)
    manager.new_task("чилл", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз по python", 2)
    print(manager, "\n")

    print("=== Задача 2 ===")
    cache = LRUCache(3)
    cache.cache = ("key1", "value1")
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")
    cache.print_cache()
    print(cache.get("key2"))
    cache.cache = ("key4", "value4")
    cache.print_cache()

    print("=== Задача 3 ===")
    print([fibonacci(i) for i in range(10)])

    print("=== Задача 4 ===")
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")
    current = player1

    while True:
        board.show()
        move = int(input(f"{current.name} ({current.symbol}), выберите клетку (1–9): "))
        if board.make_move(move, current.symbol):
            winner = board.check_winner()
            if winner:
                board.show()
                print(f" Победил {current.name}!")
                break
            elif board.is_full():
                board.show()
                print(" Ничья!")
                break
            current = player1 if current == player2 else player2
        else:
            print("❌ Клетка занята, попробуй снова.")
