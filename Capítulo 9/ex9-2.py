# Crie uma função que receba uma lista de números e retorne a média aritmética deles. Trate exceções caso a lista seja vazia ou contenha valores não numéricos.

def media(lista): 
    try: 
        return sum(lista) / len(lista) 
    except ZeroDivisionError: 
        print("Não é possível dividir por zero.") 
    except TypeError: 
        print("Não foram digitados apenos números.") 
 
lista = list(map(int, input("Digite um conjunto de números com espaços entre eles: ").split(" "))) 

print(media(lista))