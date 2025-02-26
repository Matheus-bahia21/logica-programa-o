# limpar o terminal
import os 
os.system("clear")


dia = int(input("digite um mês :"))


match dia : 
    case 1:
        print("janeiro.")
    case 2:
        print("fevereiro.")  
    case 3:
        print("março. ")   
    case 4:
        print("abril. ")       
    case 5:
        print("maio. ")
    case 6:
        print("junho. ")
    case 7:
        print("julho. ")
    case 8:
        print("agosto. ") 
    case 9:
        print("setembroo. ")  
    case 10:
        print("outubro. ")  
    case 11:
        print("novembroo. ")  
    case 12:
        print("dezembro. ")  


    case _: 
        print("dia invalido")   