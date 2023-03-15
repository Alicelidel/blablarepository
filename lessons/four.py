from lessons.Exceptions import NotAStringException, EmptyStringException


def lera_function_count_letters_a(args):
    if not isinstance(args, str):
        return NotAStringException("Not a string!")
    if len(args) == 0:
        return EmptyStringException("The string is empty")
    count = 0
    for x in args:
        if x == 'a':
            count = count + 1
    return count
