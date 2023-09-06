from contas import *
from tributos import Tributavel
Tributavel.register(ContaCorrente)
class Cliente():
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._contas = {"corrente": "", "poupanca": ""}
        self._seguros = []
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
        
        
    def add_conta(self, tipo, num):
        if tipo == 1:
            if(self._contas['corrente'] == ''):
                self._contas['corrente'] = ContaCorrente(num, 0)
                return True, "| << Conta corrente criada com sucesso!"
            return False, "| << Número máximo de contas correntes já atingido!"
        
        if tipo == 2:
            if(self._contas['poupanca'] == ''):
                self._contas['poupanca'] = ContaPoupanca(num, 0)
                return True, "| << Conta poupanca criada com sucesso!"
            return False, "| << Número máximo de contas poupancas já atingido!"
            
    def add_seguro(self, mensal, total):
        try:
            mensal = float(mensal)
            total = float(total)
        except:
            return False, "| << Insira valores numéricos!"
        self._seguros.append(SeguroDeVida(mensal, total))
        return True, "| << Seguro de vida criado com sucesso!"
        
    def informacoes(self):
        return self._cpf, self._nome
    
    def deposito(self, num_conta, valor):
        if self._contas["corrente"] != "":
            if (num_conta == self._contas["corrente"]._numero):
                return self._contas["corrente"].receber(valor)
        if self._contas["poupanca"] != "":
            if(num_conta == self._contas["poupanca"]._numero):
                return self._contas["poupanca"].receber(valor)
        return False, "| << Conta não encontrada ou não criada"
        
    def saque(self, num_conta, valor):
        if self._contas["corrente"] != "":
            if (num_conta == self._contas["corrente"]._numero):
                return self._contas["corrente"].retirar(valor)
        if self._contas["poupanca"] != "":
            if(num_conta == self._contas["poupanca"]._numero):
                return self._contas["poupanca"].retirar(valor)
        return False, "| << Conta não encontrada ou não criada"
    def extrato(self, num_conta):
        if self._contas["corrente"] != "":
            if (num_conta == self._contas["corrente"]._numero):
                return self._contas["corrente"].extrato()
        if self._contas["poupanca"] != "":
            if(num_conta == self._contas["poupanca"]._numero):
                return self._contas["poupanca"].extrato()
        return False, "| << Conta não encontrada ou não criada"

    def tributacao(self):
        tributos = []
        if isinstance( self._contas["corrente"], Tributavel):
            desconto = self._contas["corrente"].tributo()
            tributos.append(desconto)
            self._contas["corrente"].retirar(desconto, True)
            self._contas["corrente"].retirar(10, True)
        for indice, seguro in enumerate(self._seguros):
            desconto = seguro.tributo()
            tributos.append(desconto)
            self._seguros[indice].retirar(desconto)
        total = 10 + sum(tributos)
        return  True, total
