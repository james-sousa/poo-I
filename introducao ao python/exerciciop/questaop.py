import functools as ft

def funcao1(x):
    if x%3 == 0 or x%5 == 0:
        return True
    else:
        return False
    
def funcao2(x,y):
    return x + y

a = (range(15))
b = list(filter(funcao1,a))

print(b)


"""a = list(range(10))
print(a)
"""