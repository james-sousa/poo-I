palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que voce quer: ")
list(palavra)

for i in range(len(palavra)):
    caractere = palavra[i]
    if letra == caractere:
        print(f"A letra esta na posicao {i}.")

    
