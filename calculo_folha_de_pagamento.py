"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

print('programa CDFP (calculo de folha de pagamento)')

valor_hora = float(input('digite o valor da sua hora trabalhada: '))
hora_mês = float(input('digite a quatidade de horas trabalhadas no mês: '))

salario_bruto = (valor_hora * hora_mês)

if salario_bruto <= 900:

    ir                  = (0)
    sindicato           = (salario_bruto * (3/100))
    fgts                = (salario_bruto * (11/100))
    total_de_descontos  = (sindicato + ir)
    salario_liquido     = (salario_bruto - total_de_descontos)

    print('Salário Bruto:                  : R$ {:.2f}'.format(salario_bruto))
    print('IR (isento)                     : R$ 000,00')
    print('sindicato (3%)                  : R$ {:.2f}'.format(sindicato))
    print('FGTS (11%)                      : R$ {:.2f}'.format(fgts))
    print('Total de descontos              : R$ {:.2f}'.format(total_de_descontos))
    print('Salário Liquido                 : R$ {:.2f}'.format(salario_liquido))

if 900 < salario_bruto <= 1500:

    ir                  = (salario_bruto * (5/100))
    sindicato           = (salario_bruto * (3/100))
    fgts                = (salario_bruto * (11/100))
    total_de_descontos  = (sindicato + ir)
    salario_liquido     = (salario_bruto - total_de_descontos)

    print('Salário Bruto: (5 * 220)        : R$ {:.2f}'.format(salario_bruto))
    print('IR (5%)                         : R$ {:.2f}'.format(ir))
    print('sindicato (3%)                  : R$ {:.2f}'.format(sindicato))
    print('FGTS (11%)                      : R$ {:.2f}'.format(fgts))
    print('Total de descontos              : R$ {:.2f}'.format(total_de_descontos))
    print('Salário Liquido                 : R$ {:.2f}'.format(salario_liquido))

if 1500 < salario_bruto <= 2500:

    ir                  = (salario_bruto * (10/100))
    sindicato           = (salario_bruto * (3/100))
    fgts                = (salario_bruto * (11/100))
    total_de_descontos  = (sindicato + ir)
    salario_liquido     = (salario_bruto - total_de_descontos)

    print('Salário Bruto: (5 * 220)        : R$ {:.2f}'.format(salario_bruto))
    print('IR (10%)                        : R$ {:.2f}'.format(ir))
    print('sindicato (3%)                  : R$ {:.2f}'.format(sindicato))
    print('FGTS (11%)                      : R$ {:.2f}'.format(fgts))
    print('Total de descontos              : R$ {:.2f}'.format(total_de_descontos))
    print('Salário Liquido                 : R$ {:.2f}'.format(salario_liquido))

if 2500 < salario_bruto:

    ir                  = (salario_bruto * (20/100))
    sindicato           = (salario_bruto * (3/100))
    fgts                = (salario_bruto * (11/100))
    total_de_descontos  = (sindicato + ir)
    salario_liquido     = (salario_bruto - total_de_descontos)

    print('Salário Bruto: (5 * 220)        : R$ {:.2f}'.format(salario_bruto))
    print('IR (20%)                        : R$ {:.2f}'.format(ir))
    print('sindicato (3%)                   : R$ {:.2f}'.format(sindicato))
    print('FGTS (11%)                      : R$ {:.2f}'.format(fgts))
    print('Total de descontos              : R$ {:.2f}'.format(total_de_descontos))
    print('Salário Liquido                 : R$ {:.2f}'.format(salario_liquido))

else:
    print('valor incorreto repita o processo e insira os dados corretamente')