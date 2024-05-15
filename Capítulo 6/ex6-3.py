# Faça um programa que use List Comprehension para criar uma lista com o quadrado dos números pares entre 0 e 10.

quadrados = [x**2 for x in range(11) if x % 2 == 0] 
 
print(quadrados)