def fatorial_iterativa(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1,n+1):
            fatorial *= i
        return fatorial
         
    
n = int(input("Digite um numero: "))
if fatorial_iterativa:
    r = fatorial_iterativa(n)

print(r)
            