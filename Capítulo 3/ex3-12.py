# Crie um programa que calcule e mostre a soma de todos os números primos de 1 a 100.

soma = 0

for numero in range(1, 101): 
    if numero > 1:
        for i in range(2, numero): 
            if (numero % i) == 0:
                break 
        else:
            soma += numero

print(f"A soma dos números primos de 1 a 100 é igual a {soma}.")