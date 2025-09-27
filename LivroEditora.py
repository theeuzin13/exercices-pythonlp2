from datetime import date

class Dependente:

    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc

    # TO DO __str__
    def __str__(self):
        return (f'Dependente: {self.nome}, {self. data_nasc},{self.data_nasc.strftime("%d/%m/%Y")}')

# ---------------------------------
class Socio():

    def __init__(self, nome, cel, data_nasc):
        self.nome = nome
        self.cel = cel
        self.data_nasc = data_nasc
        self.deps = []

    def addDep(self, nome, dt_nasc):
        dep = Dependente(nome, dt_nasc)
        self.deps.append(dep)

    # TO DO cálculo mensalidade
    def getMensalidade(self):
        return 500 + 50 * len(self.deps)

    # TO DO __str__
    def __str__(self):
        str_socio = f'Socio: {self.nome},\nDependentes:\n'
        for dep in self.deps:
            str_socio += dep.__str__() + '\n'
        return str_socio

# ---------------------------------

if __name__ == '__main__':
    #dep1 = Dependente('Gabi', date(2000, 5, 14))
    #dep2 = Dependente('Davi', date(2015, 8, 31))

    s1 = Socio('Carlos', '(35)3571-2542', date(1980, 1, 21))
    s1.addDep('Gabi', date(2000, 5, 14))
    s1.addDep('Davi', date(2015, 8, 31))
    print(s1)
    print(f'Mensalidade: {s1.getMensalidade():.2f}')
