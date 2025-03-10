# limpar o terminal
import os 
os.system("clear")

#entrada 

nome = input ("digite seu nome: ")
primeira_nota = float(input("digite a priemira nota: "))
segunda_nota = float(input("digite a segunda nota: "))

media = (primeira_nota + segunda_nota) / 2 

print(f"media: {media}")

if media >= 9:
    conceito = "A"
elif media >= 7.5 :
    conceito = "b"
elif media >= 6 :
    conceito = "c"
elif media >= 4 :
    conceito = "d"       
else :
    conceito = "e"    
   
match conceito: 
    case "A" | "b" | "c" :
        print (f" conceito {conceito}")
        print ("aprovado")
    case "d" | "e" :  
        print (f" conceito {conceito}")
        print ("reprovado")
    case _: 
        print("opção inválida. ")