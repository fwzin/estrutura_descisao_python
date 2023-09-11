"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

print('programa CMA - calculo de media de aluno')


nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota: '))

media = ((nota1 + nota2)/2)

if 9.0 <= media <= 10.0:

    print('as notas são N1 {:.1f} e N2 {:.1f}'.format(nota1, nota2))
    print('a media correspondente as notas é: {:.1f}'.format(media))
    print('o conceito correspondente a media é: A')
    print('o aluno foi APROVADO')

if 7.5 <= media <= 9.0:

    print('as notas são N1 {:.1f} e N2 {:.1f}'.format(nota1, nota2))
    print('a media correspondente as notas é: {:.1f}'.format(media))
    print('o conceito correspondente a media é: B')
    print('o aluno foi APROVADO')

if 6.0 <= media <= 7.5:

    print('as notas são N1 {:.1f} e N2 {:.1f}'.format(nota1, nota2))
    print('a media correspondente as notas é: {:.1f}'.format(media))
    print('o conceito correspondente a media é: C')
    print('o aluno foi APROVADO')

if 4.0 <= media <= 6.0:

    print('as notas são N1 {:.1f} e N2 {:.1f}'.format(nota1, nota2))
    print('a media correspondente as notas é: {:.1f}'.format(media))
    print('o conceito correspondente a media é: D')
    print('o aluno foi REPROVADO')

if 0.0 <= media <= 4.0:

    print('as notas são N1 {:.1f} e N2 {:.1f}'.format(nota1, nota2))
    print('a media correspondente as notas é: {:.1f}'.format(media))
    print('o conceito correspondente a media é: E')
    print('o aluno foi REPROVADO')