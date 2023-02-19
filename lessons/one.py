class NotAListException(Exception):
    pass

def inna_func(args: list):
    if not isinstance(args, list):
        return NotAListException('not a list')
    return len(args) % 2 == 0

#def lera_func(a: list[int]):
#    for x in a:
#        if not isinstance(x, int):
#            return Exception('not a number')
#        for i in range(2, x - 1):
#            if x % i == 0:
#                break
#        else:
#            return True
#    else:
#        return False
