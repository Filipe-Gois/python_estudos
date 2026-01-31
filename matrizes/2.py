import json
with open("2.json", 'r', encoding="utf-8") as arquivo:
    matriz = json.load(arquivo)["matriz"]
    

total = 0
    

for i1 in range(len(matriz)):

    for i2 in range(len(matriz[i1])):
        for i3 in range(len(matriz[i1][i2])):
            current = matriz[i1][i2][i3]           
            total +=current
        

    print(*matriz[i1])
    print()
    
print("total: ", total)