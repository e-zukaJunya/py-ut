import pytest
from pytest_mock import mocker
from src.module1 import add, add_n_multi, mock_test, multiple
from src.module2 import ForMock


class TestMock():
    def test_fact(self):
        res = mock_test()
        moji = "本物"
        print(res)
        print(moji)
        assert moji == res

    def test_mock(self, mocker):
        func1_mock = mocker.patch.object(ForMock, "func1")
        func1_mock.return_value = "モック"
        res = mock_test()
        moji = "モック"
        print(res)
        print(moji)
        assert moji == res
        # 1回呼び出されたこと
        func1_mock.assert_called_once()
        # 特定引数で呼び出されたこと
        func1_mock.assert_called_with("aaa")

    def test_ex(self, mocker):
        func1_mock = mocker.patch.object(ForMock, "func1")
        func1_mock.side_effect = Exception('エラーです')

        # 例外の発生を検証
        with pytest.raises(Exception) as e:
            res = mock_test()

        print(e.value)
