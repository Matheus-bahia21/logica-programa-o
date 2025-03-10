# limpar o terminal
import os 
os.system("clear || cls ")


matricula = input ("digite sua matricula : ")
ano_de_nascimento = int(input("digite seu seu ano de nascimento : "))
tempo_de_trabalho = int(input("digite seu tempo de trabalho em anos: "))

idade = 2025 - ano_de_nascimento

if idade >= 65 or tempo_de_trabalho >= 30 : 
    resultado = " requer aposentadoria. "
else: 
    resultado = " não requer aposentadoria. " 

print(f"\nmatricula: {matricula}")  
print(f"idade: {idade}")         
print(f"tempo de trabalho: {tempo_de_trabalho}")     
print(f"resultado: {resultado}")     