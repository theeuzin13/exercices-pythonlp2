#Uma interface é um contrato que define assinaturas de métodos
#que devem ser implementados pelas classes que assinarem esse contrato.

import abc
class persistencia_interface(abc.ABC):
    @abc.abstractmethod
    def create(self, carro):
        pass
    @abc.abstractmethod
    def find(self):
        pass

    @abc.abstractmethod
    def findOne(self, id):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

