# Crie uma função que leia um arquivo de texto e exiba o conteúdo na tela. Trate exceções caso o arquivo não exista ou não seja possível lê-lo.

def ler_arquivo(nome): 
    try: 
        with open(nome, 'r') as arquivo: 
            print(arquivo.read()) 
    except FileNotFoundError: 
        print("Arquivo não encontrado.") 
    except IOError: 
        print("Não foi possível ler o arquivo.") 

nome = input("Digite o nome do arquivo: ") 

ler_arquivo(nome)