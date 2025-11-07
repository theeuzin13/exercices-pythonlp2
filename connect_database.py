import mysql.connector
from dao.ContatoDao import ContadoDao

if __name__ == '__main__':

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='aula_bd'
        )

        dao = ContadoDao(connection)

        lista_contatos = dao.listar()

        for cont in lista_contatos:
            print(cont.nome, cont.celular, cont.email, cont.data_nasc, cont.id)

    except Exception as e:
        print(e)