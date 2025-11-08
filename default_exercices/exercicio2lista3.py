from abc import ABC, abstractmethod

class Progressao(ABC):
    def __init__(self, primeiro, n):
        self.primeiro = primeiro
        self.n = n

    @abstractmethod
    def soma(self):
        pass

    @abstractmethod
    def termo(self, k):
        pass


class ProgressaoAritmetica(Progressao):
    def __init__(self, primeiro, n, razao):
        super().__init__(primeiro, n)
        self.razao = razao

    def soma(self):
        return (self.n / 2) * (2 * self.primeiro + (self.n - 1) * self.razao)

    def termo(self, k):
        return self.primeiro + (k - 1) * self.razao

    def __str__(self):
        termos = [str(self.termo(i)) for i in range(1, self.n + 1)]
        return "PA: " + ", ".join(termos)


class ProgressaoGeometrica(Progressao):
    def __init__(self, primeiro, n, razao):
        super().__init__(primeiro, n)
        self.razao = razao

    def soma(self):
        return self.primeiro * ((self.razao**self.n - 1) / (self.razao - 1))

    def termo(self, k):
        return self.primeiro * (self.razao ** (k - 1))

    def __str__(self):
        termos = [str(self.termo(i)) for i in range(1, self.n + 1)]
        return "PG: " + ", ".join(termos)

if __name__ == "__main__":
      pa = ProgressaoAritmetica(primeiro=2, n=5, razao=3)
      pg = ProgressaoGeometrica(primeiro=3, n=4, razao=2)
      
      print(pa)
      print(f"Soma da PA: {pa.soma()}")
      print(f"3º termo da PA: {pa.termo(3)}")
      
      print(pg)
      print(f"Soma da PG: {pg.soma()}")
      print(f"3º termo da PG: {pg.termo(3)}")