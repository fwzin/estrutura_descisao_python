# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('digite um numero: '))
num2 = float(input('digite mais um numero: '))

if num1 > num2:
    print('o numero maior é: {}'.format(num1))
elif num2 > num1:
    print('o maior numero é: {}'.format(num2))
else:
    print('os numeros são iguais')