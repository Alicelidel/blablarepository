class NotAStringException(Exception):
    pass

def inna_func_add_sum_to_the_middle(args):
    if len(args) % 2 == 0:
        args = ''.join((args[:(len(args) // 2)], str(len(args)), args[(len(args) // 2):]))
        return True
    elif not isinstance(args, str):
        return NotAStringException('not a string')
    return False

