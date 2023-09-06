
import random

def advinhacao():
    n = random.randint(0,10)
    cont = 10

    while cont > 0:
        cont = cont - 1
        numero = int(input("Digite um numero: "))

        if numero == n:
            print("Você acertou!")
            escolha = input("Deseja jogar novamente? (s/n): ")
            if escolha == "s":
                advinhacao()
            else:
                print("Obrigado por jogar!")
                break
        
        else:
            
            print("Você errou")
            
        print("Agora você tem ",cont,"jogadas")
           
    
    print("Você não venceu obrigado por jogar!")    
    

if advinhacao:
    
    advinhacao()
    
    
        
        
    