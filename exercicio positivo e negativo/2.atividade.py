import os 

os.system("clear || cls ")

contador = 0 
quantidade_pares = 0
soma_pares = 0
quantidade_impares = 0
soma_geral = 0

while True:
    numero = int(input(f"digite o {contador + 1}° numero "))

    if numero == 0:
       break

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares = numero     
    else: 
        quantidade_impares += 1

    contador += 1 
    soma_geral += numero

media_pares = soma_pares / quantidade_pares            
media_geral = soma_geral / contador


print(f"\nquantidade de pares: {quantidade_pares}")
print(f"\nquantidade de impares: {quantidade_impares}")
print(f"media geral: {media_geral}")
print(f"media pares: {media_pares}")