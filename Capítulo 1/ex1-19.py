# :: Crie um programa que peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo. Em seguida, o programa deve calcular e mostrar o comprimento da hipotenusa.

import math


cateto1 = int(input("digite o comprimento do primeiro cateto: "))
cateto2 = int(input("digite o comprimento do segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"O valor da hipotenusa é igual a {hipotenusa}.")