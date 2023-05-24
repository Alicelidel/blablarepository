from lessons.add_sum_to_the_middle import inna_func_add_sum_to_the_middle
from lessons.Exceptions import NotAStringException
import pytest


@pytest.mark.parametrize(
    "string, result",
    [
        ("a2", "a22"),
        ("abcd", "ab4cd"),
        ("", "0")
    ]
)
def test_returns_sum(string, result):
    assert inna_func_add_sum_to_the_middle(string) == result


@pytest.mark.parametrize(
    "string",
    [
        ("a1B"),
        ("abcdEFG12345dgjfklgdfgjdfgjdfgdfgljdfgkjdfgldfjgljdfgkldfjgkjkdfgkjljkdjkfg77")
    ]
)
def test_returns_false(string):
    assert inna_func_add_sum_to_the_middle(string) is False


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

