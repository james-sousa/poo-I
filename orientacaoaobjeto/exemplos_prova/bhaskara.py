from math import *

valo1 = float(input("Valor1: "))
valo2 = float(input("Valor2: "))
valo3 = float(input("Valor3: "))

delta = (valo2 * valo2) - (4 * valo1 * valo3)


if delta < 0 or valo1 == 0.0:
    print("Impossivel calcular")

else:
    r1 = ((-valo2) + sqrt(delta)) / (2 * valo1)
    r2 = ((-valo2) - sqrt(delta)) / (2 * valo1)
    print("R1: ",r1)
    print("R2: ",r2)