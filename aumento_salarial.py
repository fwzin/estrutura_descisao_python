"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

Salario_Atual = float(input('digite o seu salario atual :'))

if Salario_Atual <= 280.00:

    aumento1 = Salario_Atual * (20/100)
    salario_com_aumento1 = aumento1 + Salario_Atual

    print('o salário antes do reajuste: {:.2f}'.format(Salario_Atual))
    print('o percentual de aumento aplicado foi de: 20%')
    print('o valor do aumento: {:.2f}'.format(aumento1))
    print('o novo salário, após o aumento é de: {:.2f}'.format(salario_com_aumento1))


if 280 < Salario_Atual <= 700:

    aumento2 = Salario_Atual * (15/100)
    salario_com_aumento2 = aumento2 + Salario_Atual

    print('o salário antes do reajuste: {:.2f}'.format(Salario_Atual))
    print('o percentual de aumento aplicado foi de: 15%')
    print('o valor do aumento: {:.2f}'.format(aumento2))
    print('o novo salário, após o aumento é de: {:.2f}'.format(salario_com_aumento2))

if 700 < Salario_Atual  <= 1500:

    aumento3 = Salario_Atual * (10/100)
    salario_com_aumento3 = aumento3 + Salario_Atual

    print('o salário antes do reajuste: {:.2f}'.format(Salario_Atual))
    print('o percentual de aumento aplicado foi de: 10%')
    print('o valor do aumento: {:.2f}'.format(aumento3))
    print('o novo salário, após o aumento é de: {:.2f}'.format(salario_com_aumento3))

if 1500 < Salario_Atual:

    aumento4 = Salario_Atual * (5/100)
    salario_com_aumento4 = Salario_Atual + aumento4

    print('o salário antes do reajuste: {:.2f}'.format(Salario_Atual))
    print('o percentual de aumento aplicado foi de: 5%')
    print('o valor do aumento: {:.2f}'.format(aumento4))
    print('o novo salário, após o aumento é de: {:.2f}'.format(salario_com_aumento4))


else:
    print("O salário não se enquadra nos critérios de reajuste.")