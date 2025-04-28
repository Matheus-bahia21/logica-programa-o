import os
os.system("clear")

vetor = []
negativos = 0
soma_positivos = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    
    if numero < 0:
        negativos += 1
    else:
        soma_positivos += numero


print("\nQuantidade de números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)