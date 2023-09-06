peso = int(input("Digite o peso: "))
peso_maximo = 50

if peso > peso_maximo:
    excesso = peso - peso_maximo
    multa = excesso * 4
    print("O peso calculado foi: ",peso)
    print("Passou",excesso ,"Kg do limite permitido")
    print("A sua multa e de: R$",multa)

else:
    print(peso)