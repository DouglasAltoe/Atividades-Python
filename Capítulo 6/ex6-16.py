# Faça um programa que declare uma lista de 10 números inteiros e inverta a ordem dos elementos de índices pares. Ao fim, mostre a lista resultante.

numeros = list(map(int, input("Digite um conjunto de números com espaços entre eles: ").split(" "))) 
 
indices_pares = [numeros[i] for i in range(0, len(numeros), 2)] 
 
indices_pares.reverse() 
 
for i in range(0, len(numeros), 2): 
    numeros[i] = indices_pares.pop(0) 
 
print(numeros)