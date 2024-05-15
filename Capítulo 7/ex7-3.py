# Crie um programa que leia um arquivo texto, inverta o conteúdo de cada linha e salve o resultado em um novo arquivo.

nome = input("Digite o nome do arquivo: ") 
with open(nome, "r", encoding="utf-8") as arquivo: 
    linhas = arquivo.readlines() 
 
inverso = [linha[::-1] for linha in linhas] 
 
with open("arquivo_invertido.txt", "w", encoding="utf-8") as arquivo: 
    arquivo.writelines(inverso)