class Televisao:
    def __init__(self):
        self.volume = 0
        self.canal = 1
    
    def aumentar_volume(self):
        self.volume += 1
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
    
    def trocar_canal(self, novo_canal):
        self.canal = novo_canal
    
    def consultar_informacoes(self):
        print(f"Volume: {self.volume}")
        print(f"Canal: {self.canal}")


class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao
    
    def mostrar_menu(self):
        opcao = 0
        while opcao != 5:
            print("\n----- MENU -----")
            print("1. Aumentar volume")
            print("2. Diminuir volume")
            print("3. Trocar de canal")
            print("4. Consultar informações da TV")
            print("5. Sair")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                self.televisao.aumentar_volume()
            elif opcao == 2:
                self.televisao.diminuir_volume()
            elif opcao == 3:
                novo_canal = int(input("Digite o número do novo canal: "))
                self.televisao.trocar_canal(novo_canal)
            elif opcao == 4:
                self.televisao.consultar_informacoes()
            elif opcao == 5:
                print("Desligando")
            else:
                print("Opção inválida! Tente novamente.")


# Testando as classes
tv = Televisao()
controle = ControleRemoto(tv)
controle.mostrar_menu()
