from functools import reduce
total_temperatuas = int(input("Quantas temperaturas deseja informar? "))

temperaturas: list[float]= []

for i in range(total_temperatuas):
    temperatura = float(input(f"Informe a {i + 1}º temperatura: "))
    temperaturas.append(temperatura)
    
    
temperaturas.sort()
print(f"Menor: {temperaturas[0]}, Maior: {temperaturas[len(temperaturas) -1]}, Média: {reduce(lambda x,y: x+y, temperaturas) / len(temperaturas)}")