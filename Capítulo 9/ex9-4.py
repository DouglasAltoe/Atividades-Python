# Crie uma classe chamada ContaBancaria com os métodos depositar e sacar. Utilize tratamento de exceções para lidar com saques maiores que o saldo disponível, criando uma exceção personalizada.

class SaldoInsuficienteError(Exception): 
    def __init__(self): 
        super().__init__("Saldo insuficiente para realizar o saque.") 
 
class ContaBancaria: 
    def __init__(self, saldo_inicial): 
        self.saldo = saldo_inicial 
 
    def depositar(self, valor): 
        self.saldo += valor 
 
    def sacar(self, valor):
        if valor > self.saldo: 
            raise SaldoInsuficienteError() 
        self.saldo -= valor 
 
conta = ContaBancaria(100) 
try: 
    conta.sacar(50) 
    print(conta.saldo)
    conta.sacar(100) 
except SaldoInsuficienteError as e: 
    print(e)