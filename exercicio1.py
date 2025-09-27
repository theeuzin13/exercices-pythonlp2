class Aluno:

    def __init__(self, nome, idade, nota):
        self.__nome = nome
        self.__idade = idade
        self.__nota = nota

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def nota(self):
        return self.nota

    @nota.setter
    def cpf(self, nota):
        self.__nota = nota