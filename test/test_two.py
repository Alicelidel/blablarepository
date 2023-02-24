import pytest
from lessons.two import lera_func_find_letters_a


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
        (['abc']),
        ([], [])
    ]
)
def test_false(array):
    result = lera_func_find_letters_a(array)
    assert result is False

