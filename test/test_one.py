from lessons.one import inna_func
import pytest


@pytest.mark.parametrize(
    "array",
    [
        ([]),
        ([1, 2, 3]),
        (['a', 'b']),
        ([[], []]),
        (("a", 2, True, 4)),
        ({"a", 2, True, 4}),
        ({"whoami": "fool", "since": 1995})
     ]
)
def test_returns_true(array):
    result = inna_func(array)
    assert result is True


#@pytest.mark.parametrize(
#    "array",
#   [
#        ([]),
#        ([1, 2, 3]),
#        (['a', 'b']),
#        ([[], []]),
##)
#def test_prime(array):
#    result = lera_func(array)
#    assert result is True
