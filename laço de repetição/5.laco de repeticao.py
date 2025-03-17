import os 
import time 

os.system("clear || cls ")

print("contagem regressiva")
numero = int(input("digite um numero para contagem regressiva: "))

for i in range(numero, 0,-1) :
    print(i)
    time.sleep(1)
          
print("fim do programa ")    