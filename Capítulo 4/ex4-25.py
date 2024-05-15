# Faça um programa que adicione 30 dias à data atual utilizando timedelta.

from datetime import datetime, timedelta 
 
data = datetime.now()
data_nova = data + timedelta(days=30) 
 
print(f"A data de hoje é: {data}") 
print(f"A data daqui a 30 dias será: {data_nova}")