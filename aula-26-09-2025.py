class Pessoa:
    __total_pessoas = 0

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self._idade = idade
        self.__cpf = cpf
        Pessoa.__total_pessoas += 1

    def __mostra(self):
        print(self.nome, self._idade, self.__cpf)

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @classmethod
    def getTotalPessoas(cls):
        return cls.__total_pessoas


if __name__ == '__main__':
    p1 = Pessoa('Maria',42,'123')
    p2 = Pessoa('Matheus', 25, '432')

    print(Pessoa.getTotalPessoas())