def add(n: int, m: int):
    return n+m


def multiple(n: int, m: int):
    return n*m


def add_n_multi(n: int, m: int):
    tmp = add(n, m)
    return multiple(tmp, tmp)
