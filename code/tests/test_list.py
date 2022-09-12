import pytest


class TestList:

    @pytest.mark.parametrize("test_input, excepted", [(list(), []), (list(range(5)), [0, 1, 2, 3, 4]),
                                                      (list((1, 2)), [1, 2]), (list([1, 2, 3]), [1, 2, 3]),
                                                      (list({1: 1, 2: 2}), [1, 2])])
    def test_list_one(self, test_input, excepted):
        assert test_input == excepted

    def test_list_second(self):
        try:
            assert list(1) == [1]
        except TypeError:
            pass
