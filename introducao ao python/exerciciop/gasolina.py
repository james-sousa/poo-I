
def alcool(n):
    if n <= 20:
        desconto = (n * 3) / 100
        resultado = 3.45 * desconto
        print("O desconto foi de 3%")
        print("O preco a pagar eh: ",resultado)

    else:
        desconto = (n * 5) / 100
        resultado = 3.45 * desconto
        print(desconto)

def gasolina(n):
    if n <= 20:
        desconto = (n * 4) / 100
        resultado = 4.53 * desconto
        print("O desconto foi de 4%")
        print("O preco a pagar eh: ",resultado)

    else:
        desconto = (n * 6) / 100
        resultado = 4.53 * desconto
        print(desconto)


escolha = input("Digite A-alcool ou G-gasolina: ")

if escolha == "A":
    n = float(input("Digite a quantidade de litros: "))
    alcool(n)

elif escolha == "G":
    n = float(input("Digite a quantidade de litros: "))
    gasolina(n)
