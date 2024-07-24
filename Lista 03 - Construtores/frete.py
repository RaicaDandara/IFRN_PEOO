class Frete:
    def __init__(self, d: float, p: float):
        self.__distancia = d
        self.__peso = p
    def setDistancia(self, d):
        if d >= 0:
            self.__distancia = d
        else:
            raise ValueError("A distância não pode ser um valor negativo")
    def getDistancia(self):
        return self.__distancia
    def setPeso(self, p):
        if p >= 0:
            self.__peso = p
        else:
            raise ValueError("O peso não pode ser um valor negativo")
    def getPeso(self):
        return self.__peso
    def calcFrete(self):
        return (0.01 * self.__peso * self.__distancia)
    def __str__(self) -> str:
        return f"Peso da encomenda = {self.__peso} \nDistância para a entrega = {self.__distancia}"


class UI:
    @staticmethod
    def main():
        peso = float(input("Digite o peso da encomenda: "))
        distancia = float(input("Digite a distância do armazém até seu endereço: "))
        x = Frete(distancia, peso)    
        print(x)
        print(f"O valor do frete a ser pago é R$ {x.calcFrete()}")

UI.main()