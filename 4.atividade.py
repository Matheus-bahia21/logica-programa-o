import os
os.system("clear || cls ")

lista_pratos = []
preco_pratos = []

while True:

    opcao = int(input("""
código \t prato \t\t\t valor
1\t picanha \t\t R$ 25,00
2\t lasanha \t\t R$ 20,00
3\t strogonoff \t\t R$ 18,00
4\t bife acebolado\t\t R$ 15,00
5\t pão com ovo \t\t R$ 5,00

digite a opção desejada: """))

    match opcao: 
        case 1:
         prato = "picanha"
         preco = 25
        case 2:
         prato = "lasanha"
         preco = 20
        case 3:
         prato = "strogonoff" 
         preco = 18
        case 4:
         prato = "bife acebolado"
         preco =   15   
        case 5:
         prato = "pão com ovo"
         preco = 5
        case _: 
         print("opção invalida. \ntente novamente")    
         prato = ""
         preco = 0
        
    lista_pratos.append(prato) 
    preco_pratos.append(preco) 

    continuar = input("deseja escolher outro prato? \nresponda com 's' ou 'n' ").lower()
    if continuar == "n":
      break

    os.system("clear || cls ")

print("\n= PRATOS ESCOLHIDOS = ")
for prato in lista_pratos:
  print(f"prato: {prato}")

print(f"\ntotal: {sum(preco_pratos)}")  