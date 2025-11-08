from datetime import date

class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.titulo} - {self.autor}"


class Emprestimo:
    def __init__(self, codigo: int, data: date):
        self.codigo = codigo
        self.data = data
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def __str__(self):
        detalhes = f"Empréstimo {self.codigo}, Data: {self.data.strftime('%d/%m/%Y')}\nLivros:\n"
        for livro in self.livros:
            detalhes += f" - {livro}\n"
        return detalhes


if __name__ == "__main__":
    l1 = Livro("Dom Casmurro", "Machado de Assis")
    l2 = Livro("O Cortiço", "Aluísio Azevedo")

    e1 = Emprestimo(101, date(2025, 3, 1))
    e1.adicionar_livro(l1)
    e1.adicionar_livro(l2)

    print(e1)
