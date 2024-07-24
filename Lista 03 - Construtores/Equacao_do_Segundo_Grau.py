class Equacao:
    def __init__(self, a:float, b:float, c:float):
        self.__a = a
        self.__b = b
        self.__c = c
    def set_coeficienteA(self, a):
        if a != 0:
            self.__a = a
        else:
            raise ValueError("O valor de a deve ser diferente de 0 para que seja um equação do segundo grau")
    def get_coeficienteA(self):
        return self.__a
    def set_coeficienteB(self, b):
        if b != "":
            self.__b = b
        else:
            raise ValueError("Digite um número real para o valor de B")
    def get_coeficienteB(self):
        return self.__b
    def set_coeficienteC(self, c):
        if c != "":
            self.__c = c
        else:
            raise ValueError("Digite um número real para o valor de C")
    def get_coeficienteC(self):
        return self.__c
    def Delta(self):
        return (int((self.__b**2) - 4 * self.__a * self.__c))
    def TemRaizesReais(self):
        if Equacao.Delta(self) >= 0:
            return (f"tem raiz real")
        else:
            return (f"não tem raiz real")
    def Raiz1(self):
        if Equacao.Delta(self) >= 0:
            return (((-self.__b) + (Equacao.Delta(self)**(1/2)))/ (2 * self.__a))
        else:
            return (f"não tem raz real")
    def Raiz2(self):
        if Equacao.Delta(self) > 0:
            return (f" e {((-self.__b) - (Equacao.Delta(self)**(1/2)))/ (2 * self.__a)}")
        # Atenção: o filtro não inclui o 0 nessa segunda, pois quando delta = 0, diz-se que só tem 1 raíz, pois ambas são iguais, então achei que não precisava mostrar
        else:
            return (f"")
    def __str__(self):
        return f"Coeficiente A = {self.__a} \nCoeficiente B = {self.__b} \nCoeficiente C = {self.__c}"
    
class UI:
    @staticmethod
    def main():
        a = float(input("Digite o valor do coeficiente a: "))
        b = float(input("Digite o valor do coeficiente b: "))
        c = float(input("Digite o valor do coeficiente c: "))

        x = Equacao(a, b, c)
        print(x)
        print(f"A equação escolhida {x.TemRaizesReais()}, pois o delta é {x.Delta()} e as raízes são: {x.Raiz1()}{x.Raiz2()}")

UI.main()