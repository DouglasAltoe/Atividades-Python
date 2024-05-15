# Crie uma classe chamada ContaBancaria com o atributo saldo e com métodos para depositar, sacar e exibir o saldo da conta. Crie uma instância da classe ContaBancaria e teste os métodos criados.

class ContaBancaria: 
    def __init__(self): 
        self.saldo = 0 
 
    def depositar(self, valor): 
        self.saldo += valor 
 
    def sacar(self, valor): 
        self.saldo -= valor
 
    def exibir(self): 
        print(f"Saldo: {self.saldo}") 
 
conta = ContaBancaria() 

conta.depositar(1000) 
conta.exibir() 
conta.sacar(500) 
conta.exibir()