from banco import Banco


if __name__ == '__main__':
    def menu():
        print("-"*25)
        print("-"+"MENU".center(20," ")+"-")
        print("-"*25)
        opcao = input(f"{'1  - Cadastrar  Cliente':<28}\n{'2  - Criar Conta Corrente':<28}\n{'3  - Criar Conta Poupança':<28}\n|{'4  - Criar Seguro de Vida':<28}\n|{'5  - Calcular Tributação':<28}\n|{'6  - Saque':<28}\n|{'7  - Depósito':<28}\n|{'8  - Transferir':<28}\n|{'9 - Historico de transaçoes':<28}\n{'10 - Mostrar tudo':<28}\n|{'11 - Sair':<28}\n{'-'*55}\nO que deseja fazer: ")
        print("-"*25)
        return opcao
       
        
    banco = Banco()
    while True:
        opcao = menu()
        resultado = None
        if ( opcao == '1' ):  # Cadastrar Clientes
            nome  = input("Insira um nome: ").upper()
            cpf   = input("CPF: ")
            resultado = banco.cadastrar_cliente(nome, cpf)
        elif ( opcao == '2' ):  # Criar conta corrente
            cpf   = input("CPF: ")
            num   = input("Numero da conta: ")
            resultado = banco.criar_conta_corrente(cpf, num)
        elif ( opcao == '3' ):  # Criar conta poupança
            cpf   = input("CPF: ")
            num   = input("Numero da conta: ")
            resultado = banco.criar_conta_poupanca(cpf, num)
        elif ( opcao == '4' ):  # Criar seguro
            cpf   = input("CPF: ")
            mensal= input("Valor mensal: ")
            total = input("Total: ")
            resultado = banco.criar_seguro(cpf, mensal, total)
        elif ( opcao == '5' ): # Calcular tributação
            resultado = banco.calc_tributos()
        elif ( opcao == '6' ): # Saque
            cpf   = input("CPF: ")
            num   = input("Numero da conta: ")
            valor = input("Valor: R$ ")
            resultado = banco.saque(cpf, num, valor)
        elif ( opcao == '7' ): # Deposito
            cpf   = input("CPF: ")
            num   = input("Numero da conta: ")
            valor = input("Valor: R$ ")
            resultado = banco.deposito(cpf, num, valor)
        elif ( opcao == '8' ): # transferencia
            cpf1  = input("CPF da conta de origem: ")
            contas = banco.consulta_contas(cpf1)
            if(contas[0]):
                if isinstance(contas[0], int):
                    if(contas[0] > 1):
                        for i in contas[1]:
                            print(f" {i}")
                num1  = input("Numero da conta de origem: ")
            else: 
                print(contas[1])
                continue
            cpf2  = input("CPF da conta de destino: ")
            contas = banco.consulta_contas(cpf2)
            if(contas[0]):
                if isinstance(contas[0], int):
                    if(contas[0] > 1):
                        for i in contas[1]:
                            print(f"{i}")
                num2  = input("Numero da conta de destino: ")
            else:
                print(contas[1])
                continue
            valor = input(" Valor: R$ ")
            resultado = banco.transferir(cpf1, num1, cpf2, num2, valor)
        elif ( opcao == '9' ): # Consultar historico de uma conta em específico
            cpf = input("CPF: ")
            num = input("Numero da conta: ")
            resultado = banco.extrato(cpf, num)
        elif ( opcao == '10' ): # Mostrar todos os clientes cadastrados no banco
            resultado = banco.mostrar_tudo()
        elif ( opcao == '11' ): # Sair
            break
        elif ( opcao == '12'): # Listar clientes
            resultado = banco.lista_clientes()
        else: # Previni contra teclas que não estão nas condições acima
            resultado = False, "Opção Inválida!"
        print(resultado[1])
        