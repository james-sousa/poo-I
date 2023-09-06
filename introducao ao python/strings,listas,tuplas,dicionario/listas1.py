
def ispar(x):
    return x%2==0 and x!=0

def iszero(x):
    return x == 0

def isimpar(x):
    return x % 2 != 0 

numero = []

while True:
    num = int(input("Digite um numero: "))
    
    if num < 0:
        break

    numero.append(num)

par = filter(ispar,numero)
zero = filter(iszero,numero)
impar = filter(isimpar,numero)

par = list(par)
impar = list(impar)

par = list(par)
impar = list(impar)
zero = list(zero)

par.sort
impar.sort


print(par + impar + zero)