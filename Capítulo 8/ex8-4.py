# Crie uma classe chamada Carro com o atributo velocidade e com métodos para acelerar e frear o carro por X segundos, sendo que o carro acelera a 10m/s2 e freia a 5m/s2. Crie uma instância da classe Carro e teste os métodos criados.

class Carro: 
    def __init__(self): 
        self.velocidade = 0 
 
    def acelerar(self, segundos): 
        aceleracao = 10
        self.velocidade += aceleracao * segundos 
 
    def frear(self, segundos): 
        frenagem = 5
        self.velocidade -= frenagem * segundos

carro = Carro() 
 
carro.acelerar(10) 
print(f"Velocidade: {carro.velocidade}") 
carro.frear(1) 
print(f"Velocidade: {carro.velocidade}")