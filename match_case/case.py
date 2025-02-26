# limpar o terminal
import os 
os.system("clear")

# exemplo de estrutura condicional animada. 
# macth-case substitui o uso do if-elif-else

dia = input("digite dia da semana ")
match dia:
    case "segunda":
        print("hoje é segunda-feiera.")
    case "terça":
        print("hoje é terça-feiera.")
    case "quarta":
        print("hoje é quarta-feiera.")
    case "quinta":
        print("hoje é quinta-feiera.")
    case "sexta":
        print("hoje é sexta-feiera.")
    case "sabado" | "domingo":
        print("hoje é fim de semana.")
    case _:
        print("dia invalido.") 

print(dia)

print("===fim===")