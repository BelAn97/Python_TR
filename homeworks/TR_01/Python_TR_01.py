import doctest


# Ввод вывод. Функции

def divide_func(x, y):
    """
    >>> divide_func(6, 3)
    2.0
    >>> divide_func(2, 0)
    """
    return x / y if y else None


print(divide_func(6, 3))
print(divide_func(2, 0))


def degree_func(deg, *args):
    for x in args:
        print(f"число={x} степень={deg} результат={x ** deg}")


degree_func(3, 1, 2, 3)


def file_len_func(filename):
    with open(filename) as testfile:
        for (index, row) in enumerate(testfile):
            print(f"номер строки={index} длинна={len(row)}")


file_len_func('../../main.py')


def nod_func(*args):
    """
    >>> nod_func(30, 6, 12, 18)
    6
    """
    lst = sorted(args, reverse=True)
    while lst[1] != 0:
        lst[0], lst[1] = lst[1], lst[0] % lst[1]
        lst = sorted(lst, reverse=True)
    return lst[0]


print(nod_func(30, 6, 12, 18))


# Классы и ООП. Исключения

def divide_func_ext(x, y):
    """
    Создать функцию, которая принимает два числа и делит одно на другое.
    в случае деления на 0, перехватить исключение и вернуть None.
    >>> divide_func_ext(4,2)
    2
    >>> divide_func_ext(4,0)
    """
    try:
        return x / y
    except ZeroDivisionError:
        return None


class ContextClass:
    """
    Создать класс менеджера контекста, который будет при входе в блок
    печатать текст переданный в конструкторе. А при выходе из блока
    печатать "context closed".
    """

    def __init__(self, text):
        self.text = text

    def __enter__(self):
        print(f"Context text: {self.text}")

    def __exit__(self, type, value, traceback):
        print("Context closed")


with ContextClass('My text') as myContext:
    pass


# Создать иерархию классов


class Building:
    def __init__(self, address, floors, wall_material):
        self.address = address
        self.floors = floors
        self.wall_material = wall_material

    def print_address(self):
        print(f"{self.__class__.__name__} Address: {self.address}")

    def floors_count(self):
        return self.floors

    def __lt__(self, other):
        bless = self.floors_count() < other.floors_count()
        print(f"{self.__class__.__name__} \
        {'less' if bless else 'larger'} when {other.__class__.__name__}")
        return bless


class House(Building):
    def __init__(self, address, floors, wall_material, tenants):
        super().__init__(address, floors, wall_material)
        self.tenants = tenants


class Shop(Building):
    def __init__(self, address, floors, wall_material, workers):
        super().__init__(address, floors, wall_material)
        self.workers = workers


myHouse = House('NY, Queens, 5', 7, 'concrete', 50)
myShop = Shop('NY, Wall Street, 12', 3, 'bricks', 100)

myHouse.print_address()
myShop.print_address()

print(myShop > myHouse)

doctest.testmod()
