class Departamento:
    def __init__(self, nome: str, sigla: str):
        self.nome = nome
        self.sigla = sigla

    def __str__(self):
        return f"Departamento: {self.nome} ({self.sigla})"


class Funcionario:
    def __init__(self, nome: str, cargo: str, departamento: Departamento):
        self.nome = nome
        self.cargo = cargo
        self.departamento = departamento

    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, {self.departamento}"

if __name__ == "__main__":
    d1 = Departamento("Tecnologia da Informação", "TI")
    d2 = Departamento("Recursos Humanos", "RH")

    f1 = Funcionario("Ana Souza", "Analista de Sistemas", d1)
    f2 = Funcionario("Carlos Silva", "Recrutador", d2)

    print(f1)
    print(f2)