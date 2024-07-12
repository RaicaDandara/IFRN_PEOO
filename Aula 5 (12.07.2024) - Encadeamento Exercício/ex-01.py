class Corrida:
    def __init__(self):
        self.__distancia = 1 #metros
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0
    def set_distancia (self, distancia):
        if distancia > 0: 
            self.__distancia = distancia #validação
        else:
            raise ValueError("Distância deve ser positiva")
    def get_distancia(self):
        return self.__distancia
    def set_tempo(self, tempo):
        t = tempo.split(":")
        self.__horas = int(t[0])
        self.__minutos = int(t[1])
        self.__segundos = int(t[2])
        if self.__horas < 0 or self.__minutos < 0 or self.__segundos < 0 or self.__horas + self.__minutos + self.__segundos == 0:
            raise ValueError("Valor do tempo informado é inválido")
    def get_tempo(self):
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"    
    def pace(self):
        t = self.__horas * 60 + self.__minutos + self.__segundos / 60
        d = self.__distancia / 1000
        return t/d 
    
    class Triangulo:              
        def __init__(self):       
            self.__b = 0          
            self.__h = 0
        def set_base(self, valor):  
            if valor >= 0: self.__b = valor
            else: raise ValueError("Valor da base não pode ser negativo")
        def get_base(self):         
            return self.__b
        def set_altura(self, valor):
            if valor >= 0: self.__h = valor
            else: raise ValueError("Valor da altura não pode ser negativo")
        def get_altura(self):    
            return self.__h
        def calc_area(self):      
            return self.__b * self.__h / 2

    class UI:
        @staticmethod
        def menu():
            print("1 - Corrida, 2 - Triangulo, 3 - Fim")
            return int(input("Escolha uma opção: "))
        @staticmethod
        def main():
            op = 0
            while op != 3:
                op = UI.menu()
                if op == 1: UI.nova_corrida()
                if op == 2: UI.novo_triangulo()
        @staticmethod
        def nova_corrida():
            c = Corrida() 
            distancia = float(input("Informe a distância em metros: "))
            tempo = input("Informe o tempo no formato 'h:m:s': ")
            c.set_distancia(distancia)
            c.set_tempo(tempo)
            print(f"Seu pace é de {c.pace()} minutos/km")
        @staticmethod
        def novo_triangulo():
            x = Triangulo()
            x.set_base(float(input("Informe o valor da base: ")))
            x.set_altura(float(input("Informe o valor da altura: ")))
            print(f"A base do triângulo é {x.get_base()}")
            print(f"A altura do triângulo é {x.get_altura()}")
            print(f"A área do triângulo é {x.calc_area()}")

UI.main()