# limpar o terminal
import os 
os.system("clear")

# Elabore um algoritimo usando operações lógicas para solicitar ao usuário 2 numeros e escrever:
# Os 2 numeros informados
# o maior numero
# o menor numero 

primeiro_numero = float(input("digite a priemiro numero: "))
segundo_numero = float(input("digite a segundo numero: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero


print()
print (f"primeiro numero: {primeiro_numero}")
print (f"primeiro numero: {segundo_numero}")
print (f"menor numero: {menor}")     
print (f"maior numero: {maior}")