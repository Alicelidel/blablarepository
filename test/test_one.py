from lessons.one import inna_func, lera_func
import pytest


@pytest.mark.parametrize(
    "array",
    [
        ([]),
        ([1, 2, 3]),
        (['a', 'b']),
        ([[], []]),
     ]
)
def test_returns_true(array):
    result = inna_func(array)
    assert result is True


@pytest.mark.parametrize(
    "array",
    [
        ([]),
        ([1, 2, 3]),
        (['a', 'b']),
        ([[], []]),
    ]
)
def test_prime(array):
    result = lera_func(array)
    assert result is True
