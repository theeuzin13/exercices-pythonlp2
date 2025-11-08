class ConversaoDeUnidadeDeTempo:

    @staticmethod
    def minutos_para_segundos(minutos):
        return minutos * 60

    @staticmethod
    def horas_para_minutos(horas):
        return horas * 60

    @staticmethod
    def dias_para_horas(dias):
        return dias * 24

    @staticmethod
    def semanas_para_dias(semanas):
        return semanas * 7

    @staticmethod
    def meses_para_dias(meses):
        return meses * 30

    @staticmethod
    def anos_para_dias(anos):
        return anos * 365.25

if __name__ == "__main__":
    print("5 minutos = ", ConversaoDeUnidadeDeTempo.minutos_para_segundos(5), "segundos")
    print("2 horas = ", ConversaoDeUnidadeDeTempo.horas_para_minutos(2), "minutos")
    print("3 dias = ", ConversaoDeUnidadeDeTempo.dias_para_horas(3), "horas")
    print("4 semanas = ", ConversaoDeUnidadeDeTempo.semanas_para_dias(4), "dias")
    print("6 meses = ", ConversaoDeUnidadeDeTempo.meses_para_dias(6), "dias")
    print("2 anos = ", ConversaoDeUnidadeDeTempo.anos_para_dias(2), "dias")
