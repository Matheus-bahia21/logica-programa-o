import os 

os.system("clear || cls ")

contador = 0 
soma = 0


while True: 
    nota = int(input("digite um numero "))
    if nota < 0: 
        break
    else: 
        contador += 1 
        soma += nota

media = soma / contador        

print(f"\nmedia: {media}")
print(f"\nmedia: {contador}")