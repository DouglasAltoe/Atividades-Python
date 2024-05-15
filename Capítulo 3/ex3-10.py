# Crie um programa que calcule e mostre todos os números primos de 1 a 100.

for numero in range(1, 101): 
    if numero > 1:
        for i in range(2, numero): 
            if (numero % i) == 0:
                break 
        else:
            print(numero, end=", ")