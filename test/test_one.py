from lessons.is_list_even import is_list_even
from lessons.Exceptions import NotAListException
import pytest


@pytest.mark.parametrize(
    "array",
    [
        ([]),
        (['a', 'b']),
        ([[], []])
     ]
)
def test_returns_true(array):
    result = is_list_even(array)
    assert result is True

@pytest.mark.parametrize(
    "array",
    [
        ([1]),
        (["apple", 1, True, False, 2, "a", "b", "c", 3, 4, "d"])
    ]
)
def test_returns_false(array):
    result = is_list_even(array)
    assert result is False

@pytest.mark.parametrize(
    "arg",
    [
        (("a", 2, True, 4)),
        ({"a", 2, True, 4}),
        ({"whoami": "fool", "since": 1995}),
        ("LeraDurak"),
        (1),
        (1.025)
    ]
)
def test_raises_exception(arg):
    try:
        is_list_even(arg)
    except Exception as e:
        assert isinstance(e, NotAListException)
