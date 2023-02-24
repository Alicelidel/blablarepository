# на вход массив, нужно вывести True если там есть буква A, большая или маленькая)

#def find_letters_a(args: list):
#    for i in range(len(list)):
#        if list[i] == "a" or list[i] == "A":
#            return True
#        else:
#            return False

def lera_func_find_letters_a(args: list):
    for x in args:
        if x == "a" or x == "A":
            return True  #выход из find_letters_a_func
    return False
