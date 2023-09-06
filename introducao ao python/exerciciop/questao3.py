
for x in range(0,41):
    if x % 4 == 0 or x % 10 == 0:
        print("PIN")
    if x == 40:
        print("FIM")
    else:
        print(x)