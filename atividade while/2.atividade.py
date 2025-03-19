import os 

os.system("clear || cls ")

idade = int(input ("diigte sua idade: "))

while idade < 18: 
    print("somente maiores de 18 anos.\n")
    idade = int(input ("diigte sua idade: "))

print ("fim")