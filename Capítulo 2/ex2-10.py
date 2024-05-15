# Crie um programa que verifique se uma temperatura corporal digitada pelo usuário está acima, abaixo ou dentro da faixa normal (36°C a 37°C).

temperatura = float(input("Digite a sua temperatura: ")) 
 
if temperatura < 36: 
    print("A sua temperatura está abaixo do normal.") 
elif temperatura > 37: 
    print("A sua temperatura está acima do normal.") 
else: 
    print("A sua temperatura está normal.")