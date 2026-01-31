import json
with open("./1.json", 'r', encoding='utf-8') as arquivo:
    matriz = json.load(arquivo)["matriz"]

pares = 0
maior = 0
soma = 0
diagonalP= 0




for index_linha, linha in enumerate(matriz):
    diagonalP += matriz[index_linha][index_linha]
    for index_numero, numero in enumerate(linha):
        soma += numero
        if(numero > maior):
            maior = numero
        if(numero % 2 == 0):
            pares += 1
    print(*linha)
    
    
print(f"Soma: {soma}")
print(f"diagonalP: {diagonalP}")
print(f"Maior: {maior}")
print(f"pares: {pares}")
