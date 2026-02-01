import json


with open("3.json", "r", encoding="utf-8") as data:
    matriz = json.load(data)["matriz"]
    
    
medias = []

for i in range(len(matriz)):
    nota_aluno = 0
    for j in range(len(matriz[i])):
        item =matriz[i][j]
        nota_aluno += item
    medias.append(nota_aluno / len(matriz[i]))

for i in range(len(medias)):
    media = medias[i]
    status = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    print(f"Média do aluno {i + 1}: {media}. Status: {status}")
    


maior_media = max(medias)
menor_media = min(medias)

print(f"Maior média: {maior_media}. Menor: {menor_media}")