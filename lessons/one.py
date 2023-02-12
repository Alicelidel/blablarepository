list = input().split() #split() method a string into a a list, default separator is whitespace. 

def inna_func(args):
    if len(args) % 2 == 0: #len() returns the number of elements in the list
        print('True')
    else:
        print('False')
        
inna_func(list)