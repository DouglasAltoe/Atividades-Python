# Crie um arquivo vazio qualquer. Agora, na mesma pasta, crie um programa que solicite ao usuário que digite o nome desse arquivo e exclua-o.

import os 

nome = input("Digite o nome do arquivo: ") 

os.remove(nome)