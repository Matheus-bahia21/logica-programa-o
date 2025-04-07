import os 

os.system("clear || cls ")

def numeracao(numero):

    if numero > 0:
        print(f"O número {numero} positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else : 
        print ("zero é um numero neutro ")

print("= positivo ou negativo =")
numero = int(input("digite um numero: "))
numeracao(numero)