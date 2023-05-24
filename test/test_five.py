from lessons.most_repeated_letter import inna_func_most_repeated_letter, NotAStringException, EmptyStringException
import pytest


@pytest.mark.parametrize(
    "string, result",
    [
        ("bAnana", 3),
        ("hzfhdhdudhdg", 4),
        ("a", 1)
    ]
)
def test_returns_number_of_most_repeated_letter(string, result):
    assert inna_func_most_repeated_letter(string) == result


@pytest.mark.parametrize(
    "string",
    [
        ("0123456789"),
        ("~!@#$%^&*()_+{}:<>?,./;'[]-='!")
    ]
)
def test_returns_false(string):
    assert inna_func_most_repeated_letter(string) is False


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
        inna_func_most_repeated_letter(arg)
    except Exception as e:
        assert isinstance(e, NotAStringException)


@pytest.mark.parametrize(
    "arg",
    [
        (""),
    ]
)
def test_raises_empty_string_exception(arg):
    try:
        inna_func_most_repeated_letter(arg)
    except Exception as e:
        assert isinstance(e, EmptyStringException)