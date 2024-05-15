# Implemente uma calculadora que realize operações de soma, subtração, multiplicação e divisão. Utilize tratamento de exceções para lidar com operações inválidas.

def calcular(numero1, numero2, operacao): 
    try: 
        if operacao== "+": 
            return numero1 + numero2 
        elif operacao== "-": 
            return numero1 - numero2 
        elif operacao== "*":
            return numero1 * numero2 
        elif operacao== "/": 
            return numero1 / numero2 
        else: 
            raise ValueError("Operação inválida.") 
    except ZeroDivisionError: 
        print("Não é possível dividir por zero.") 
    except TypeError: 
        print("Não foram digitados apenos números.") 
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
simbolo = input("Digite o símbolo da operação desejada: ")

print(calcular(numero1, numero2, simbolo))