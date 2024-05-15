# :: Crie um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero.

numero = int(input("Digite um número: "))

if numero < 0:
    print(f"O número {numero} é negativo.")
elif numero > 0:
    print(f"O número {numero} é positivo.")
else:
    print(f"O número {numero} é igual a zero.")