import mysql.connector
from dao.ContatoDao import ContadoDao
from model import Contato

from datetime import date

if __name__ == '__main__':

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='aula_bd'
        )

        dao = ContadoDao(connection)


        data = date(2000, 7, 13)
        contato = Contato('Matheus', '35998967579', 'matt.henrique13700@gmail.com', data)

        contatoSalvo = dao.salvar(contato)
        print(contatoSalvo)

        lista_contatos = dao.listar()
        # contato = dao.listar_por_id(1)
        # print(contato.nome, contato.celular, contato.email, contato.data_nasc, contato.id)
        #
        for cont in lista_contatos:
            print(cont.nome, cont.celular, cont.email, cont.data_nasc, cont.id)

    except Exception as e:
        print(e)