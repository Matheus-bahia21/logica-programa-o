import os 

os.system("clear || cls ")

while True: 
    nota1 = int(input ("diigte sua primeira nota: "))
    nota2 = int(input ("diigte sua segunda nota: "))
    
    if nota1 | nota2 < 0 or nota1 | nota2 > 10: 
        print("repetindo....")  
    else : 
        break


media = (nota1+nota2) /2

print(f"a primeiro nota do aluno é: {nota1}")
print(f"a segunda nota do aluno é: {nota2}")
print(f"sua media: é {media}")