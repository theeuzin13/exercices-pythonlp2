from model import Contato

SQL_SELECT_CONTATOS = 'SELECT * FROM contato;'

class ContadoDao:

    def __init__(self, conn):
        self.__conn = conn

    def listar(self):
        cursor = self.__conn.cursor()
        cursor.execute(SQL_SELECT_CONTATOS)
        lista_tuplas = cursor.fetchall()
        lista_contatos = self.__traduz_contatos(lista_tuplas)
        return lista_contatos

    def __traduz_contatos(self, lista):
        lista_contatos = []

        for tupla in lista:
            cont = Contato(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
            lista_contatos.append(cont)
        return lista_contatos