from lessons.count_character_occurrences import count_character_occurrences as lera_function_count_letters_a
from lessons.Exceptions import NotAStringException, EmptyStringException
import pytest

@pytest.mark.parametrize(
    "string, result",
    [
        ("bbbb", 0),
        ("a2", 1),
        ("abAcad", 2)
    ]
)
def test_returns_result_sum(string, result):
    assert lera_function_count_letters_a(string) == result

@pytest.mark.parametrize(
    "arg",
    [
        (("a", 2, True, 4)),
        ({"a", 2, True, 4}),
        ({"whoami": "fool", "since": 1995}),
        (["apple", 1, True]),
        (1),
        (1.025),
        ()
    ]
)
def test_not_a_string_exception(arg):
    try:
        lera_function_count_letters_a(arg)
    except Exception as e:
        assert isinstance(e, NotAStringException)

@pytest.mark.parametrize(
    "arg",
    [
        ("")
    ]
)
def test_empty_string_exception(arg):
    try:
        lera_function_count_letters_a(arg)
    except Exception as e:
        assert isinstance(e, EmptyStringException)
