lista = []

while True:
    numero = int(input("Numero: "))
    if numero not in lista:
        lista.append(numero)
    else:
        print("Valor já cadastro!")
        print("Não vou cadastrar!")
    
    escolha = str(input("Deseja adicionar mais valores (S/N)? "))
    if escolha in 'Nn':
        break


lista.sort()

print(lista)