numero = int(input("Numero: "))

cont = numero - 1

while cont > 1:
    if numero % cont == 0:
        print("nao Eh primo")
        break
    cont -= 1
else: 
    print("Eh primo!")
        
    
    
    

    
    