import random

def gerar_gabarito():
    gabarito = []
    for _ in range(13):
        num = random.randint(1, 3)
        gabarito.append(num)
    return gabarito

def gerar_cartao(numero):
    cartao = []
    for _ in range(13):
        num = random.randint(1, 3)
        cartao.append(num)
    return (numero, cartao)

def verificar_acertos(gabarito, cartao):
    acertos = 0
    for i in range(13):
        if gabarito[i] == cartao[i]:
            acertos += 1
    return acertos

# Gerar gabarito
gabarito = gerar_gabarito()

# Gerar cartões de aposta
apostador1 = gerar_cartao(1)
apostador2 = gerar_cartao(2)
apostador3 = gerar_cartao(3)

# Verificar acertos dos apostadores
acertos1 = verificar_acertos(gabarito, apostador1[1])
acertos2 = verificar_acertos(gabarito, apostador2[1])
acertos3 = verificar_acertos(gabarito, apostador3[1])

# Imprimir resultados
print("Número do apostador:", apostador1[0])
print("Número de acertos:", acertos1)
if acertos1 == 13:
    print("Ganhador")

print("\nNúmero do apostador:", apostador2[0])
print("Número de acertos:", acertos2)
if acertos2 == 13:
    print("Ganhador")

print("\nNúmero do apostador:", apostador3[0])
print("Número de acertos:", acertos3)
if acertos3 == 13:
    print("Ganhador")
