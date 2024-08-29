# 1. Círculo

# A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área 
# e sua circunferência.

#Escrever um programa para testar a classe.

class Circulo:
    def __init__(self):
        self.__r = 0
        self.__pi = 3.1415
    def set_raio (self, raio):
        if raio >= 0: 
            self.__r = raio
        else: 
            raise ValueError("Valor do raio não pode ser negativo")
    def get_raio(self):         
        return self.__r
    def calc_area(self):
        return (self.__pi * self.__r**2)
    
class UI:                     
    @staticmethod             
    def main():               
        x = Circulo()
        x.set_raio(float(input("Informe o valor da base: ")))
        
        print(f"A o raio do círculo é {x.get_raio()}")

        print(f"A área do círculo é {x.calc_area()}")

UI.main()                         
