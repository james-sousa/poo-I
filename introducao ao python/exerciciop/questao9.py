def remove_repetidos(lista):
    lista2 = list(set(lista))
    lista2.sort()
    
            

    return lista2

lista = [2,4,2,2,3,3,1]

resultado = remove_repetidos(lista)

list(resultado)

print(resultado)


