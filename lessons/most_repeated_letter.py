from lessons.Exceptions import NotAStringException


class EmptyStringException(Exception):
    pass


def inna_func_most_repeated_letter(args):
    if not isinstance(args, str):
        return NotAStringException('not a string')

    if args == "":
        return EmptyStringException('max() arg is an empty sequence')

    args = args.lower()

    letters = {}  # create dict to store letter:the number

    for i in args:
        if i.isalpha():
            if i in letters.keys():
                letters[i] += 1  # if such a letter is already in the dict, it increments its count
            else:
                letters[i] = 1  # otherwise, add the letter to the dic with a count of 1
        else:
            return False  # False if string does not contain letters

    return max(letters.values())
