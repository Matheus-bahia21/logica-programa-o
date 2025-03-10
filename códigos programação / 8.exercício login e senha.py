# limpar o terminal
import os 
os.system("clear")







login_cadastro = "marta"
senha_cadastrada = "123"

login = input("digite o login: ")
senha = input("digite a senha: ")

if login == login_cadastro and senha == senha_cadastrada: 
    print("bem-vindo")
else: 
    print("login ou senha inválidos!")    