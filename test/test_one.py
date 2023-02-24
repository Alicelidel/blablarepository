from lessons.one import inna_func, NotAListException
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
    result = inna_func(array)
    assert result is True

@pytest.mark.parametrize(
    "array",
    [
        ([1]),
        (["apple", 1, True, False, 2, "a", "b", "c", 3, 4, "d"])
    ]
)
def test_returns_false(array):
    result = inna_func(array)
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
        inna_func(arg)
    except Exception as e:
        assert isinstance(e, NotAListException)
