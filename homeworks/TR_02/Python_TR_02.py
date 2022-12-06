import collections
from homeworks.TR_02.setup_date_pack import print_current

# Создать декоратор, который перед запуском функции
# распечатывает все аргументы вызываемой функции.


def print_decor(func):
    def inner(*args, **kwargs):
        print(f"args:{args},{kwargs}")
        return func(*args, **kwargs)

    return inner


@print_decor
def func_print_decor(x, y, *args, **kwargs):
    pass


func_print_decor(3, 4, 5, param=1)


# Создать класс в котором применить декоартор @property
# для доступа к внутренней переменной.
class TestProp:

    def __init__(self, value):
        self.value = value

    @property
    def val(self):
        return self.value


TestProp(44).val


# Создать генератор который возвращается квадраты чисел от 1 до N.
# N передается в качестве параметра генератору.
def sqrt(n):
    for i in range(1, n + 1):
        yield i ** 2


sqrt_gen = sqrt(5)
for j in sqrt_gen:
    print(j)

# С помощью стандартной функции collections.namedtuple
# создать объект для хранения точки в трехмерном пространстве.

Point3D = collections.namedtuple('Point3D', ['x', 'y', 'z'])
pnt = Point3D(10, 20, 30)
print(pnt)

# Создать пакет в котором будет функция для распечатки текущей даты
# (можно использовать пакет datetime).
print_current()
