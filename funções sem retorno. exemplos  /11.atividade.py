import os 

os.system("clear || cls ")

def converter_para_centimetros(metros):
    return metros * 100


metros = float(input("Digite um valor em metros: "))
centimetros = converter_para_centimetros(metros)

print(f"{metros} metros equivalem a {centimetros} centímetros.")