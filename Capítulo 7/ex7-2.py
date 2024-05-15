# Crie um programa que leia um arquivo texto e exiba quantas linhas ele possui.

nome = input("Digite o nome do arquivo: ") 
with open(nome, "r", encoding="utf-8") as arquivo: 
    linhas = arquivo.readlines() 
print(len(f"O arquivo tem {linhas} linhas."))