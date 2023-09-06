from mercado import  Carrinho


produtos = Carrinho()
print("!----MENU----!")

while True:
    print("1-Cadastrar produto\n2-Listar produtos\n3-Adicioanr ao carrinho\n4-listar compras\n5-Sair: ")
    escolha = int(input())

    if escolha == 1:
        nome = input("Digite o nome: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))

        produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
        produtos.cadastrar(produto)
    
    elif escolha == 2:
        produtos.listar_produtos()
    
    elif escolha == 3:
        nome = input("Nome: ")
        produtos.adicionar_carrinho(nome)
    
    elif escolha == 4:
        produtos.imprimir_carrinho()
    
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")