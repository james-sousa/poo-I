def isTriAnguloRect(lado1,lado2,lado3):
    if lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
        return True
    else:
        return False


lado1 = int(input("Digite o lado1: "))
lado2 = int(input("Digite o lado2: "))
lado3 = int(input("Digite o lado3: "))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print("Não eh possivel formar o triangulo!")

else:


    if lado1 == lado2 and lado3 == lado1:
        print("Equilatero!")
    
    elif lado1 != lado2 and lado3 or lado2 != lado3:
        print("Escaleno")
    
    else:
        print("Isoceles!")

n = isTriAnguloRect(lado1,lado2,lado3)

print(n)
