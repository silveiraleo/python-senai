class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}'

class ContaBancaria:
    def __init__(self, numero_conta, saldo, titular):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para o saque.')
        else:
            print('O valor do saque deve ser positivo.')

    def consultar_saldo(self):
        return f'Saldo atual: R$ {self.saldo:.2f}'

    def informacoes_titular(self):
        print(f'Informações do Titular: {self.titular}')

# Exemplo de uso

cliente1 = Cliente(nome='Leonardo da Silveira', cpf='123.456.789-00')
conta1 = ContaBancaria(numero_conta='0001', saldo=1000.00, titular=cliente1)

print(conta1.consultar_saldo())  
conta1.depositar(500.00)         
conta1.sacar(200.00)            
print(conta1.consultar_saldo())  
conta1.informacoes_titular()
