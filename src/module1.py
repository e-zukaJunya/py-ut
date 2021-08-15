from src.module2 import ForMock


def add(n: int, m: int):
    return n+m


def multiple(n: int, m: int):
    return n*m


def add_n_multi(n: int, m: int):
    tmp = add(n, m)
    return multiple(tmp, tmp)


def mock_test():
    moji = ForMock().func1("aaa")
    return moji
