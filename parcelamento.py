valor_compra = float(input("Informe o valor: "))
qnt_parcelas  = int(input("qnts parcelas: "))
 
valor_final = valor_compra

if qnt_parcelas <= 3:
    print(f"sem juros: {valor_final}")
    
elif qnt_parcelas <= 6:
    juros_percent = 5
    valor_final += (valor_final / 100) * juros_percent
    print(f"Juros de {juros_percent}%. Valor de cada parcela {valor_final / qnt_parcelas} .Valor final {valor_final}")
    
elif qnt_parcelas <= 12:
    juros_percent = 10
    valor_final += (valor_final / 100) * juros_percent
    print(f"Juros de {juros_percent}%. Valor de cada parcela {valor_final / qnt_parcelas} .Valor final {valor_final}")
    
    
    
else:
    print("Até 12 parcelas")