def calculos(numeros):
    media = sum(numeros) / len(numeros)
    numeros.sort()
    meio = len(numeros) // 2
    if len(numeros) % 2 == 0:
        mediana = (numeros[meio - 1] + numeros[meio]) / 2
    else:
        mediana = numeros[meio]
    
    soma = sum((x - media) ** 2 for x in numeros)
    varianciacao = soma / len(numeros)


    desvio_padrao = varianciacao ** 0.5

    print("Média:", media)
    print("Mediana:", mediana)
    print("Variância:", varianciacao)
    print("Desvio Padrão:", desvio_padrao)

if calculos:

    numeros = list(range(1, 101))
    calculos(numeros)

