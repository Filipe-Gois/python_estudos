vendas = [
    [120, 90, 150, 80],    
    [60, 200, 100, 140],  
    [130, 110, 90, 160]   
]

total_vendas_vendedores : list[int] = []
total_vendas_por_dia : list[int] = []
maior_vendedor = {}
maior_individual = {
         "iDia":0,
                "iVendedor":0,
                "total": 0
}

for i in range(len(vendas)):
    vendedor_atual = vendas[i]
    total = 0
    for j in range(len(vendedor_atual)):
        venda = vendedor_atual[j]
        total += venda
        if  venda > maior_individual["total"] :
            maior_individual = {
                "iDia":j,
                "iVendedor":i,
                "total": venda

            }
    total_vendas_vendedores.append(total)



for i in range(len(vendas[0])):
    total = 0
    for j in range(len(vendas)):
        total+= vendas[j][i] 
    total_vendas_por_dia.append(total)


maior = max(total_vendas_vendedores)
maior_vendedor = {
    "index": total_vendas_vendedores.index(maior),
    "total":maior
}


print( "Total de vendas: ",total_vendas_vendedores)

print("O maior foi:", maior_vendedor)

print("Total por dia", total_vendas_por_dia)

melhor = max(total_vendas_por_dia)
melhor_dia = {
    "index": total_vendas_por_dia.index(melhor),
    "total":melhor

}

print("A maior venda individual foi:", maior_individual)