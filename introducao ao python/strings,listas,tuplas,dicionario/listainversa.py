lista = []

while True:
    
    l = int(input("Dgite um numero: "))
    if l !=0:
        lista.append(l)
    else:
        break

lista.reverse()

print(lista)

