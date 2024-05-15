# Crie um programa que peça ao usuário para digitar três números, armazenando-os em variáveis distintas. Em seguida, imprima a média aritmética dos três números. 

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

media = (numero1 + numero2 + numero3) / 3

print(f"A média dos três números é igual a {media}")