class NotAStringException(Exception):
    pass

def inna_func_add_sum_to_the_middle(args):
    if not isinstance(args, str):
        return NotAStringException('not a string')

    if len(args) % 2 == 0:
        return ''.join((args[:(len(args) // 2)], str(len(args)), args[(len(args) // 2):]))
    else:
        return False


