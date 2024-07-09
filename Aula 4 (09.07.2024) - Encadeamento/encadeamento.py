# O encapsulamento visa filtrar o que será selecionado

class Triangulo:                    # Entidade
    def __init__(self):             # Contrutor
        self.__b = 0                  # Atributos
        self.__h = 0
    def set_base(self, valor):
        if valor >= 0:
            self.__b = valor
    def get_base(self):
        return self.__b
    def set_altura(self, valor):
        if valor >= 0:
            self.__h = valor
    def get_altura(self):
        return self.__h
    def calc_area(self):            # métodos = operação -> método de instância
        return (self.__b * self.__h/2)

    
class UI:                           # Interface com o usuário
    @staticmethod                   # prints e inputs nessa classe
    def main():                     # operação principal da UI -> método de cla
        x = Triangulo()
        # Sem encapsulamento
        # x.__b = float(input("Informe o valor da base: "))
        # x.__h = float(input("Informe o valor da altura: "))
        x.set_base = (float(input("Informe o valor da base: ")))
        x.set_altura = (float(input("Informe o valor da altura: ")))
        print(f"A base do triângulo é {x.get_base()}")
        print(f"A altura do triângulo é {x.get_altura()}")
        print(f"A área do triângulo é {x.calc_area()}")

UI.main()                           # rodar o programa
