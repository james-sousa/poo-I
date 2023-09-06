from funcionario import Cadastrar_funcionario
from autenticacao import Autenticavel
login_funcionario = Cadastrar_funcionario()

class Login(Autenticavel):
    def __init__(self,login_funcionario):
        self.login_funcionario = login_funcionario
    
    def autenticacao(self,cpf,senha):
        funcionario = self.login_funcionario.funcionario.get(cpf)

        if funcionario and funcionario.cpf == cpf and funcionario.senha == senha:
            
            return True, funcionario.cargo
        else:
            print("Falha no login!")
            return False