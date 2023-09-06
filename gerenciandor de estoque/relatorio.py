class Relatorios():
    def __init__(self):
        self.movimentacoes = []

class Relatorio(Relatorios):

    def registrar_cadastro_produto(self, marca, modelo, tamanho,quantidade):
        movimento = f"Cadastro de novo produto: Marca = {marca}, Modelo = {modelo}, Tamanho = {tamanho} Quantidade cadastrada = {quantidade}"
        self.movimentacoes.append(movimento)

    def registrar_reposicao_estoque(self, marca, modelo, tamanho, quantidade):
        movimento = f"Reposição de estoque: Marca = {marca}, Modelo = {modelo}, Tamanho = {tamanho}, Quantidade reposta = {quantidade}"
        self.movimentacoes.append(movimento)

    def registrar_venda(self, marca, modelo, tamanho, quantidade):
        movimento = f"Venda de produto: Marca = {marca}, Modelo = {modelo}, Tamanho = {tamanho}, Quantidade = {quantidade}"
        self.movimentacoes.append(movimento)
    
    def registrar_remoção(self, marca, modelo, tamanho):
        movimento = f"Remoção de produto: Marca = {marca}, Modelo = {modelo}, Tamanho = {tamanho}"
        self.movimentacoes.append(movimento)

    def mostrar_movimentacoes(self):
        for movimento in self.movimentacoes:
            print(movimento)