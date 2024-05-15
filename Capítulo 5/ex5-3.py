# Crie uma função que tenha 3 parâmetros: um número inteiro, um número real e um texto. A função deve imprimir os valores dos parâmetros na tela. Em seguida, chame a função passando os argumentos de forma posicional.

def imprime_valores(inteiro, real, texto): 
    print(inteiro, real, texto)

numero_inteiro = int(input("Digite um número: "))
numero_real = float(input("Digite um número real: "))
texto = input("Digite um texto: ")

imprime_valores(numero_inteiro, numero_real, texto)