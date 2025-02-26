# limpar o terminal
import os 
os.system("clear")

# entrada 
valor_produto = float(input ("digite o valor do produto: "))
forma_de_pagamento = int(input("""
1- a vista                               
2- a prazo                             
digite a forma de pagamento"""))

match forma_de_pagamento:
    case 1:
        # aplicando desconto de 10%
        desconto = valor_produto * 0.10
    case 2:
        ...    
    case _:
        print("opção inválida")