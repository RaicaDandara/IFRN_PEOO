# O encapsulamento visa filtrar o que será selecionado

class Triangulo:                    # Entidade
    def __init__(self):             # Contrutor
        # self.b = 0                # Atributos
        self.__b = 0                # Atributos Encapsulado
        self.__h = 0
    def set_base(self, valor):      # armazenar um valor, ates é feita a varredura/verificação
        if valor >= 0:
            self.__b = valor
        else:
            raise ValueError()
        # ou raise ValueError("Valor da base não pode ser nagativo") - raise ValueError pode conter/passar uma mensagem
    def get_base(self):             # retornar um valor
        return self.__b
    def set_altura(self, valor):
        if valor >= 0:
            self.__h = valor
        else:
            raise ValueError()
            # ou raise ValueError("Valor da altura não pode ser nagativo") - raise ValueError pode conter/passar uma mensagem
    def get_altura(self):
        return self.__h
    def calc_area(self):            # métodos = operação -> método de instância
        return (self.__b * self.__h/2)

    
class UI:                           # Interface com o usuário
    @staticmethod                   # prints e inputs nessa classe
    def main():                     # operação principal da UI -> método de cla
        # Quando a classe segue de () ele chama o init
        x = Triangulo()
        # Sem encapsulamento - acesso direto ao atributo
        # qualquer valor é armazenado
        # x.__b = float(input("Informe o valor da base: "))
        # x.__h = float(input("Informe o valor da altura: "))

        # Com encapsulamento - acesso indireto ao atributo
        x.set_base = (float(input("Informe o valor da base: ")))
        x.set_altura = (float(input("Informe o valor da altura: ")))
        print(f"A base do triângulo é {x.get_base()}")
        print(f"A altura do triângulo é {x.get_altura()}")
        print(f"A área do triângulo é {x.calc_area()}")

UI.main()                           # rodar o programa
