import functools as ft

def ispar(x):
    return x % 2 == 0 and x != 0

def soma(a,b):
    return a + b

lista = [1,2,3,4]

par = filter(ispar,lista)

resultado = list(par)

a = ft.reduce(soma, resultado)

print(a)