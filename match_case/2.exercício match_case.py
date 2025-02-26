# limpar o terminal
import os 
os.system("clear")

# faça um algoritimo que mostre um menu com opçao de um cardapio de restaurante 
# para uma pessoa 
# a pessoa vai escolher o prato desejado digitando o código do prato 
# após escolher o prato, o algoritimo deve mostrar o nome e valor do prato escolhido. 


# entrada 
opcao = int(input("""
código \t prato \t\t\t valor
1\t picanha \t\t R$ 25,00
2\t lasanha \t\t R$ 20,00
3\t strogonoff \t\t R$ 18,00
4\t bife acebolado\t R$ 15,00
5\t pão com ovo \t\t 5,00

digite a opção desejada:                 
"""))

# peocessamento 
# saída
match opcao: 
    case 1:
        print("picanha - R$ 25,00.")
    case 2:
        print("lasanha -  R$ 20,00.")  
    case 3:
        print("strogonoff - R$ 18,00")   
    case 4:
        print("bife acebolado - R$ 15,00")       
    case 5:
        print("pão com ovo - R$ 5,00")
    case _: 
        print("opção invalida")    