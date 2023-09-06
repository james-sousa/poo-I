
def calculaMedia(notas):
    medias = {}
    maior_media = 0
    aluno_maior_media = ""

    for aluno, notas_aluno in notas.items():
        media = sum(notas_aluno) / len(notas_aluno)
        medias[aluno] = media

        if media > maior_media:
            maior_media = media
            aluno_maior_media = aluno
    
    return aluno_maior_media, medias
    

notas = {
    "João": [8, 7, 6],
    "Maria": [9, 9, 10],
    "Pedro": [7, 8, 7],
    "Ana": [6, 9, 8]
}

aluno_maior_media, medias = calculaMedia(notas)

print("Aluno com maior média:", aluno_maior_media)
print("Médias dos alunos:")
for aluno, media in medias.items():
    print(aluno, ":", media)
