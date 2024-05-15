# Crie um programa que peça ao usuário para digitar três números (A, B e C). Em seguida, o programa deve calcular e mostrar os valores das raízes da seguinte equação, usando a fórmula de Bhaskara.

import math


numeroA = int(input("Digite o valor de A: "))
numeroB = int(input("Digite o valor de B: "))
numeroC = int(input("Digite o valor de C: "))

delta = numeroB**2 - (4 * numeroA * numeroC)

if delta < 0:
    print(f"A equação {numeroA}x^2 + {numeroB}x + {numeroC} não possui raízes.")
else:
    raiz1 = ((numeroB * -1) + math.sqrt(delta)) / (2 * numeroA)
    raiz2 = ((numeroB * -1) - math.sqrt(delta)) / (2 * numeroA)

    if raiz1 == raiz2:
        print(f"A equação {numeroA}x^2 + {numeroB}x + {numeroC} possui apenas a raiz {raiz1}.")
    else:
        print(f"A equação {numeroA}x^2 + {numeroB}x + {numeroC} possui as raízes {raiz1} e {raiz2}.")