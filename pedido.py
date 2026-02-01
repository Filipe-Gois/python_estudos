preco = float(input("preco: "))
qnt = int(input("qnt: "))
tipo_cliente = input("tipo: ")
forma_pagamento = input("pagamento: ")
preco *= qnt

if tipo_cliente.lower() == "vip" :
    preco -= (preco / 100) * 10

elif  forma_pagamento.lower() == "pix" :
    preco -= (preco / 100) * 5

if  forma_pagamento.lower() == "cartao" :
    preco += (preco / 100) * 3


print(f"Valor final: {preco}. usuario do tipo {tipo_cliente}")