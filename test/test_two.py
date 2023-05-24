import pytest
from lessons.find_letters_a import lera_func_find_letters_a
from lessons.Exceptions import NotAListException


@pytest.mark.parametrize(
    "array",
    [
        (['a', 'b']),
        ([1, 2, 3, 'A']),
    ]
)
def test_true(array):
    result = lera_func_find_letters_a(array)
    assert result is True


@pytest.mark.parametrize(
    "array",
    [
        ([]),
        (['b', 'c']),
        ([1, 2, 3]),
        (['abc'])
    ]
)
def test_false(array):
    result = lera_func_find_letters_a(array)
    assert result is False


@pytest.mark.parametrize(
    "array",
    [
        (1),
        ('b', 'c'),
        ([], [])
    ]
)
def test_exception(array):
    try:
        lera_func_find_letters_a(array)
    except Exception as e:
        assert isinstance(e, NotAListException)