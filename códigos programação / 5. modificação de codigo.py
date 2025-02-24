# limpar o terminal
import os 
os.system("clear") 

# elabore um algoritimo para solicitar dois números e ao final mostre na tela:
# a media, a soma, o produto, o menor valor e o maior valor
# usando uma linha para cada resultado. 


primeiro_numero = float(input("digite a priemira nota: "))
segundo_numero = float(input("digite a segunda nota: "))

media = (primeiro_numero + segundo_numero) / 2 
produto = primeiro_numero * segundo_numero

menor  = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)


print ("\nexibindo resultado: ")
print (f"media: {media}")
print (f"produto: {produto}")
print (f"menor: {menor}")     
print (f"maior: {maior}")
