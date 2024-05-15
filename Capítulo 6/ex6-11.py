# Faça um programa que peça ao usuário para digitar uma lista de números e que, em seguida, use filtragem (filter) para retornar uma nova lista apenas com os números pares.

numeros = list(map(int, input("Digite um conjunto de números com espaços entre eles: ").split(" "))) 

pares = list(filter(lambda x: x % 2 == 0, numeros)) 

print(pares)