salario = float(input("Salario: "))

if salario > 2000.00 and salario <= 3000.00:
    print("Taxa de 8%")
    imposto = (salario * 8) / 100
    print("Imposto a pagar: ",imposto)

elif salario > 3000.00 and salario <= 4500.00:
    print("Taxa de 18%")
    imposto = (salario * 18) / 100
    print("Imposto a pagar: ",imposto)

elif salario > 4500.00:
    print("Taxa de 28%")
    imposto = (salario * 28) / 100
    print("Imposto a pagar: ",imposto)

else:
    print("Isento")