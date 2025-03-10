# limpar o terminal
import os 
os.system("clear")






# entrada 
idade = int(input("digite sua idade: "))

#processamento 
if idade < 18 or idade > 65:
    resultado = "não é obrigado a votar. "
else:
    resultado = "voto obrigatorio. " 

# saída 
print(f"\nresultado: {resultado}")