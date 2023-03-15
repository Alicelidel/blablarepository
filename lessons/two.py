# на вход массив, нужно вывести True если там есть буква A, большая или маленькая)
from lessons.one import NotAListException


def lera_func_find_letters_a(args: list):
    if not isinstance(args, list):
        return NotAListException('not a list')
    for x in args:
        if x == "a" or x == "A":
            return True
    return False
