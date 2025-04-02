import os 

# faça uma função sem retorno com o nome: login_senai ()
# limpando o terminal e inserido: === SENAI DENDEZEIROS ===

# Solicite ao usuario dois números 
# cada um em uma variável diferente 
# crie uma função com retorno para somar os dois números informados pelo usuario 

os.system("clear || cls ")

def logo_senai () :
    os.system("cls || clear")
    print("==SENAI DENDEZEIROS==")

def somar(n1, n2):
    return n1 + n2 

def subtrair(n1, n2):
    return n1 - n2 

def dividir(n1, n2):
    return n1 / n2 


def multiplicar(n1, n2):
    return n1 * n2 

logo_senai()
n1 = int(input("digite o primeiro numero: "))

logo_senai()
n2 = int(input("digite o segundo numero: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2)
divisao = dividir(n1, n2)
multiplicacao = multiplicar(n1, n2)


logo_senai() 
print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"divisão: {divisao}")
print(f"multiplicação: {multiplicacao}")