"""lista = []
mai = 0
men = 0

for x in range(0,5):
    lista.append(int(input("Numero: ")))
    if x == 0:
        mai = men = lista[x]
    else:
        if lista[x] > mai:
            mai = lista[x]
        if lista[x] < men:
            men = lista[x]

print(f'O maior numero digitado foi {mai} nas posicoes', end=' ')

for i, v in enumerate(lista):
    if v == mai:
        print(f'{i+1}...',end='')

print()
print(f'O menor numero digitado foi {men} nas posicoes', end=' ')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i+1}...',end='')

print()
"""
#solução 2

lista = []
maior = 0
menor = 0 
op = 5

while op > 0:
    numero = int(input("Numero: "))
    lista.append(numero)
    op = op - 1

for x in range(len(lista)):
    if x == 0:
        maior = menor = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]

print(f'O maior numero foi {maior} nas posições',end=' ')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...',end='')

print()

print(f'O menor numero foi: {menor} nas posições ',end=' ')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...',end='')

print()