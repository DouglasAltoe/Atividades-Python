# Crie um programa que peça ao usuário para digitar 5 números inteiros. O programa deve exibir uma mensagem informando se todos os números digitados são pares ou se há pelo menos um número ímpar.

numero1 = int(input("Digite o primeiro número: ")) 
numero2 = int(input("Digite o segundo número: ")) 
numero3 = int(input("Digite o terceiro número: ")) 
numero4 = int(input("Digite o quarto número: ")) 
numero5 = int(input("Digite o quinto número: ")) 
 
if numero1 % 2 == 0 and numero2 % 2 == 0 and numero3 % 2 == 0 and numero4 % 2 == 0 and numero5 % 2 == 0: 
    print("Todos os números são pares.") 
else: 
    print("Há pelo menos um número ímpar.")