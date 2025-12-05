import mysql.connector
from avaliacao.dao.AvaliacaoDao import AvaliacaoDao
from avaliacao.model.carros import Carros

if __name__ == '__main__':

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='avaliacao_db'
        )

        dao = AvaliacaoDao(connection)


        # criar carro
        carro = Carros('Palio', 'Preto', 100, 1000.00)
        carro1 = Carros('Punto', 'Cinza', 200, 2000.00)
        carro2 = Carros('Uno', 'Vermelho', 300, 3000.00)

        carroSalvo = dao.create(carro)
        print(carroSalvo)

        # atualizar carro
        carro = Carros('Palio', 'Branco', 100, 1000.00, 1)
        carroEditado = dao.create(carro)
        print(carroEditado)

        # listar carros
        lista_carros = dao.find()

        # listar por id
        carros = dao.findOne(1)
        print(carro.modelo, carro.cor, carro.ano, carro.preco_venda, carro.id)

        # deletar
        dao.delete(3)
    except Exception as e:
        print(e)
