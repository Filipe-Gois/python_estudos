import json

with open("caixa.json", "r", encoding="utf-8") as data:
    matriz = json.load(data)["matriz"]
    
total_semanas = []
total_produtos = [0,0]

for i in range(len(matriz)):
    semana = matriz[i]
    total = 0
    for j in range(len(semana)):
        dia = semana[j]
        
        for h in range(len(dia)):
            produto = dia[h]
            total_produtos[h] += produto
            total += produto
    total_semanas.append(total)

for i in range(len(total_semanas)):
    print(f"Total da {i + 1}º semana: {total_semanas[i]}")
print ("")
for i in range(len(total_produtos)):
    print(f"Produto número {i + 1}: {total_produtos[i]}")
    
total_semanas.sort()
maior_semana_index = total_semanas.index(total_semanas[-1])
print(f"A semana com maior faturamento foi a {maior_semana_index + 1}º semana, com {total_semanas[-1]}")

print ("")
total_produtos.sort()
maior_produto_index = total_produtos.index(total_produtos[-1])
print(f"A produto mais vendido foi o {maior_produto_index}º, com {total_produtos[-1]}")