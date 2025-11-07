from datetime import date

class Dependente:
    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc

    def __str__(self):
        return (f'Dependente: {self.nome}, {self.data_nasc.strftime("%d/%m/%Y")}')


class Socio:
    mensalidade_base = 400.00

    def __init__(self, nome, cel, data_nasc):
        self.nome = nome
        self.cel = cel
        self.data_nasc = data_nasc
        self.deps = []

    def addDep(self, nome, dt_nasc):
        dep = Dependente(nome, dt_nasc)
        self.deps.append(dep)

    def getMensalidade(self):
        return Socio.mensalidade_base + 50 * len(self.deps)

    def __str__(self):
        str_socio = f'Sócio: {self.nome}, Cel: {self.cel}, Nasc: {self.data_nasc.strftime("%d/%m/%Y")}\nDependentes:\n'
        for dep in self.deps:
            str_socio += dep.__str__() + '\n'
        return str_socio


if __name__ == '__main__':
    s1 = Socio('Carlos', '(35)3571-2542', date(1980, 1, 21))
    s1.addDep('Gabi', date(2000, 5, 14))
    s1.addDep('Davi', date(2015, 8, 31))

    print(s1)
    print(f'Mensalidade: R${s1.getMensalidade():.2f}')
