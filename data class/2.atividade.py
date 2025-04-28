import os
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class pessoa:
    nome: str
    email: str
    telefone: float
    endereço: float

print("solicitando dados: ")
Nome = input("Digite seu nome: ")
email = input("Digite seu email:")
endereço = input("Digite seu endereço:")
telefone = input("Digite seu telefone: ")

pessoa2 = pessoa(email, Nome, endereço, telefone)

print("\nexibindo dados:")
print(f"Nome: {pessoa2.nome}, email: {pessoa2.email}, endereço: {pessoa2.endereço}, telefone: {pessoa2.telefone}")