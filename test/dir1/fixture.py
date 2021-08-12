import pytest

@pytest.fixture
def aaa():
    print("normal fixture pre")
    yield
    print("normal fixture post")
    
