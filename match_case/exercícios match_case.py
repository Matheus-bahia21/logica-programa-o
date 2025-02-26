# limpar o terminal
import os 
os.system("clear")

# faça um algoritimo que solicite ao usuario dois números 
# e um caractere que calcula as operações básicas (+ * /)
# mostre os números informados pelo usuário
# o operador escolhido e o resultado 

# entrada 
primeiro_numero = int(input("digite um número: "))
operador = input("digite a operação que deseja (+ - * /):")
segundo_numero = int(input("digite um número: "))

# processamento 
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero    
    case "*":
        resultado = primeiro_numero * segundo_numero 
    case "/":
        resultado = primeiro_numero / segundo_numero    
    case _: 
        resultado = "operação invalida."  

# saída 
print(f"\nprimeiro número: {primeiro_numero}") 
print(f"operação : {operador}")     
print(f"segungo número: {segundo_numero}") 
print(f"resultado: {resultado}")