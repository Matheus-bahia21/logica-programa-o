# limpar o terminal
import os 
os.system("clear") 

# elabore um algoritimo para solicitar ao usuario um valor e escreva a mensagem:
# "é maior que 10!"
# se o valor lido for maior que 10, caso contario escrever:
# "não é maior que 10!"
# verifique se o numero digitado é igual a 10, caso seja, escreva a mensagem:
# "o numero ´r igual a 10!"

numero = int(input("digite um número: "))

if numero == 10: 
    print("é igual a 10!")
elif numero > 10:
    print ("é maior que 10!")  
else: 
    print ("não é maior que 10!")      

    