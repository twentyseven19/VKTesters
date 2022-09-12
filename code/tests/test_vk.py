import pytest


class TestVk:

    # Float
    @pytest.mark.parametrize("test_input, excepted", [(1, -1), (1.1, 1), (1., 1), (.1, 1)])
    def test_float_one(self, test_input, excepted):
        num_to_str = str(test_input)
        assert num_to_str.find(".") == excepted

    def test_float_second(self):
        try:
            assert float("12,3") == 12.3
        except ValueError:
            pass

    # List
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

    # Dict
    @pytest.mark.parametrize("test_input, excepted", [(dict(), {}), (dict(a=1, b=2), {"a": 1, "b": 2}),
                                                      (dict.fromkeys(["a", "b"]), {"a": None, "b": None})])
    def test_dict_one(self, test_input, excepted):
        assert test_input == excepted

    def test_dict_second(self):
        a = 1
        b = 2
        try:
            assert dict(a, b) == {"a": 1, "b": 2}
        except TypeError:
            pass
