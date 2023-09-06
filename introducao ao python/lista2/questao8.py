import random

gabarito = []
apostador1 = []
apostador2 = []
apostador3 = []
n = 0
while n < 14:
    numero = random.randint(1,3)
    gabarito.append(numero)
    numero2 = random.randint(1,3)
    apostador1.append(numero2)
    numero3 = random.randint(1,3)
    apostador2.append(numero3)
    numero4 = random.randint(1,3)
    apostador3.append(numero4)
    n = n + 1

if apostador1 == gabarito:
    print("Ganhador")
elif apostador1 != gabarito:
    acertos = 0
    for n in range(len(apostador1)):
        if gabarito[n] == apostador1[n]:
            acertos += 1
    print(acertos,"Acertos")
    print("cartao de reposta do jagador1: ",apostador1)

if apostador2 == gabarito:
    print("Ganhador")

elif apostador2 != gabarito:
    acertos = 0
    for n in range(len(apostador2)):
        if gabarito[n] == apostador2[n]:
            acertos += 1
    print(acertos,"Acertos")
    print("cartao de reposta do jagador2: ",apostador2)


if apostador3 == gabarito:
    print("Ganhador")

elif apostador1 != gabarito:
    acertos = 0
    for n in range(len(apostador3)):
        if gabarito[n] == apostador3[n]:
            acertos += 1
    print(acertos,"Acertos")
    print("cartao de reposta do jagador1: ",apostador3)


    print("\n resultado oficial: ",gabarito)

