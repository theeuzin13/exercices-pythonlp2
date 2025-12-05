from avaliacao.model.carros import Carros

SQL_SELECT_CARROS= 'SELECT * FROM carros;'
SQL_SELECT_CARROS_ID = 'SELECT * FROM Carros WHERE id_carro = %s'
SQL_INSERT_CARROS = 'INSERT INTO Carros (modelo, cor, ano, preco_venda) VALUES(%s, %s, %s, %s)'
SQL_UPDATE_CARROS = 'UPDATE Carros SET modelo=%s, cor=%s, ano=%s, preco_venda=%s WHERE id_carro=%s'
SQL_DELETE_CARROS = 'DELETE FROM Carros Where id_carro = %s'

class AvaliacaoDao:

    def __init__(self, db):
        self.__db = db

    def create(self, carro):
        cursor = self.__db.connection.cursor()

        if carro.id is None:
            cursor.execute(SQL_INSERT_CARROS,
                   (carro.modelo, carro.cor, carro.ano, carro.preco_venda)
            )
            carro.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_CARROS,
                           (carro.modelo, carro.cor, carro.ano, carro.preco_venda, carro.id)
           )

        self.__db.connection.commit()

        return carro

    def find(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CARROS)
        list = cursor.fetchall()
        carro_list = self.__translate_carros(list)
        return carro_list

    def findOne(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CARROS_ID, (id,))
        tuple = cursor.fetchone()
        cont = self.__translate_carro(tuple)
        return cont

    def __translate_carros(self, list):
        carro_list = []

        for tuple in list:
            cont = self.__translate_carro(tuple)
            carro_list.append(cont)
        return carro_list

    def __translate_carro(self, tuple):
        cont = Carros(tuple[1], tuple[2], tuple[3], tuple[4], tuple[0])
        return cont

    def delete(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_CARROS, (id,))
        self.__db.connection.commit()
        print(f'carro {id} was deleted successfully.')


