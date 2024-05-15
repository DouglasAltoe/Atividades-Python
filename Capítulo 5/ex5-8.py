#Você é um investigador e precisa decifrar uma mensagem secreta escondida em um texto. Cada letra da mensagem foi substituída pela letra do alfabeto que vem imediatamente depois dela. Por exemplo, "a" foi substituída por "b", "b" foi substituída por "c", e assim por diante. A letra "z" foi substituída por "a". Escreva uma função recursiva chamada decifrar_mensagem que aceite a mensagem codificada como uma string e retorne a mensagem decodificada. A regra é que a função deve ser recursiva!

def decifrar_mensagem(mensagem):
    if len(mensagem) == 0: 
        return mensagem 
    else:
        letra = chr((ord(mensagem[0]) - 98) % 26 + 97) 
        return letra + decifrar_mensagem(mensagem[1:]) 

texto = input("Escreva um texto codificado: ")

print(decifrar_mensagem(texto))