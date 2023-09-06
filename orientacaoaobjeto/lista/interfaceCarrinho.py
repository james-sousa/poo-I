from carrinho import CarrinhoDeCompras

carrinho_pessoa = CarrinhoDeCompras()

print("!----------Bem-vindo ao sistema de gerenciamento de compras-----!")
print("!---------Menu---------!")
while True:
    print("1-Adicionar ao carrinho: \n2-Bucar Produto: \n3-Calcular valor do carrinho: \n4-Listar compras: \n5-Sair: ")
    opcao = int(input())

    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        preco1 = input("Digite o preço do produto: ")
        preco = float(preco1)
        quantidade = int(input("Digite a quantidade que você comprou: "))
        compra = {'nome': nome,'preco': preco,'quantidade': quantidade}
        carrinho_pessoa.adicionarProdutos(compra)
    elif opcao == 2:
        nome = input("Digite o nome do produto que deseja buscar: ")
        carrinho_pessoa.bucarProduto(nome)
    elif opcao == 3:
        carrinho_pessoa.calcular()

    elif opcao == 4:
        carrinho_pessoa.listarCarrinho()
    
    elif opcao == 5:
        break

