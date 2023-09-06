def agenda():
    lista = []
    maximo = 2
    while maximo >= 0:
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        cep = input("CEP: ")
        bairro = input("Bairro: ")
        telefone = input("Telefone: ")
        
        pessoa = [nome,endereco,cep,bairro,telefone]
        lista.append(pessoa)

        maximo = maximo - 1
    
    print("Agenda:\n")
    
    for pessoa in reversed(lista):
        print(pessoa)


if agenda:
    agenda()
