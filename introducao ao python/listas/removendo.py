lista = ['a','b','c','d','b','e','b','d']
lista2 = []
for x in lista:
    if x  == 'b':
        pass
    else:
        lista2.append(x)

print(lista2)


for x,v in enumerate(lista):
    if v == 'b':
        lista.pop(x)

print(lista)
    

