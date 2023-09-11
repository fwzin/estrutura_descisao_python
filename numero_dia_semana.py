"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido
"""
numero = int(input("Digite um número (1 a 7) correspondente ao dia da semana: "))

if numero == 1:
    print('1 corresponde ao domingo')
if numero == 2:
    print('2 corresponde a segunda')
if numero == 3:
    print('3 corresponde a terça')
if numero == 4:
    print('4 corresponde a quarta')
if numero == 5:
    print('5 corresponde a quinta')
if numero == 6:
    print('6 corresponde a sexta')
if numero == 7:
    print('7 corresponde a sabado')
else:
    print('numero não corresponde a nenhum dia da semana')