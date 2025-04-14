import os
os.system("clear || cls ")

# Criando uma lsita.
listas_notas = []

# adicionando 3 notas em uma lista. 
for i in range(3):
    nota = float(input("digite uma nota: "))
    listas_notas.append (nota)

# exibindo todos os valores em uma lista. 
print()  
for nota in listas_notas: # ForEach
    print(nota)