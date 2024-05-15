# Crie um programa que peça ao usuário para digitar a massa e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a força resultante.

massa = float(input("Digite a massa do objeto: "))
aceleracao = float(input("Digite a aceleração do objeto: "))

forca = massa * aceleracao

print(f"A força do objeto é igual a {forca} N.")