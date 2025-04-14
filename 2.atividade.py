import os
os.system("clear || cls ")

listas_notas = []
quantidade_notas = 3 

for i in range(3):
    nota = float(input("digite uma nota: "))
    listas_notas.append (nota)
    
media = sum(listas_notas) / quantidade_notas


print()
for nota in listas_notas: 
    print(nota)

print(f"media: {media}")   