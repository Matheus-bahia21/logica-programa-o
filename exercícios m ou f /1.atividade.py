# limpar o terminal
import os 
os.system("clear")


#entrada 

altura = float(input("digite sua altura: "))
sexo = input("digite seu sexo: ")

#processamento 

match sexo:
    case "M": 
        peso_ideal = (72.7 * altura) - 58
        print(f"\npeso ideal: {peso_ideal}")
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"\npeso ideal: {peso_ideal}")
    case _:
        print("opção inválida")