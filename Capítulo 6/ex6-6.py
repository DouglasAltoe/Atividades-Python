# Faça um programa que use Dict Comprehension para criar um dicionário com as raízes quadradas dos números de 1 a 10. Utilize os números como chave e as raízes quadradas como valor.

import math


raizes = {n: math.sqrt(n) for n in range(1, 11)}

print(raizes)