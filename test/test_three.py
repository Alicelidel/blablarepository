from lessons.three import inna_func_add_sum_to_the_middle, NotAStringException
import pytest

@pytest.mark.parametrize(
    "array",
    [
        ("a2"),
        ("abcdEFG12345dgjfklgdfgjdfgjdfgdfgljdfgkjdfgldfjgljdfgkldfjgkjkdfgkjljkdjkfgj78"),
        ("")
    ]
)
def test_returns_true(array):
    result = inna_func_add_sum_to_the_middle(array)
    assert result is True

@pytest.mark.parametrize(
    "array",
    [
        ("a1B"),
        ("abcdEFG12345dgjfklgdfgjdfgjdfgdfgljdfgkjdfgldfjgljdfgkldfjgkjkdfgkjljkdjkfg77")
    ]
)
def test_returns_false(array):
    result = inna_func_add_sum_to_the_middle(array)
    assert result is False

@pytest.mark.parametrize(
    "arg",
    [
        (("a", 2, True, 4)),
        ({"a", 2, True, 4}),
        ({"whoami": "fool", "since": 1995}),
        (["apple", 1, True]),
        (1),
        (1.025)
    ]
)
def test_raises_exception(arg):
    try:
        inna_func_add_sum_to_the_middle(arg)
    except Exception as e:
        assert isinstance(e, NotAStringException)

