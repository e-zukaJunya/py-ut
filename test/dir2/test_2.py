from time import sleep, time

from src.module1 import add, add_n_multi, multiple


def test_1():
    a = 1
    b = 2
    num1 = add(1, 2)
    assert a+b == num1
