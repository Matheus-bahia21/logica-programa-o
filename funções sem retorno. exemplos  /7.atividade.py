import os 

os.system("clear || cls ")

def imprimir_tabuada(numero):
    for i in range( 0 , 11 ):
        print(f"{numero} x {i} = {numero * i}")


print("= TABUADA =")
numero = int(input("Digite um número de 1 a 10 para ver sua tabuada: "))        
imprimir_tabuada(numero)