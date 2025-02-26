# limpar o terminal
import os 
os.system("clear")

#entrada 
dia = int(input("digite um número para o dia da semana :"))
                  
# processamento

match dia: 
    case 1:
        print("domingo.")
    case 2:
        print("segunda-feira.")  
    case 3:
        print("terça-feira. ")   
    case 4:
        print("quarta-feira. ")       
    case 5:
        print("quinta-feira . ")
    case 6:
        print("sexta-feira. ")
    case 7:
        print("sabado. ")    

    case _: 
        print("dia invalido")   