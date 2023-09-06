
import functools as ft

Lista = [1,2,3,0,0,4]

filter(lambda x: x % 2 == 0 and x !=0, Lista)

r = ft.reduce(lambda x,y: x+y, Lista)

print(r)