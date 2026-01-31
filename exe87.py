from functools import reduce

nome = input("Insira seu nome: ")
saltos : list[int]= []
for i in range (5):
    salto = float(input(f"Informe o {i + 1}º salto: "))
    saltos.append(salto)
saltos.sort()
saltos.remove(min(saltos))
saltos.remove(max(saltos))

print(f"{nome}, sua média de saltos é de {reduce(lambda x, y: x + y, saltos)  / len(saltos)}m")