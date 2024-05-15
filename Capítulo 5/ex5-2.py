# Crie uma função que tenha um número inteiro como parâmetro e retorne True se o número for par e False se o número for ímpar. Em seguida, crie uma chamada para essa função passando argumentos para os parâmetros e mostrando o resultado na tela.

def verifica_par(numero): 
    return numero % 2 == 0 
 
valor = int(input("Digite um número: "))

resultado = verifica_par(valor) 
print(f"{valor} é par? R:{resultado}.")