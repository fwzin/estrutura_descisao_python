"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math

def calcular_raizes(a, b, c):
    if a == 0:
        print("A equação não é do segundo grau.")
        return
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma raiz real: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")

def main():
    print("Digite os coeficientes da equação ax^2 + bx + c:")
    a = float(input("a: "))
    
    if a == 0:
        print("A equação não é do segundo grau.")
        return
    
    b = float(input("b: "))
    c = float(input("c: "))
    
    calcular_raizes(a, b, c)

if __name__ == "__main__":
    main()
