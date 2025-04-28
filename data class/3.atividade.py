import os
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class pessoa ():
    nome: str
    email: str
    telefone: float
    endereço: float


    def exibindo_dados(self):
        print("\nexibindo dados:")
        print(f"Nome: {self.nome}, email: {self.email}, endereço: {self.endereço}, telefone: {self.telefone}")

print("solicitando dados: ")
Nome = input("Digite seu nome: ")
email = input("Digite seu email:")
endereço = input("Digite seu endereço:")
telefone = input("Digite seu telefone: ")

pessoa1 = pessoa(email, Nome, endereço, telefone)
pessoa1.exibindo_dados()
