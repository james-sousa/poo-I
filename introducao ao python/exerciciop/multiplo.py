inicio = 0
final = 40

while final >= inicio:
    if inicio % 4 == 0 or inicio % 10 == 0:
        print("PIN")
    elif inicio == 40:
        print("FIM")
    
    else:
        print(inicio)
    
    
    inicio +=1