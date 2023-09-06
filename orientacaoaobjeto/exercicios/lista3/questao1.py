import datetime

class Pessoa():
    
    def __init__(self,nome,data_nascimento,altura):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._altura = altura
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    @data_nascimento.setter
    def data_nascimento(self,data_nascimento):
        self._data_nascimento = data_nascimento
    
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self,altura):
        if altura < 0.0:
            print("Altura invalida!")
        else:
            self._altura = altura

    def calcular_idade(self):
        data_atual = datetime.date.today()
        idade = data_atual.year - self._data_nascimento.year
        if data_atual.month < self._data_nascimento.month or (data_atual.month == self._data_nascimento.month and data_atual.day < self._data_nascimento.day):
            idade -= 1
            
        else:
            
            return idade
        return idade

    def imprimir(self):
        idade = self.calcular_idade()
        print("---------------Dados----------------")
        print("Nome: ",self._nome)
        print(f"Nascimento: {self._data_nascimento.day}-{self._data_nascimento.month}-{self._data_nascimento.year}")
        print("Altura: ",self._altura)
        print(f"Idade: {idade}")

pessoa1 = Pessoa("João",datetime.date(1999, 1, 12),1.78)
pessoa1.imprimir()
pessoa1.calcular_idade()
pessoa2 = Pessoa("James",datetime.date(2002, 10, 5), 1.70)

pessoa2.calcular_idade()
pessoa2.imprimir()


