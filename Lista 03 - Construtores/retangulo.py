class Retangulo:
    def __init__(self, b: float, h: float):
        self.__b = b
        self.__h = h
    def set_base(self, b):
        if b >= 0:
            self.__b = b
        else:
            raise ValueError("O valor da base não pode ser negativo")
    def get_base(self):
        return self.__b
    def set_altura(self, h):
        if h >= 0:
            self.__h = h
        else:
            raise ValueError("O valor da altura não pode ser negativo")
    def get_altura(self):
        return self.__h
    def calcArea(self):
        return (self.__h * self.__b)
    def calcDiagonal(self):
        return ((self.__b**2 + self.__h**2)**(1/2))
    def __str__(self):
        return f"Base = {self.__b} \nAltura = {self.__h}"

class UI:
    @staticmethod
    def main():
        base = float(input("Digite o valor da base do retângulo: "))
        altura = float(input("Digite o valor da altura do retângulo: "))
        x = Retangulo(base, altura)
        print(x)
        print(f"A área do seu retângulo é: {x.calcArea()} \nA diagonal do seu triângulo é: {x.calcDiagonal()}")

UI.main()