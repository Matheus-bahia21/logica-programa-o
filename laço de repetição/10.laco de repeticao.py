import os 

os.system("clear || cls ")

pares = 0
impares = 0

print("números pares e impares: ")
for i in range(5):
    numero = int(input("digite um número: "))
    if  numero % 2 == 0:
        pares += 1
    else : 
        impares += 1


print()
print(f"pares: {pares}")
print(f"impares: {impares}") 

print("\nfim do programa") 