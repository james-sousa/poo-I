n = int(input("Digite a quantidade de termos: "))

t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    print(t3)
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    


