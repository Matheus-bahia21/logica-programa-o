import os 

os.system("clear || cls ")

def numeracao(numero):

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

print("= PAR OU IMPAR =")
numero = int(input("digite um numero: "))
numeracao(numero)