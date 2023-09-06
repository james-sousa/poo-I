import functools as ft

lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

def maior(n,n1):
    if n > n1:
        n2 = n
        return n2
    else:
        return n1



p = ft.reduce(maior,lista)



print(p)




