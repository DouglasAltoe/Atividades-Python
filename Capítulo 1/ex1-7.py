# Crie um programa que peça ao usuário para digitar um número inteiro. Em seguida, o programa deve calcular e mostrar o valor dos inteiros anterior e posterior a esse número.

numero = int(input("Digite um número: "))
anterior = numero - 1
posterior = numero + 1

print(f"Número anterior a {numero}: {anterior}.")
print(f"Número posterior a {numero}: {posterior}.")