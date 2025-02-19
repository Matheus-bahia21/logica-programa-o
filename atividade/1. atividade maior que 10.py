# limpar o terminal
import os 
os.system("clear") 

# elaborar um algoritimo para solicitar ao usuario um valor 
# escrever a mensagem: é maior que 10!
# se o valor lido for maior que 10, caso contario escrever:
# não é maior que 10!

numero = int(input("digite um número: "))

if numero < 10:
    print ("é menor que 10!")
else: 
    print ("não é menor que 10!") 
   