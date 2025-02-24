# limpar o terminal
import os 
os.system("clear") 

# elabore um algoritimo para solicitar ao usuario três notas.
# calcule a media do aluno. 
# casoa media do aluno seja menor que 7, o aluno está reprovado.
# mostrar: media e se está aprovado ou reprovado. 

primeira_nota = float(input("digite a priemira nota: "))
segunda_nota = float(input("digite a segunda nota: "))
terceira_nota = float(input("digite a terceira nota: "))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma 

print(f"media: {media}")

if media < 7:
    print ("reprovado!")
else: 
    print ("aprovado!")    
