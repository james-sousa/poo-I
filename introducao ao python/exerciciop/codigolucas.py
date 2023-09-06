horas = int(input("horas :"))

semana = horas // 168
diar = horas % 168
dia = diar // 24
hora = dia // 60
print(semana,dia,hora)