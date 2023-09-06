class Mercado():
    def __init__(self):
        self.produtos = []
    
    def cadastrar(self,produto):
        self.produtos.append(produto)
        print("Produto Cadastrado com sucesso!")
        return self.produtos
    
    def listar_produtos(self):
        for produto in self.produtos:
            print("Nome: ",produto["nome"])
            print("Quantidade: ",produto["quantidade"])
            print("Preço: ",produto["preco"])
    

class Carrinho(Mercado):
    def __init__(self):
        super().__init__()
        self.carrinho = []
    
    def adicionar_carrinho(self,nome):
        #produto_encontrado = False
        for carrinho in self.produtos:
            if nome == carrinho["nome"] and carrinho["quantidade"] > 0:
                quantidade = int(input("Digite a quantidade que deseja: "))
                if carrinho["quantidade"] >= quantidade:
                    preco = carrinho["preco"] * quantidade
                    print("O preço da compra eh: ",preco)
                    pagamento = float(input("pagamento: "))
                    if pagamento == preco:
                        carrinho["quantidade"] -= quantidade
                        print("Compra realizada: ")
                        compra = {"nome": nome,"quantidade": quantidade}
                        self.carrinho.append(compra)
                        #produto_encontrado = True
                        break
                    else:
                        print("Valor insuficiente!")
                        return self.produtos
                else:
                    print("Quantidade em estoque insuficiente!")
                    return self.produtos
        else:#if not produto_encontrado:
            print("Produto não encontrado!")
        return self.carrinho,self.produtos
    
    def imprimir_carrinho(self):
        for produto in self.carrinho:
            print("Nome: ",produto["nome"])
            print("Quantidade: ",produto["quantidade"])
                    
