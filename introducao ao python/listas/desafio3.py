def comparacao(m,n):
    if m > n:
        return m
    else:
        return n




lista = []
cont = 5
while cont > 0:
    numero = int(input("numero: "))
    lista.append(numero)
    
    cont -= 1

resultado = map(comparacao,lista)
resultado = list(resultado)
print(resultado)