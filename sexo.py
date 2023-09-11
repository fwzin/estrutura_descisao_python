"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = str(input('digite seu sexo: M ou F? '))

if sexo == 'F' or sexo == 'f' or sexo == 'feminino':
    print("F - Feminino")
elif sexo == 'M' or sexo == 'm' or sexo == 'masculino':
    print("M - Masculino")
else:
    print("Sexo Inválido")

    