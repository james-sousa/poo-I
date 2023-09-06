def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def media_aluno(nome_aluno, notas_alunos):
    if nome_aluno in notas_alunos:
        notas = notas_alunos[nome_aluno]
        media = calcular_media(notas)
        return media
    else:
        return None

notas_alunos = {}

while True:
    nome_aluno = input("Digite o nome do aluno (ou digite 'sair' para encerrar): ")
    if nome_aluno.lower() == "sair":
        break

    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    notas_alunos[nome_aluno] = [nota1, nota2]

print("--- Médias dos alunos ---")
for aluno in notas_alunos:
    media = media_aluno(aluno, notas_alunos)
    print(f"Aluno: {aluno} - Média: {media}")
