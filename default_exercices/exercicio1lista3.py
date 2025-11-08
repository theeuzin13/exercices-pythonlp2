from datetime import datetime
from abc import ABC, abstractmethod

class Veiculo(ABC):
      def __init__(self, numero_serie, data_manutencao=None):
            self.numero_serie = numero_serie
            self.data_manutencao = data_manutencao or datetime.now()
            self.quilometragem = 0
      
      @abstractmethod
      def __str__(self):
            pass

class Bicicleta(Veiculo):
      def __init__(self, numero_serie, tipo_modelo, data_manutencao=None):
            super().__init__(numero_serie, data_manutencao)
            self.tipo_modelo = tipo_modelo  # "estrada" ou "trilha"
      
      def __str__(self):
            return f"Bicicleta - Série: {self.numero_serie}, Modelo: {self.tipo_modelo}, Manutenção: {self.data_manutencao.strftime('%d/%m/%Y')}"

class Motocicleta(Veiculo):
      def __init__(self, numero_serie, cilindradas, data_manutencao=None):
            super().__init__(numero_serie, data_manutencao)
            self.cilindradas = cilindradas
            self.km_ultima_troca_pneus = 0
      
      def trocar_pneus(self):
            self.km_ultima_troca_pneus = self.quilometragem
            print(f"Pneus trocados na quilometragem: {self.quilometragem} km")
      
      def verificar_troca_pneus(self, limite_km=10000):
            km_desde_troca = self.quilometragem - self.km_ultima_troca_pneus
            if km_desde_troca >= limite_km:
                  print(f"Atenção: Pneus precisam ser trocados! ({km_desde_troca} km desde a última troca)")
                  return True
            return False
      
      def __str__(self):
            return f"Motocicleta - Série: {self.numero_serie}, Cilindradas: {self.cilindradas}cc, Quilometragem: {self.quilometragem} km, Manutenção: {self.data_manutencao.strftime('%d/%m/%Y')}"

class Automovel(Veiculo):
      def __init__(self, numero_serie, data_manutencao=None):
            super().__init__(numero_serie, data_manutencao)
            self.km_ultima_troca_pneus = 0
            self.km_ultima_troca_oleo = 0
      
      def trocar_pneus(self):
            self.km_ultima_troca_pneus = self.quilometragem
            print(f"Pneus trocados na quilometragem: {self.quilometragem} km")
      
      def trocar_oleo(self):
            self.km_ultima_troca_oleo = self.quilometragem
            print(f"Óleo trocado na quilometragem: {self.quilometragem} km")
      
      def verificar_manutencao(self, limite_pneus=40000, limite_oleo=10000):
            km_desde_troca_pneus = self.quilometragem - self.km_ultima_troca_pneus
            km_desde_troca_oleo = self.quilometragem - self.km_ultima_troca_oleo
            
            if km_desde_troca_pneus >= limite_pneus:
                  print(f"Atenção: Pneus precisam ser trocados! ({km_desde_troca_pneus} km desde a última troca)")
            
            if km_desde_troca_oleo >= limite_oleo:
                  print(f"Atenção: Óleo precisa ser trocado! ({km_desde_troca_oleo} km desde a última troca)")
      
      def __str__(self):
            return f"Automóvel - Série: {self.numero_serie}, Quilometragem: {self.quilometragem} km, Manutenção: {self.data_manutencao.strftime('%d/%m/%Y')}"

if __name__ == "__main__":
      bicicleta = Bicicleta("B001", "estrada")
      moto = Motocicleta("M001", 250)
      carro = Automovel("A001")
      
      print(bicicleta)
      print(moto)
      print(carro)
      
      moto.quilometragem = 12000
      moto.verificar_troca_pneus()
      
      carro.quilometragem = 15000
      carro.verificar_manutencao()