numero = input("informe o número: ")
if(int(numero) <= 0 or int(numero) >= 1000):
    print("Insira um número entre 0 e 1000")
    exit()
res = ""

if len(numero) == 3:
    res = f"{numero[0]} centenas, {numero[1]} dezenas, {numero[2]} unidades"
elif len(numero )== 2:
    res = f"{numero[0]} dezenas, {numero[1]} unidades"
else:
    res = f"{numero[0]} unidades"

print(f"{numero} = {res}")