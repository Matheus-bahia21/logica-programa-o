import os 

os.system("clear || cls ")

login_cadastrado = "Matheus"
senha_cadastrada = "1234"


for i in range(3):
    input_login = input("digite seu login:")
    input_senha = input ("digite sua senha:")
    if input_login == login_cadastrado and input_senha == senha_cadastrada:
        print("BEM-VINDO")
        break
    else: 
        print("LOGIN OU SENHA IMCORRETOS")
        if i == 2: 
            print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS")
            break
        
        print("repetindo....")
