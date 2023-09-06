lista = []

numeros_digitados = int(input("Digite a quantidade de números da lista: "))

while numeros_digitados > 0:
    x = int(input("Numero: "))
    
    lista.append(x)

    numeros_digitados -= 1

media = sum(lista)

print("Media: ",media/len(lista))