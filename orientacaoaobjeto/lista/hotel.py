class Administracao():
    pass

class Cliente():
    pass

class Funcionario():
    pass

class Gerente():
    pass

class Hotel():
    quarto_reservardo = []
    def __init__(self):
        self.quartos_disponiveis = []
    
    def adicionar_quarto(self,quarto):
        
        self.quartos_disponiveis.append(quarto)
        print("Adicionado!")
        
    def busca_quarto(self,numero):
        for quarto_cadastrado in self.quartos_disponiveis:
            if quarto_cadastrado['numero'] == numero:
                print("Tipo: ",quarto_cadastrado['tipo'])
                print("Preço: ",quarto_cadastrado['preco'])
                return self.quartos_disponiveis
        else:
            print("Quarto indisponível!")
    
    def fazer_reserva(self,numero):
        for quarto_cadastrado in self.quartos_disponiveis:
            if quarto_cadastrado['numero'] == numero:
                self.quarto_reservardo.append(quarto_cadastrado)
                print("Quarto reservado!")
                self.quartos_disponiveis.remove(quarto_cadastrado)
                return self.quartos_disponiveis
        else:
            print("Quarto Indisponível!")
    
    def cancelar_reserva(self,numero):
        for quarto_reservado in self.quarto_reservardo:
            if quarto_reservado['numero'] == numero:
                self.quartos_disponiveis.append(quarto_reservado)
                self.quarto_reservardo.remove(quarto_reservado)
                print("Reserva cancelada com sucesso!")
                return self.quarto_reservardo,self.quartos_disponiveis
        else:
            print("Reserva não encontrada!")

    def verificar_disponibilidade(self):
        for quarto in self.quartos_disponiveis:
            print("Numero: ",quarto['numero'])
            print("Tipo: ",quarto['tipo'])
            print("Preço: ",quarto['preco'])

    def verificar_reservados(self):
        for quarto in self.quarto_reservardo:
            print("Numero: ",quarto['numero'])
            print("Tipo: ",quarto['tipo'])
            print("Preço: ",quarto['preco'])    
    

    


quarto = Hotel()
quato1 = {'numero': 142,'tipo': "solteiro", 'preco': 142.50}
quarto.adicionar_quarto(quato1)
quato2 = {'numero': 143,'tipo': "casal",'preco': 180.87}
quarto.adicionar_quarto(quato2)
quarto3 = {'numero': 144,'tipo': "casal",'preco': 185.80}
quarto.adicionar_quarto(quarto3)
quarto4 = {'numero': 145,'tipo': "solteiro",'preco': 178.87}
quarto.adicionar_quarto(quarto4)
quarto5 = {'numero': 159,'tipo': "duplo",'preco': 200.00}
quarto.adicionar_quarto(quarto5)
quarto.verificar_disponibilidade()
numero = int(input("Digite o numero: "))
quarto.fazer_reserva(numero)
quarto.verificar_disponibilidade()
numero = int(input("Digite o numero: "))
quarto.fazer_reserva(numero)
print()
quarto.verificar_reservados()
numero = int(input("Digite o numero: "))
quarto.cancelar_reserva(numero)
quarto.verificar_disponibilidade()