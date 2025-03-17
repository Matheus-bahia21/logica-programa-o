import os 

os.system("clear || cls ")

numero = int(input("digite um numero para a tabuada: "))

for i in range (1,11): 
    print(F"{numero} x {i} = {numero * i}")
          
print("fim do programa")