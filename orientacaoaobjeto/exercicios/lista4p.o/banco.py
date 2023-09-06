from cliente import Cliente



class Banco:
    
    def __init__(self):
        self._clientes = {}
        self._tributos = []
    
   
    @property
    def clientes(self):
        return self._clientes
    @clientes.setter
    def clientes(self, client):
        self._clientes[client.cpf] = client
    
    def quantidade_de_contas(self):
        quant = 0
        for _, cliente in self._clientes.items():
            if(cliente._contas["corrente"] != ""):
                quant += 1
            if(cliente._contas["poupanca"] != ""):
                quant += 1 
        
        return quant
    
  
        
    def cadastrar_cliente(self, nome, cpf):
        if not(cpf in self.clientes.keys()):
            self.clientes = Cliente(nome, cpf)
            return True, "| << Cliente cadastrado com sucesso!"
        return False, "| << O(a) cliente com esse cpf já está cadastrado(a)!"
    
    def existe_conta(self, numero):
        for _, cliente in self.clientes.items():
            try:
                if cliente._contas["corrente"]._numero.strip() == numero.strip():
                    return True  
            except: pass
            try:
                if cliente._contas["poupanca"]._numero.strip() == numero.strip():
                    return True
            except: pass
        return False
        
    def criar_conta_corrente(self, cpf, num):
        try:
            temp = int(num)
        except:
            return False, "| << Insira um valor numérico!"

        if self.existe_conta(num):
            return False, "| << Esse número não está disponível"   
    
        if (cpf in self.clientes.keys()):
            return self._clientes[cpf].add_conta(1, num)

        return False, "| << CPF incorreto ou o usuário não está cadastrado!"

    def criar_conta_poupanca(self, cpf, num):
        try:
            temp = int(num)
        except:
            return False, "| << Insira um valor numérico!"
        
        if self.existe_conta(num):
            return False, "| << Esse número não está disponível" 
        if (cpf in self.clientes.keys()):
            return self._clientes[cpf].add_conta(2, num)

        return False, "| << CPF incorreto ou o usuário não está cadastrado!"
    def criar_seguro(self, cpf, mensal, total):
        if (cpf in self.clientes.keys()):
            return self._clientes[cpf].add_seguro(mensal, total), "| << Seguro criado com sucesso!"

        return False, "| << CPF incorreto ou o usuário não está cadastrado!"
    
    def calc_tributos(self):
        if(self.clientes):
            tributo_atual = 0
            for _, cliente in self.clientes.items():
                tributo_atual += cliente.tributacao()[1]
            self._tributos.append(tributo_atual)
            tabela = "-" * 10 + "\n"
            tabela += f"|{'Tributos'.center(13, ' ')}|\n"
            tabela += "-" * 10 + "\n"
            tabela = "-" * 10 + "\n"
            tabela += f"|{'Nº':<3}|{'Valor':<10}|\n"
            tabela += "-" * 10 + "\n"
            for indice, valor in enumerate(self._tributos):
                valor = f"R${valor:.2f}".replace(".",",")
                tabela += f"|{indice+1:<3}|{valor:<10}|\n"
                tabela += "-" * 10 + "\n"
                
            return True, tabela
        return False, f"| << Nenhum cliente cadastrado."
                
    def deposito(self, cpf, num, valor):
        if (cpf in self.clientes.keys()):
            return self._clientes[cpf].deposito(num, valor)
        return False, f"| << O cliente de cpf {cpf} não encontrado."
    def saque(self, cpf, num, valor):
        if (cpf in self.clientes.keys()):
            return self._clientes[cpf].saque(num, valor)
        return False, f"| << O cliente de cpf {cpf} não encontrado."
    
    def consulta_contas(self, cpf):
        if (cpf in self._clientes.keys()):
            numeros = []
            quantidade = 0
            if (self._clientes[cpf]._contas["corrente"] != ""):
                numeros.append(f"Conta corrente, numero: {self.clientes[cpf]._contas['corrente']._numero}")
                quantidade += 1
            if (self._clientes[cpf]._contas["poupanca"] != ""):
                numeros.append(f"Conta poupanca, numero: {self.clientes[cpf]._contas['poupanca']._numero}")
                quantidade += 1
            return quantidade, numeros
        return False, "| << Usuario não cadastrado"
    
    def transferir(self, cpf1, num1, cpf2, num2, valor):
        if num1 == num2 and cpf1 == cpf2:
            return False, "| << Não é possível fazer uma transferência para si mesmo!"
        if( self.quantidade_de_contas() > 1):
            retirada = self.saque(cpf1, num1, valor)
            if(retirada[0]):
                envio = self.deposito(cpf2, num2, valor)
                if not(envio[0]):
                    self.deposito(cpf1, num1, valor)
                    return False, "| << Não foi possivel enviar para conta de destino\n| << O valor foi estornado para conta de origem!"
                return envio[0], "| << Transferência realizada com sucessoe!"
            return retirada
        return False, "| << Só existe uma conta nesse banco!"
    
    def extrato(self, cpf, num_conta):
        if (cpf in self._clientes.keys()):
            return self._clientes[cpf].extrato(num_conta)
        return False, "| << Usuário não encontrado!"
    
    def mostrar_tudo(self):
        tabela = ""
        tabela += "-" * 45 + "\n"
        tabela += "|"+f"Total de Contas: {self.quantidade_de_contas()}".center(20," ")+"|\n"
        tabela += "-" * 30 + "\n"
        if(len(self.clientes) > 0):
            tabela += f"|{'nome':<25}|{'Conta Corrente':<20}|{'Conta Poupanca':<20}|{'Seguro de Vida(Qtd.)':<20}|\n"
            tabela += "-" * 30 + "\n"
            for _, cliente in self.clientes.items():
                tabela += f"|{cliente.nome:<25}|{'Possui' if cliente._contas['corrente'] != '' else 'Não Possui':<20}|{'Possui' if cliente._contas['poupanca'] != '' else 'Não Possui':<20}|{str(len(cliente._seguros)).center(20, ' ')}|\n"
                tabela += "-" * 30 + "\n"
        return True, tabela
            
    def lista_clientes(self):
        tabela = ""
        if(len(self.clientes) > 0):
            tabela += "-" * 20+ "\n"
            tabela += f"|{'CPF':<13}|{'Nome':<15}|{'nascimento':<12}|{'Profissão':>14}|\n"
            tabela += "-" * 20+ "\n"
            for _, clientes in self.clientes.items():
                infos = clientes.informacoes()
                tabela += f"|{infos[0]:<13}|{infos[1]:<15}|{infos[2]:<12}|{infos[3]:>14}|\n"
                tabela += f"{'-' * 20}\n"
            return True, tabela

        return False, "| << Nenhum cliente cadastrado!"