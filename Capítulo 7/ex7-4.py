# Crie um programa que solicite ao usuário o nome de um arquivo e que renomeie esse arquivo adicionando a palavra "renomeado" ao nome existente, mantendo sua extensão.

import os 

arquivo = input("Digite o nome do arquivo: ") 
nome = os.path.splitext(arquivo)[0] 
extensao = os.path.splitext(arquivo)[1] 

os.rename(arquivo, f"{nome}_renomeado{extensao}")