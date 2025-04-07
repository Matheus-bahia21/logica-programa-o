import os 

os.system("clear || cls ")

def saudacao(parametro): 
    print(f"olá {parametro}! bem-vindo(a) ao nosso site.")


nome_visitante = input("digite seu nome: ")
saudacao(nome_visitante)