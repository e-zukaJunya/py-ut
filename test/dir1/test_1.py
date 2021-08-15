from test.dir1.fixture import aaa
from time import sleep, time

from src.module1 import add, add_n_multi, multiple


def test_1(aaa):
    a = 1
    b = 2
    num1 = add(1, 2)
    assert a+b == num1


class TestGroup():
    def test_2(self):
        a = 1
        b = 2
        num1 = multiple(1, 2)
        assert a*b == num1

    def test_3(self):
        a = 1
        b = 2
        num1 = add_n_multi(1, 2)
        sleep(1)
        assert (a+b) ** 2 == num1
