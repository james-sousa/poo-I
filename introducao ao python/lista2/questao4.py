
def string_ordenada(palavra):
    palavra_lista = list(palavra)
    for l in range(len(palavra_lista)):
        for p in range(l + 1, len(palavra_lista)):
            if palavra_lista[p] < palavra_lista[l]:
                palavra_lista[l], palavra_lista[p] = palavra_lista[p], palavra_lista[l]
    palavra_string = ''.join(palavra_lista)
    print(palavra_string)

if string_ordenada:
    palavra = input("Difite uma palavra: ")
    string_ordenada(palavra)





    