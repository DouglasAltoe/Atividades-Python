# Crie uma função que tenha dois parâmetros: nome e idade. A função deve imprimir na tela uma mensagem a seu gosto contendo o nome e a idade da pessoa. Em seguida, crie uma chamada para essa função passando argumentos de forma nomeada.

def imprime_nome_idade(nome, idade): 
    print(f"Seu nome é {nome} e sua idade é {idade}.") 

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

imprime_nome_idade(nome, idade)