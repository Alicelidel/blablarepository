from lessons.one import inna_func
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
