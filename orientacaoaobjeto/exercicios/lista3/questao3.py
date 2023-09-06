class Elevador():
    def __init__(self,capacidade,total_andares):
        self._andar_atual = 0
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._quat_pessoas = 0    

    @property
    def entra(self):
        return self._quat_pessoas
    
    @entra.setter
    def entra(self,quantidade_pessoas_entra):
        if quantidade_pessoas_entra <= self._capacidade - self._quat_pessoas:
            self._quat_pessoas += quantidade_pessoas_entra
            print(f"{quantidade_pessoas_entra} pessoas entraram no elevador.")
        else:
            print("Não há mais capacidade!")
    
    @property
    def sair(self):
        return self._quat_pessoas
    @sair.setter
    def sair(self,quantidade_pessoas_sair):
        if self._quat_pessoas - quantidade_pessoas_sair > 0:
            self._quat_pessoas -= quantidade_pessoas_sair
            print(f"{quantidade_pessoas_sair} pessoa(s) saiu do elevador!")
        elif self._quat_pessoas - quantidade_pessoas_sair < 0 and self._quat_pessoas != 0:
            print(f"O elevador só tem {self._quat_pessoas} pessoas no momento por isso apenas uma vai sair!")
            self._quat_pessoas -= 1
            print(f"Quantidade de pesssas atualmente: {self._quat_pessoas}") 
        else:
            print("Nenhuma pesssoa saiu!")
        
    @property
    def sobe(self):
        return self._andar_atual
    @sobe.setter
    def sobe(self,qu_andares_subir):
        if self._andar_atual + qu_andares_subir < self._total_andares:
            self._andar_atual += qu_andares_subir
            print(f"O elevador subiu: {qu_andares_subir} andares")
            print("O elevador está no andar: ",self._andar_atual)
        elif self._andar_atual + qu_andares_subir >= self._total_andares and self._andar_atual != self._total_andares:
            print(f"O elevador pode subir até {self._total_andares  - self._andar_atual} andares")
            self._andar_atual += 1
            print(f"O elevador está no andar {self._andar_atual}")
        else:
            print("Ultimo andar!")
    
    @property
    def desce(self):
        return self._andar_atual
    @desce.setter
    def desce(self,qu_andares_descer):
        if self._andar_atual - qu_andares_descer > 0:
            self._andar_atual -= qu_andares_descer
            print("O elevador esta no andar: ",self._andar_atual)
        elif self._andar_atual - qu_andares_descer < 0 and self._andar_atual != 0:
            print(f"O elevador pode descer até {self._andar_atual} andares")
            self._andar_atual -= 1
            print(f"O elevador está no andar {self._andar_atual}")
        else:
            print("O elevador está no terreo!")
    
    def informacoes(self):
        print("Andar atual:", self._andar_atual)
        print("Quantidade de pessoas:", self._quat_pessoas)
        print("Capacidade:", self._capacidade)
        print("Total de andares:", self._total_andares)
    
    

elevador = None  
capacidade = int(input("Informe a capacidade: ")) 
total_andares = int(input("Informe a quantidade de andares: ")) 
elevador = Elevador(capacidade,total_andares)
while True:
    print("-------MENU--------")
    print("1-Entrar no elevador")
    print("2. Sair do elevador")
    print("3. Subir um andar")
    print("4. Descer um andar")
    print("5-informações")
    print("0. Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        quantidade_pessoas_entra = int(input("Quantas pessoas vão entrar: "))
        elevador.entra = quantidade_pessoas_entra
    elif opcao == "2":
        quantidade_pessoas_sair = int(input("Quantas pessoas vão sair: "))
        elevador.sair = quantidade_pessoas_sair
    elif opcao == "3":
        qu_andares_subir = int(input("Quantos andares vai subir: "))
        elevador.sobe = qu_andares_subir
    elif opcao == "4":
        qu_de_andares_decer = int(input("Quantos andares deseja descer: "))
        elevador.desce = qu_de_andares_decer
    elif opcao == "5":
        elevador.informacoes()
    elif opcao == "0":
        break
    else:
        print("Opção invalida!")
