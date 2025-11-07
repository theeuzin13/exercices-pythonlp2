From Funcionario import Funcionario, Gerente

class ControleBonificacao:

    def __init__(self):
        self.__total = 0

    def addBonificacao(self, obj):
        self.__total += obj.getBonificacao()

    @property
    def total(self):
        return self.__total

