from estoque import *
from funcionario import Cadastrar_funcionario
from sistema_login import Login
import re
from relatorio import Relatorio
cadastro_funcionario = Cadastrar_funcionario()
fazer_login = Login(cadastro_funcionario)
controle_estoque = Controle_estoque()
vendas = Vendas(controle_estoque)
relatorio = Relatorio()
def validar_texto(texto):
    # A expressão regular [a-zA-Z\s]+ verifica se o texto contém apenas letras e espaços em branco.
    return re.match(r'^[a-zA-Z\s]+$', texto)
while True:
    
    
    print("*" * 37)
    print("|Bem-Vindo ao Sistema da Donna Shoes|")
    print("|                                   |")
    print("|                                   |")
    print("| ----------MENU OPÇÔES----------   |")
    print("|                                   |")
    print("|     1-Cadastrar gerente           |")
    print("|     2-Cadastrar Funcionario       |")
    print("|     3-Cadastrar ou Repor produto  |")
    print("|     4-Listar produtos em estoque  |")
    print("|     5-Registrar venda             |")
    print("|     6-Relatório de movimentação   |")
    print("|     7-Remover produto             |")
    print("|     8-Niveis de estoque           |")
    print("|     9-Listar funcionarios         |")
    print("|     10-Sair                       |")
    print("|                                   |")
    print("*"*37)
    escolha = input("Sua escolha: ")
    try:
        escolha = int(escolha)
    except ValueError:
        print("Opção invalida. Por favor, digite um numero inteiro!")
   
    if escolha == 1:
        print("Apenas um gerente pode ser cadastrado!")
        print()
        nome = input("Digite o nome: ").upper()
        if not validar_texto(nome):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
        
        cpf_funcionario = input("Cpf gerente: ")
        try:
            cpf_funcionario = int(cpf_funcionario)
            if cpf_funcionario <= 0:
                print("Cpf inválido. Certifique-se de inserir um número positivo.")
                continue  # volte ao início
        except ValueError:
            print("Cpf inválido. Certifique-se de inserir um número inteiro.")
            continue  # volte ao início
        cargo = "GERENTE"
        senha_acesso = input("Crie uma senha de acesso: ")
        cadastro_funcionario.cadastrar_funcionario(nome,cpf_funcionario,cargo,senha_acesso)
    
    elif escolha == 2:
        print("Apenas gerentes podem acessar essa pagina!")
        cpf_realizar_lg = input("Gerente digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Valor invalido digite apenas numeros inteiros!")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        try:
            resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        except Exception:
            print("Erro durante o login. Usuario ao senha invalido!")
            continue #volte ao inicio
        
        if resultado == True and cargo == "GERENTE":
            print("Login realizado com sucesso!")
            print()
            print("Apenas os cargos de vendedor e estoquista estão disponiveis para cadastro!")
            nome = input("Digite o nome do funcionario que deseja cadastrar: ").upper()
            if not validar_texto(nome):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
            
            try:
                cpf_funcionario = input("Cpf funcionario: ")
                try:
                    cpf_funcionario = int(cpf_funcionario)
                except ValueError:
                    print("Valor invalido digite apenas numeros inteiros!")
                    continue #volte ao inicio
                if cpf_funcionario <= 0:
                    print("Cpf inválido. Certifique-se de inserir um numero positivo.")
                    continue #volte ao inicio
            except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número válido.")
                    continue #volte ao inicio
            cargo = input("Cargo: ").upper()
            if not validar_texto(cargo):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
            senha_acesso = input("Crie uma senha de acesso: ")
            if cargo not in ["VENDEDOR","VENDEDORA", "ESTOQUISTA"]:
                print("Cargo indisponivel para cadastro no momento! Certifique-se de cadastrar apenas vendedores ou estoquistas!")
                continue #volte ao inicio
            cadastro_funcionario.cadastrar_funcionario(nome,cpf_funcionario,cargo,senha_acesso)
        else:
            print("Usuário não autorizado a fazer essa operação!")
            print("Apenas gerentes podem fazer essa operação! Certifique-se de ter cadstrado um gerente indo na opção de listar funcionarios!")
    
    elif escolha == 3:
        print("Apenas estoquistas podem acessar essa pagina!")
        cpf_realizar_lg = input("Digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Cpf inválido. Certifique-se de inserir um número inteiro.")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        try:
            resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        except Exception:
            print("Erro durante o login! Usuario ou senha invalido" )
            continue #volte ao inicio
        if resultado == True and cargo == "ESTOQUISTA":
            print("Login realizado!")
            print("O que voce deseja fazer?\n1-Cadastrar Produto\n2-Repor estoque: ")
            opcao = int(input("Digite sua escolha: "))
            if opcao == 1:
                marca = input("Digite a marca: ").upper()
                
                if not validar_texto(marca):
                    print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                    continue # volte ao inicio
                modelo = input("Modelo: ").upper()
                if not validar_texto(modelo):
                    print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                    continue # volte ao inicio
                try:
                    preco = float(input("Digite o preço: "))
                    if preco <= 0.0:
                        print("Preço inválido. Insira um valor positivo.")
                        continue #volte ao inicio
                    quantidade = input("Digite a quantidade a ser cadastrada no estoque: ")
                    try:
                        quantidade = int(quantidade)
                    except ValueError:
                        print("Valor invalido digite apenas numeros inteiros!")
                        continue #volte ao inicio
                    if quantidade <= 0:
                        print("Quantidade inválida. Insira um valor positivo.")
                        continue #volte ao inicio
                except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número válido.")
                    continue #volte ao inicio
                
                try:
                    tamanho = input("Tamanho do calçado: ")
                    try:
                        tamanho = int(tamanho)
                    except ValueError:
                        print("Valor invalido digite apenas numeros inteiros!")
                        continue #volte ao inicio
                    if tamanho <= 0:
                        print("Tamanho inválido. Certifique-se de inserir um numero positivo.")
                        continue #volte ao inicio
                except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número válido.")
                    continue #volte ao inicio
                retorno,retornodesc = controle_estoque.cadastrar_produto(marca,modelo,tamanho,preco,quantidade)
                if retorno == True:
                    relatorio.registrar_cadastro_produto(marca,modelo,tamanho,quantidade)
            
            elif opcao == 2:
                marca = input("Digite a marca: ").upper()
                
                if not validar_texto(marca):
                    print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                    continue # volte ao inicio
                modelo = input("Modelo: ").upper()
                if not validar_texto(modelo):
                    print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                    continue # volte ao inicio
                try:
                    tamanho = input("Tamanho do calçado: ")
                    try:
                        tamanho = int(tamanho)
                    except ValueError:
                        print("Valor invalido digite apenas numeros inteiros!")
                        continue #volte ao inicio
                    if tamanho <= 0:
                        print("Tamanho inválido. Certifique-se de inserir um numero positivo.")
                        continue #volte ao inicio
                except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número válido.")
                    continue #volte ao inicio
                retornorp,retronorpdesc = controle_estoque.reposicao_estoque(marca,modelo,tamanho)
                if retornorp == True:
                    relatorio.registrar_reposicao_estoque(marca,modelo,tamanho,retronorpdesc)
        else:
            print("Funcionário não autorizado a fazer essa operação!")
            print("Apenas estoquistas podem fazer essa operação! Certifique-se de ter cadstrado um estoquista indo na opção de listar funcionarios!")  
    
    elif escolha == 4:
        print("Todos os funcionarios podem acessar essa pagina!")
        
        cpf_realizar_lg = input("Digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Valor invalido digite apenas numeros inteiros!")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        try:
            resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        except Exception:
            print("Erro durante o login. Usuario ao senha invalido!")
            continue #volte ao inicio
        if resultado == True and cargo == "GERENTE" or cargo == "VENDEDOR" or cargo == "VENDEDORA" or cargo == "ESTOQUISTA":
            print("Login realizado!")
            controle_estoque.listar_produtos()
        else:
            print("Usuário não autorizado a fazer essa operação!")
            print("Certifique-se de ter cadstrado um funcionario indo na opção de listar funcionarios!")
    
    elif escolha == 5:
        print("Apenas vendedores podem acessar essa pagina!")
        
        cpf_realizar_lg = input("Vendedor digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Valor invalido digite apenas numeros inteiros!")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        try:
            resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        except Exception:
            print("Erro durante o login. Usuario ao senha invalido!")
            continue #volte ao inicio
        if resultado == True and cargo == "VENDEDOR" or cargo == "VENDEDORA":
            print("Login realizado!")
            marca_prodt = input("Marca: ").upper()
            if not validar_texto(marca_prodt):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
            modelo_prodt = input("Modelo: ").upper()
            if not validar_texto(modelo_prodt):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
            try:
                tamanho_prodt = input("Tamanho do calçado: ")
                try:
                    tamanho_prodt = int(tamanho_prodt)
                except ValueError:
                    print("Valor invalido digite apenas numeros inteiros!")
                    continue #volte ao inicio
                if tamanho_prodt <= 0:
                    print("Preço inválido. Insira um valor positivo.")
                    continue #volte ao inicio
                quantidade = input("Digite a quantidade: ")
                try:
                    quantidade = int(quantidade)
                except ValueError:
                    print("Valor invalido digite apenas numeros inteiros!")
                    continue #volte ao inicio
                if quantidade <= 0:
                    print("Quantidade inválida. Insira um valor positivo.")
                    continue #volte ao inicio
            except ValueError:
                print("Valor inválido. Certifique-se de inserir um número válido.")
                continue #volte ao inicio
            retornovd,mensagem = vendas.registrar_venda(marca_prodt,modelo_prodt,tamanho_prodt,quantidade)
            print(mensagem)
            if retornovd == True:
                relatorio.registrar_venda(marca,modelo,tamanho,quantidade)
        else:
            print("Usuário não autorizado a fazer essa operação!")
            print("Apenas vendedores podem realizar essa operação! Certifique-se de ter cadstrado um vendedor indo na opção de listar funcionarios!")
        
    elif escolha == 6:
        print("Apenas estoquistas e gerentes podem acessar essa pagina!")
        cpf_realizar_lg = input("Gerente ou Estoquista digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Valor invalido digite apenas numeros inteiros!")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        if resultado == True and cargo == "ESTOQUISTA" or cargo == "GERENTE":
            relatorio.mostrar_movimentacoes() 
        else:
            print("Usuário não autorizado a fazer essa operação!")
            print("Apenas estoquistas e o gerente podem fazer essa operação! Certifique-se de ter cadstrado um estoquista ou um gerente indo na opção de listar funcionarios!")
    
    elif escolha == 7:
        print("Apenas estoquistas e gerentes podem acessar essa pagina!")
        cpf_realizar_lg = input("Gerente ou Estoquista digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Valor invalido digite apenas numeros inteiros!")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        try:
            resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        except Exception:
            print("Erro durante o login. Usuario ao senha invalido!")
            continue #volte ao inicio
        if resultado == True and cargo == "ESTOQUISTA" or cargo == "GERENTE":
            print("Login realizado!")
            marca = input("Marca: ").upper()
            if not validar_texto(marca):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
            modelo = input("Modelo: ").upper()
            if not validar_texto(modelo):
                print("Nome inválido. Certifique-se de inserir apenas letras e espaços.")
                continue # volte ao inicio
            try:
                tamanho = input("Tamanho do calçado: ")
                try:
                    tamanho = int(tamanho)
                except ValueError:
                    print("Valor invalido digite apenas numeros inteiros!")
                    continue #volte ao inicio
                if tamanho <= 0:
                    print("Preço inválido. Insira um valor positivo.")
                    continue #volte ao inicio
            except ValueError:
                print("Valor inválido. Certifique-se de inserir um número válido.")
                continue #volte ao inicio
            retornorm = controle_estoque.remover_produto(marca,modelo,tamanho)
            if retornorm == True:
                relatorio.registrar_remoção(marca,modelo,tamanho)

        else:
            print("Usuário não autorizado a fazer essa operação!")
            print("Apenas estoquistas e o gerente podem fazer essa operação! Certifique-se de ter cadstrado um estoquista ou um gerente indo na opção de listar funcionarios!")
    
    elif escolha == 8:
        print("Apenas estoquistas podem acessar essa pagina!")
        cpf_realizar_lg = input("Estoquista digite o seu cpf: ")
        try:
            cpf_realizar_lg = int(cpf_realizar_lg)
        except ValueError:
            print("Valor invalido digite apenas numeros inteiros!")
            continue #volte ao inicio
        senha_realizar_lg = input("Digite a sua senha do sitema: ")
        try:
            resultado,cargo = fazer_login.autenticacao(cpf_realizar_lg,senha_realizar_lg)
        except Exception:
            print("Erro durante o login! Usuario ao senha invalido!")
            continue #volte ao inicio
        if resultado == True and cargo == "ESTOQUISTA":
            print("Login realizado!")
            controle_estoque.niveis_de_estoque()
        else:
            print("Usuário não autorizado a fazer essa operação!")
            print("Apenas estoquistas podem fazer essa operação! Certifique-se de ter cadstrado um estoquista indo na opção de listar funcionarios!")
    
    elif escolha == 9:
        cadastro_funcionario.listar_funcionarios()
    
    elif escolha == 10:
        print("Saindo...")
        break

    else:
        print("Opção invalida!")
