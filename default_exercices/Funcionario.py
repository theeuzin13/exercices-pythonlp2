class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def getBonificacao(self):
        return self._salario * 0.1

    def __str__(self):
        return f'{self._nome}, {self._cpf}, {self._salario}'


class Gerente (Funcionario):

    def __init__(self, nome, cpf, salario, senha, n_funcionario):
        super().__init__(nome,cpf,salario)
        self.senha = senha
        self.n_funcionario = n_funcionario

    def getBonificacao(self):
        return super().getBonificacao() + 10 * self.n_funcionario




if __name__ == '__main__':

    ger = Gerente('Ana', '213.123.123-45', 2000, '123', 10)
    print(ger.getBonificacao())