# Crie um programa que solicite ao usuário um nome de arquivo e exiba seu conteúdo na tela.

nome = input("Digite o nome do arquivo: ") 
with open(nome, "r", encoding="utf-8") as arquivo: 
    conteudo = arquivo.read() 
print(conteudo)