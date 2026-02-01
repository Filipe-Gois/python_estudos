import json


with open ("3.json", "r", encoding="utf-8") as data:
    
    matriz = json.load(data)["matriz"]
    
    
total = 0
dias: list[int] = [0,0,0]
produtos: list[int] = [0,0,0]
    
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        item = matriz[i][j]
        dias[i] += item
        produtos[j] += item
    

for i in range(len(dias)):
    print(f"Dia {i + 1}: R${dias[i]}")

print("---")
print("Total por produto:")

for i in range(len(produtos)):
    print(f"Produto {i + 1}: R${produtos[i]}")
    
dias.sort()
produtos.sort()
dia_com_mais_vendas = dias.index(dias[-1]) + 1
produto_mais_vendido = produtos.index(produtos[-1]) + 1
print(f"O dia com maior venda foi o {dia_com_mais_vendas}º dia")
print(f"O produto mais vendido foi o {produto_mais_vendido}º")