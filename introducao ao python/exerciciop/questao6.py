def fatorial_recursiva(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*fatorial_recursiva(n-1)
    
n = int(input("Digite um numero: "))
if fatorial_recursiva:
    r = fatorial_recursiva(n)

print(r)