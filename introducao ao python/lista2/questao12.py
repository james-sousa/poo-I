def obter_melhor_volta(corredores):
    melhor_volta = float("inf")
    for corredor, tempos in corredores.items():
        for volta, tempo in enumerate(tempos, start=1):
            if tempo < melhor_volta:
                melhor_volta = tempo
                corredor_melhor_volta = corredor
                volta_melhor_volta = volta

    return corredor_melhor_volta, volta_melhor_volta

def obter_campeao(corredores):
    menor_media = float("inf")
    for corredor, tempos in corredores.items():
        media = sum(tempos) / len(tempos)
        if media < menor_media:
            menor_media = media
            campeao = corredor

    return campeao

corredores = {}

for i in range(1, 6):
    nome_corredor = input(f"Digite o nome do corredor {i}: ")
    tempos = []
    for volta in range(1, 4):
        tempo = float(input(f"Digite o tempo da volta {volta} para o corredor {nome_corredor} (em segundos): "))
        tempos.append(tempo)
    corredores[nome_corredor] = tempos

melhor_volta_corredor, melhor_volta_volta = obter_melhor_volta(corredores)
campeao = obter_campeao(corredores)

print("\n--- Resultados ---")
print(f"A melhor volta da prova foi de {melhor_volta_corredor} na volta {melhor_volta_volta}.")
print(f"O campeão da prova é {campeao}.")
