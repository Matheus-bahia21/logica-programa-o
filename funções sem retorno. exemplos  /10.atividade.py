import os 

os.system("clear || cls ")


def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    resultado = soma / 2 
    return resultado 

def verificar_resultado(media):
    if media >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

print("= NOTAS =")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
resultado = verificar_resultado(media)

print(f"Média: {media:.2f}")
print(resultado)