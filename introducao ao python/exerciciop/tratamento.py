a = input("Digite um numero: ")
b = input("Digite outro numero: ")

try:
    resultado = float(a)/float(b)
    print(resultado)
except:
    print("Não existe divisao por zero!")