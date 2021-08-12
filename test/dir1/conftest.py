import pytest
# 自動で読み込まれて実行される


@pytest.fixture(scope="session", autouse=True)
def session_f():
    print("session fixture pre")
    yield
    print("session fixture post")


@pytest.fixture(scope="module", autouse=True)
def module_f():
    print("module fixture pre")
    yield
    print("module fixture post")


@pytest.fixture(scope="class", autouse=True)
def class_f():
    print("class fixture pre")
    yield
    print("class fixture post")


@pytest.fixture(scope="function", autouse=True)
def func_f():
    print("function fixture pre")
    yield
    print("function fixture post")
