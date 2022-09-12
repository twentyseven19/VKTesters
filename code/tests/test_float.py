import pytest


class TestFloat:

    @pytest.mark.parametrize("test_input, excepted", [(1, -1), (1.1, 1), (1., 1), (.1, 1)])
    def test_float_one(self, test_input, excepted):
        num_to_str = str(test_input)
        assert num_to_str.find(".") == excepted

    def test_float_second(self):
        try:
            assert float("12,3") == 12.3
        except ValueError:
            pass
