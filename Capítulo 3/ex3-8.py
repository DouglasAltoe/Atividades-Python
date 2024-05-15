# Crie um programa que calcule e mostre o fatorial de um número digitado pelo usuário.

numero = int(input("Digite um número: ")) 
fatorial = 1 
i = 1

while i <= numero:
    fatorial *= i
    i += 1

print(f"O fatorial de {numero} é igual a {fatorial}.")