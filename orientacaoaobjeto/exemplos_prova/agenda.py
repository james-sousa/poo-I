class Agenda():
    def __init__(self):
        self.contatos_book = []
    
    def adicionar(self,contato):
        self.contatos_book.append(contato)
        print("Contato adicionado!")
    
    def listar(self):
        for contato in self.contatos_book:
            print("Nome: ",contato["nome"])
            print("Email: ",contato["email"])
            print("Telefone: ",contato["telefone"])
    
    def remover(self,nome):
        for contato_nome in self.contatos_book:
            if nome == contato_nome["nome"]:
                self.contatos_book.remove(contato_nome)
                print("Removido!")
                return self.contatos_book
        else:
            print("Contato não encontrado!")
    
    def busca(self,nome):
        for contato_busca in self.contatos_book:
            if nome == contato_busca["nome"]:
                print("Nome: ",contato_busca["nome"])
                print("Email: ",contato_busca["email"])
                print("Telefone: ",contato_busca["telefone"])
                return self.contatos_book
        else:
            print("Contato não cadastrado!")