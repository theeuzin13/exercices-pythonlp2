class Carros:

    def __init__(self, modelo, cor, ano, preco_venda, id=None):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco_venda = preco_venda
        self.id = id

    def __str__(self):
        return self.modelo
