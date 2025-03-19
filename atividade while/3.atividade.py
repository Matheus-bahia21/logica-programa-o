import os 

os.system("clear || cls ")



while True: 
    nota = int(input ("diigte sua nota: "))
    
    if nota < 0 or nota > 10: 
        print("repetindo....")  
    else : 
        break

print(f"a nota do aluno é {nota}")         