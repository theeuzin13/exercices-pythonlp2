from model import Contato

SQL_SELECT_CONTATOS = 'SELECT * FROM contato;'
SQL_SELECT_CONTATOS_ID = 'SELECT * FROM contato WHERE id_contato = %s'
SQL_INSERT_CONTATO = 'INSERT INTO contato (nome_contato, cel_contato, email_contato, data_nasc_contato) VALUES(%s, %s, %s, %s)'

class ContadoDao:

    def __init__(self, conn):
        self.__conn = conn

    def salvar(self, contato):
        cursor = self.__conn.cursor()

        if contato.id is None:
            cursor.execute(SQL_INSERT_CONTATO,
                   (contato.nome, contato.celular, contato.email, contato.data_nasc)
            )
            contato.id = cursor.lastrowid
        else:
            pass
        self.__conn.commit()

        return contato

    def listar(self):
        cursor = self.__conn.cursor()
        cursor.execute(SQL_SELECT_CONTATOS)
        lista_tuplas = cursor.fetchall()
        lista_contatos = self.__traduz_contatos(lista_tuplas)
        return lista_contatos

    def listar_por_id(self, id):
        cursor = self.__conn.cursor()
        cursor.execute(SQL_SELECT_CONTATOS_ID, (id,))
        tupla = cursor.fetchone()
        cont = self.__traduz_contato(tupla)
        return cont

    def __traduz_contatos(self, lista):
        lista_contatos = []

        for tupla in lista:
            cont = self.__traduz_contato(tupla)
            lista_contatos.append(cont)
        return lista_contatos

    def __traduz_contato(self, tupla):
        cont = Contato(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        return cont