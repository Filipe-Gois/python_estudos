valor_tabuada = int(input("Informe o numero que quer a tabuada: "))
comeco = int(input("Começo: "))
fim = int(input("Fim: "))

for i in range(comeco, fim + 1):
    print(f"{valor_tabuada} X {i} = {valor_tabuada * i}")