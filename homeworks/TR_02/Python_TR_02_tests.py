# Написать класс IntCalc, который имеет методы add, substract (сложение и вычитание целых чисел)
# Протестировать этот класс с помощью библиотек pytest.
# Для pytest использовать фикстуру, которая создает экземпляр класса.
# Так же для тестирования использовать возможность параметризации теста.
import pytest as pytest


class IntCalc:
    def __init__(self, can_add):
        self.can_add = can_add

    def add(self, *args):
        return sum(args) if self.can_add else None

    def substract(self, *args):
        return args[0] - args[1] if not self.can_add else None


@pytest.fixture(scope="function", params=[IntCalc(True), IntCalc(False)])
def calcs_gen(request):
    return request.param


@pytest.mark.parametrize("arg1,arg2,expected_add,expected_sub", [(2, 1, 3, 1), (5, -100, -95, 105)])
def test_calcs(calcs_gen, arg1, arg2, expected_add, expected_sub):
    assert calcs_gen.add(arg1, arg2) == (expected_add if calcs_gen.can_add else None), 'wrong result for add'
    assert calcs_gen.substract(arg1, arg2) == (expected_sub if not calcs_gen.can_add else None), 'wrong result for ' \
                                                                                                 'subtract '
