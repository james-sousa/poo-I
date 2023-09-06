agenda = {}

def incluirNovoNome(nome, telefones):
    agenda[nome] = telefones
    print("Nome adicionado com sucesso!")

def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
        print("Telefone adicionado com sucesso!")
    else:
        resposta = input("Nome não encontrado na agenda. Deseja incluí-lo? (s/n): ")
        if resposta.lower() == "s":
            incluirNovoNome(nome, [telefone])

def excluirTelefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            if len(agenda[nome]) == 0:
                excluirNome(nome)
            print("Telefone excluído com sucesso!")
        else:
            print("Telefone não encontrado para esse nome.")
    else:
        print("Nome não encontrado na agenda.")

def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]
        print("Nome excluído com sucesso!")
    else:
        print("Nome não encontrado na agenda.")

def consultarTelefone(nome):
    if nome in agenda:
        telefones = agenda[nome]
        print(f"Telefones de {nome}:")
        for telefone in telefones:
            print(telefone)
    else:
        print("Nome não encontrado na agenda.")

while True:
    print("\nMenu:")
    print("1. Incluir novo nome")
    print("2. Incluir telefone")
    print("3. Excluir telefone")
    print("4. Excluir nome")
    print("5. Consultar telefone")
    print("Digite um número negativo para encerrar o programa.")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        nome = input("Digite o nome: ")
        telefones = input("Digite os telefones (separados por vírgula): ").split(",")
        incluirNovoNome(nome, telefones)
    elif opcao == 2:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        incluirTelefone(nome, telefone)
    elif opcao == 3:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        excluirTelefone(nome, telefone)
    elif opcao == 4:
        nome = input("Digite o nome: ")
        excluirNome(nome)
    elif opcao == 5:
        nome = input("Digite o nome: ")
        consultarTelefone(nome)
    elif opcao < 0:
        break
    else:
        print("Opção inválida. Tente novamente.")
