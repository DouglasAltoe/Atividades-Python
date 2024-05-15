# Faça um programa que mostre a data atual no formato "DD-MM-AAAA".

import datetime 
 
data_atual = datetime.date.today()
data_formatada = data_atual.strftime("%d-%m-%Y") 

print(f"A data de hoje é {data_formatada}.")