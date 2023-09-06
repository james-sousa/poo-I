from agenda import Agenda

contatos = Agenda()

print("!----MENU----!")

while True:
    print("1-Adicionar Contato\n2-Listar contatos\n3-Busca\n4-Remover\n5-Sair: ")
    escolha = int(input())

    if escolha == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")

        contato = {"nome": nome, "email": email, "telefone": telefone}
        contatos.adicionar(contato)
    
    elif escolha == 2:
        contatos.listar()
    
    elif escolha == 3:
        nome = input("Nome: ")
        contatos.busca(nome)
    
    elif escolha == 4:
        nome = input("Nome: ")
        contatos.remover(nome)
    
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")