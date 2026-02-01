valor_uma_bola = 4.5
valor_duas_bolas = 7.5
valor_tres_bolas = 10
preco_total = 0
quantidade = int(input("Informe a qt: "))

if(quantidade >3 or quantidade < 1):
    print("Informe de 1 - 3")
    exit()

valor = float(input("Informe o valor entregue: "))
preco_total = valor_uma_bola if quantidade == 1 else valor_duas_bolas if quantidade == 2 else valor_tres_bolas
tem_troco = valor > preco_total
falta = valor < preco_total


print("preço: ", preco_total)
print(f"O valor {valor} { "" if valor >= preco_total else "não"} é suficiente para o preço de {preco_total}")

if(tem_troco):
    print(f"Troco de {valor - preco_total}")

if(falta):
    print(f"Faltam: {preco_total - valor}")