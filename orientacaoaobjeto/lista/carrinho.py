class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []
    
    def adicionarProdutos(self,produto):
        self.produtos.append(produto)
        print("Produto adicionado com sucesso.... :)")
    
    def calcular(self):
        total = 0.0
        for carrinho in self.produtos:
            total += carrinho['quantidade'] * carrinho['preco']
        
        print(total)

    def listarCarrinho(self):
        
        for carrinho in self.produtos:
            print("Nome: ",carrinho['nome'])
            print("Preço: ",carrinho['preco'])
            print("Quantidade: ",carrinho['quantidade'])

    def bucarProduto(self,nome):
        for produto in self.produtos:
            if nome == produto['nome']:
                print("Nome: ",produto['nome'])
                print("Preço: ",produto['preco'])
                print("Quantidade comprada: ",produto['quantidade'])

        else:
            print("Produto não comprado... :(")            




