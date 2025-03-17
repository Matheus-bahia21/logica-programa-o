import os 

os.system("clear || cls ")


soma = 0
media = 0 

print("notas")
for i in range(4):
  nota = float(input(f"digite a {i + 1}ª nota : "))
  soma += nota 

media = soma /4

print() 

print(f"media: {media}")
print("\nfim do programa")