class BankAccount():
    def __init__(self,nome,numero,saldo = 0):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.cliente = {"nome": self.nome, "numero": self.numero, "saldo": self.saldo}
        self.clientes = []
    
    def cadastrar_conta(self,tipo):
        if tipo == "corrente":
            self.cliente["tipo"] = tipo
            self.clientes.append(self.cliente)

    
    def deposito(self,valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso!")
            return self.saldo
        else:
            print("Erro ao depositar!")
            return self.saldo
    
    def saque(self,valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado!")
            return self.saldo
        else:
            print("Erro")
            return self.saldo
    
    def saldo_atual(self):
        print("Saldo atual: ",self.saldo)

    def imprimir(self):
        for cliente in self.clientes:
            print(cliente)

cliente = BankAccount("james","345-6",450.90)
cliente2 = BankAccount("João","035-7",300.00)
cliente.deposito(250.00)

cliente.saldo_atual()

cliente.saque(-300.00)

cliente.saldo_atual()

cliente.cadastrar_conta("corrente")
cliente2.cadastrar_conta("corrente")
cliente.imprimir()
cliente2.imprimir()