class Produto():
    def __init__(self,marca,modelo,tamanho,preco,quantidade):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        
        self.preco = preco
        self.quantidade = quantidade

    

class Controle_estoque():
    def __init__(self):
        
        self._produto_cadastro = {}

    
    @property
    def produto(self):
        return self._produto_cadastro
    @produto.setter
    def produto(self,produt):
        chave = (produt.marca, produt.modelo, produt.tamanho)
        self._produto_cadastro[chave] = produt
    
    def cadastrar_produto(self,marca,modelo,tamanho,preco,quantidade):
        chave = (marca,modelo,tamanho)
        if chave in self._produto_cadastro.keys():
            print("Produto já cadastrado!")
            return False, self._produto_cadastro
            
        else:
            self._produto_cadastro[chave] = Produto(marca,modelo,tamanho,preco,quantidade)
            print("Produto Cadastrado com sucesso!")
            
            return True, self._produto_cadastro

    def reposicao_estoque(self,marca,modelo,tamanho):
        chave = (marca, modelo, tamanho)
        produto_dados = self._produto_cadastro.get(chave)
        if produto_dados:
            try:
                quantidade = int(input("Digite a quantidade a ser reposta no estoque: "))
                if quantidade <= 0:
                    print("Dgite um valor positivo!")
                    return self._produto_cadastro
                produto_dados.quantidade += quantidade
                print("Reposição realizada com sucesso!")
                return True, quantidade #self._produto_cadastro
            except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número válido.")
                    return False, self._produto_cadastro
        else:
                print("Produto não encontrado!")
                return False, self._produto_cadastro

    
    def listar_produtos(self):
        for produto_marca, produto_dados in self._produto_cadastro.items():
            print("Marca: ",produto_dados.marca)
            print("Modelo: ",produto_dados.modelo)
            print("Tamanho: ",produto_dados.tamanho)
            print("Preço: ",produto_dados.preco)
            print("Quantidade em estoque: ",produto_dados.quantidade)
            print()
    
    def remover_produto(self, marca, modelo, tamanho):
        chave = (marca, modelo, tamanho)
        if chave in self._produto_cadastro:
            del self._produto_cadastro[chave]
            print("Produto removido com sucesso!")
            return True
        else:
            print("Produto não encontrado!")
            return False


    def niveis_de_estoque(self):
        print("1-Nivel Excelente - Até 50 unidades \n2-Nivel Bom - Até 20 unidades\n3-Nivel Baixo - Até 10 unidades\n4-Nivel Critico - Até 5 unidades")
        opcao_estoque = int(input("Digite sua opção: "))
        if opcao_estoque == 1:
            nivel_estoque = 50
            
            for produto_, produto_dados in self._produto_cadastro.items():
                if produto_dados.quantidade <= nivel_estoque and produto_dados.quantidade > 20:
                    print("Produtos da marca ", produto_dados.marca)
                    print("Modelo: ",produto_dados.modelo)
                    print("Tamanho: ",produto_dados.tamanho)
                    print("Preço: ",produto_dados.preco)
                    print("Quantidade em estoque: ",produto_dados.quantidade)
                    print()
                    return self._produto_cadastro
                else:
                    print("Não encontrado nenhum produto nesse nivel!")
                    return self._produto_cadastro
        elif opcao_estoque == 2:
            nivel_estoque = 20
            
            for produto_, produto_dados in self._produto_cadastro.items():
                if produto_dados.quantidade <= nivel_estoque and produto_dados.quantidade > 10:
                    print("Produtos da marca ", produto_dados.marca)
                    print("Modelo: ",produto_dados.modelo)
                    print("Tamanho: ",produto_dados.tamanho)
                    print("Preço: ",produto_dados.preco)
                    print("Quantidade em estoque: ",produto_dados.quantidade)
                    print()
                    return self._produto_cadastro
                else:
                    print("Não encontrado nenhum produto nesse nivel!")
                    return self._produto_cadastro
        elif opcao_estoque == 3:
            nivel_estoque = 10
            
            for produto_, produto_dados in self._produto_cadastro.items():
                if produto_dados.quantidade <= nivel_estoque and produto_dados.quantidade > 5:
                    print("Produtos da marca ", produto_dados.marca)
                    print("Modelo: ",produto_dados.modelo)
                    print("Tamanho: ",produto_dados.tamanho)
                    print("Preço: ",produto_dados.preco)
                    print("Quantidade em estoque: ",produto_dados.quantidade)
                    print()
                    return self._produto_cadastro
                else:
                    print("Não encontrado nenhum produto nesse nivel!")
                    return self._produto_cadastro         
        elif opcao_estoque == 4:
            nivel_estoque = 5
            
            for produto_, produto_dados in self._produto_cadastro.items():
                if produto_dados.quantidade == nivel_estoque:
                    print("Produtos da marca ", produto_dados.marca)
                    print("Modelo: ",produto_dados.modelo)
                    print("Tamanho: ",produto_dados.tamanho)
                    print("Preço: ",produto_dados.preco)
                    print("Quantidade em estoque: ",produto_dados.quantidade)
                    print()
                    return self._produto_cadastro
                else:
                    print("Não encontrado nenhum produto nesse nivel!")
                    return self._produto_cadastro

        else:
            print("Opção invalida!")
    

class Vendas():
    def __init__(self,controle_estoque):
        self.controle_estoque = controle_estoque
        self.conpras_rea_dia = []
    
    def registrar_venda(self, marca_produto, modelo_produto, tamanho_produto, quantidade):
        chave_produto = (marca_produto, modelo_produto, tamanho_produto)
        produto = self.controle_estoque.produto.get(chave_produto)
        
        
        if produto and produto.quantidade >= quantidade:
            preco_pagar = quantidade * produto.preco
            compra = {
                "Marca": marca_produto,
                "Modelo": modelo_produto,
                "Tamanho": tamanho_produto,
                "Quantidade": quantidade,
                "Preço": preco_pagar
            }

            produto.quantidade -= quantidade
            self.conpras_rea_dia.append(compra)
            
            return True, "Venda realizada com sucesso!"
        else:
            return False, "Produto não encontrado ou quantidade insuficiente no estoque!"
   