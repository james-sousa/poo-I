class Funcionario():
    def __init__(self,nome,cpf,cargo,senha):
        self._nome = nome
        self._cpf = cpf
        self._cargo = cargo
        self._senha = senha
        
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf
    
    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self,cargo):
        self._cargo = cargo
    
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha = senha
    
    


class Cadastrar_funcionario():
    def __init__(self):
        
        self._funcionario = {}
    
    @property
    def funcionario(self):
        return self._funcionario
    
    @funcionario.setter
    def funcionario(self,func):
        self._funcionario[func.cpf] = func
    
    def existe_gerente_cadastrado(self):
        for func in self._funcionario.values():
            if func.cargo == "GERENTE":
                return True
        return False
    
    def cadastrar_funcionario(self,nome,cpf,cargo,senha):
        
        if cpf in self._funcionario.keys():
            print("Funcionario já cadastrado!")
            return self._funcionario
        
        else:
            if cargo == "GERENTE" and self.existe_gerente_cadastrado():
                print("Já existe um gerente cadastrado!")
                return self._funcionario
             
            self._funcionario[cpf] = Funcionario(nome,cpf,cargo,senha)
            print("Funcionario cadastrado com sucesso!")
            
            return self._funcionario

    def listar_funcionarios(self):
        if(len(self._funcionario) > 0):
            for _,funcionario in self._funcionario.items():
                print()
                print("Nome: ",funcionario.nome)
                print("Cpf: ",funcionario.cpf)
                print("Cargo: ",funcionario.cargo)
                print()
                
        else:
            print("Nenhum funcionario cadastrado!")

        