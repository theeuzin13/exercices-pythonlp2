class Retangulo:

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def calcula_perimetro(self):
        return 2 * (self.__base + self.__altura)

    def calcula_area(self):
        return self.__base * self.__altura


if __name__ == '__main__':
    # Criando um retângulo com base 10 e altura 5
    r = Retangulo(10, 5)

    print(f"Base: {r.base}")
    print(f"Altura: {r.altura}")
    print(f"Perímetro: {r.calcula_perimetro()}")
    print(f"Área: {r.calcula_area()}")

    # Alterando os valores
    r.base = 20
    r.altura = 15

    print("\nApós alteração:")
    print(f"Nova base: {r.base}")
    print(f"Nova altura: {r.altura}")
    print(f"Novo perímetro: {r.calcula_perimetro()}")
    print(f"Nova área: {r.calcula_area()}")
