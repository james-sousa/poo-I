numero = int(input("Numero: "))

fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    
    numero -= 1

print("Fatorial: ",fatorial)