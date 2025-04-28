import os
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("solicitando dados: ")
Nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))


pessoa2 = pessoa(idade, Nome, peso, altura)

print("\nexibindo dados:")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}, peso: {pessoa2.peso}, altura: {pessoa2.altura}")