import os 
import time 

os.system("clear || cls ")

contador = 0
soma_salario =0
maior_idade = 0
menor_idade = 0
mulheres5k = 0


while True: 
   print("""
CÓDIGO | DESCRIÇÃO 
   1   | Adicionar pessoa
   2   | Exibir resultados
   3   | Sair   
""")
   
   opcao = int(input ("digite a opção desejada: "))

   match opcao: 
    case 1 : 
       idade = int(input("digite sua idade: "))
       sexo = input("informe seu sexo - use 'm' ou 'f': "). upper()
       salario = float(input("digite seu salario: "))
       contador += 1
       soma_salario += salario
       maior_idade = max(maior_idade, idade)
       menor_idade = min(menor_idade, idade)
       if sexo == "f" and salario >= 5000: 
          mulheres5k
       os.system("cls || clear")   
    case 2 : 
         if contador > 0:  
            media_salarial = soma_salario / contador  
            print("\n = exibindo resultados = ")
            print(f"media salarial do grupo: {media_salarial} ")
            print(f"maior idade do grupo: {maior_idade} ")
            print(f"menor idade do grupo: {menor_idade} ")
            print(f"quantidade de mulheres com salario a partir de 5k: {mulheres5k} ")
         else: 
            print("\nnão foram informados os dados necessários. ")   
         time.sleep(3)   
         os.system("cls || clear")
    case 3 :  
         print("\n = fim =")
         break
    case _: 
         print("\nopção inválida. ")  
         time.sleep(3)
         os.system("cls || clear")
         