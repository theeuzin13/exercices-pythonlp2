class Aluno:

    def __init__(self, nome, idade, nota):
        self.__nome = nome
        self.__idade = idade
        self.__nota = nota

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

if __name__ == '__main__':
    al1 = Aluno('Gabriel', 22, 7.3)
    al2 = Aluno('Isabela', 16, 10.0)

    print(f'Aluno 1: {al1.nome}, Idade: {al1.idade}, Nota: {al1.nota}')
    print(f'Aluno 2: {al2.nome}, Idade: {al2.idade}, Nota: {al2.nota}')

    # Alterando atributos com os setters
    al1.nome = 'Gabriel Santos'
    al1.nota = 8.5

    print(f'Aluno 1 (atualizado): {al1.nome}, Idade: {al1.idade}, Nota: {al1.nota}')