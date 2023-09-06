
lista = []

while True:
    numero = int(input())
    if numero > 0:
        lista.append(numero)
    else:
        break

lista2 = []

for x in lista:
    if x % 2 == 0:
        lista2.append(x)

print(lista2)