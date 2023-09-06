class Estoque():
    def __init__(self):
        self.estoque = []
    
    def cadastro(self,produto):
        self.estoque.append(produto)
        print("Produto cadastrado!")
        return self.estoque
    
    def atualizar(self,nome_produto):
        for produto in self.estoque:
            if nome_produto == produto["nome"]:
                nova_qt = int(input("Nova quantidade: "))
                produto["quantidade"] = nova_qt
                print("Atualizado!")
                return self.estoque
        else:
            print("Produto não encontrado!")
            return self.estoque
    
    def listar_produtos(self):
        for produto in self.estoque:
            print("Nome: ",produto["nome"])
            print("Quantidade: ",produto["quantidade"])
            print("Preço: ",produto["preco"])
    
    def remover(self,nome_produto):
        for produto in self.estoque:
            if nome_produto == produto["nome"]:
                self.estoque.remove(produto)
                print("Produto removido!")
                return self.estoque
        else:
            print("Produto não encontrado")
            return self.estoque

nome = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))

produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
produtos = Estoque()

produtos.cadastro(produto)
produtos.listar_produtos()
nome_produto = input("Digite o nome: ")
produtos.atualizar(nome_produto)
produtos.listar_produtos()

nome = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))
produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
produtos.cadastro(produto)
produtos.listar_produtos()
nome_produto = input("Digite o nome: ")
produtos.atualizar(nome_produto)
produtos.listar_produtos()
nome_produto = input("Digite o nome: ")
produtos.remover(nome_produto)
produtos.listar_produtos()