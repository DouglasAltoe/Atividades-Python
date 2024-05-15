# Crie um programa que peça ao usuário para inserir um número e calcule o fatorial desse número.

import math 
 
numero = int(input("Digite um número: ")) 
fatorial = math.factorial(numero) 

print(f"O fatorial de {numero} é igual a {fatorial}.")