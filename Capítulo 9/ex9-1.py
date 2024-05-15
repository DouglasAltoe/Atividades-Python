# Crie um programa que solicite ao usuário dois números inteiros e exiba a divisão do primeiro número pelo segundo. Trate possíveis exceções de divisão por zero.

try: 
    numero1 = int(input("Digite o primeiro número: ")) 
    numero2 = int(input("Digite o segundo número: ")) 
    print(f"Resultado: {numero1 / numero2}") 
except ZeroDivisionError: 
    print("Não é possível dividir por zero.") 