salario_bruto = int(input("Digite o seu salario bruto: "))

inss = (salario_bruto * 8) / 100
imposto_renda = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - (inss + imposto_renda + sindicato)

print("Salario Bruto: R$",salario_bruto)
print("IR (11%) : R$",imposto_renda)
print("INSS (8%) : R$",inss)
print("Sindicato (5%) : R$",sindicato)
print("Salario Liquido : R$",salario_liquido)
