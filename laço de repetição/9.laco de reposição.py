import os 

os.system("clear || cls ")

print("somando números")
soma = 0
for i in range(5):
  nota = float(input(f"digite o {i + 1}ª número: "))
  soma = soma + nota

print() 
print(f"soma: {soma}")

print("\nfim do programa")    