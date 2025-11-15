from model import Contact

SQL_SELECT_CONTATOS = 'SELECT * FROM contato;'
SQL_SELECT_CONTATOS_ID = 'SELECT * FROM contato WHERE id_contato = %s'
SQL_INSERT_CONTATO = 'INSERT INTO contato (nome_contato, cel_contato, email_contato, data_nasc_contato) VALUES(%s, %s, %s, %s)'
SQL_UPDATE_CONTATO = 'UPDATE contato SET nome_contato=%s, cel_contato=%s, email_contato=%s, data_nasc_contato=%s WHERE id_contato=%s'
SQL_DELETE_CONTATO = 'DELETE FROM contato Where id_contato = %s'

class ContactDAO:

    def __init__(self, db):
        self.__db = db

    def create(self, contact):
        cursor = self.__db.connection.cursor()

        if contact.id is None:
            cursor.execute(SQL_INSERT_CONTATO,
                   (contact.name, contact.phone, contact.email, contact.date_of_birth)
            )
            contact.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_CONTATO,
               (contact.name, contact.phone, contact.email, contact.date_of_birth, contact.id)
           )

        self.__db.connection.commit()

        return contact

    def find(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CONTATOS)
        list = cursor.fetchall()
        contact_list = self.__translate_contacts(list)
        return contact_list

    def findOne(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CONTATOS_ID, (id,))
        tuple = cursor.fetchone()
        cont = self.__translate_contact(tuple)
        return cont

    def __translate_contacts(self, list):
        contatc_list = []

        for tuple in list:
            cont = self.__translate_contact(tuple)
            contatc_list.append(cont)
        return contatc_list

    def __translate_contact(self, tuple):
        cont = Contact(tuple[1], tuple[2], tuple[3], tuple[4], tuple[0])
        return cont

    def delete(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_CONTATO, (id,))
        self.__db.connection.commit()
        print(f'Contact {id} was deleted successfully.')


