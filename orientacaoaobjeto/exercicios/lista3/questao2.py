class Agenda:
    def __init__(self):
        self.pessoas = []
    
    def armazenaPessoas(self,pessoa):
        if len(self.pessoas) < 10:
            self.pessoas.append(pessoa)
            print("Adicionado!")
        else:
            print("Armazenamneto cheio!")
    
    def removePessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa['nome'] == nome:
                self.pessoas.remove(pessoa)
                print("Removido!")
                return self.pessoas
        else:
            print("Pessoa não cadastrada!")
    
    def busca(self,nome):
        for pessoa in self.pessoas:
            if pessoa['nome'] == nome:
                print("Dados da pessoa:")
                print("Nome: ",pessoa['nome'])
                print(f"Idade: ",pessoa['idade'])
                print(f"Altura: ",pessoa['altura'])
                return self.pessoas
            else:
                print("Não encontrada!")
    
    def imprimir(self):
        for pessoa in self.pessoas:
            print("Nome: ",pessoa['nome'])
            print("Idade: ",pessoa['idade'])
            print("Altura: ",pessoa['altura'])

agenda = Agenda()

agenda.armazenaPessoas({"nome": "João", "idade": 25, "altura": 1.75})
agenda.armazenaPessoas({"nome": "Maria", "idade": 30, "altura": 1.65})
agenda.armazenaPessoas({"nome": "Pedro", "idade": 40, "altura": 1.80})

# Removendo uma pessoa
agenda.removePessoa("Maria")

# Buscando uma pessoa
agenda.busca("João")

# Imprimindo a agenda
agenda.imprimir()