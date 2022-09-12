import pytest


class TestDict:

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
