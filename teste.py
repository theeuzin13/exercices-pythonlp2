import mysql.connector
from dao.ContatoDao import ContactDAO
from model import Contact

from datetime import date

if __name__ == '__main__':

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='aula_bd'
        )

        dao = ContactDAO(connection)


        data = date(2000, 7, 13)
        contato = Contact('Felipe', '0000000000', 'matt.henrique0@gmail.com', data, 3)

        contatoSalvo = dao.create(contato)
        print(contatoSalvo)



        lista_contatos = dao.find()
        # contato = dao.listar_por_id(1)
        # print(contato.nome, contato.celular, contato.email, contato.data_nasc, contato.id)
        #
        for cont in lista_contatos:
            print(cont.nome, cont.celular, cont.email, cont.data_nasc, cont.id)

        dao.delete(6)
    except Exception as e:
        print(e)