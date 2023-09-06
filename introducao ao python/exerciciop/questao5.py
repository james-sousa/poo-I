def area(n):
    if n==1:
        b = int(input("Digite a base: "))
        h = int(input("Digite a altura: "))
        a = (b*h)/2
        return a
    
    elif n == 2:
        lado1 = int(input("Digite o lado1: "))
        lado2 = int(input("Digite o lado2: "))
        lado3 = int(input("Digite o ldao3: "))
        lado4 = int(input("Digite o lado4: "))
        a = lado1+lado2+lado3+lado4
        return a
    
    elif n == 3:
        pi = float(input("Digite o valor de pi: "))
        r = int(input("Digite o valor do raio: "))
        a = pi * (r*r)
        return a
    

n = int(input("Digite \n1-triangulo\n2-quadrado\n3-circulo: "))

if area:
    r = area(n)
    print("O valor da area eh: ",r)