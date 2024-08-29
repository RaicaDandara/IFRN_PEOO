# 2. Uma Viagem

# A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem
# realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de 
# acordo com a distância e o tempo gasto.

#Escrever um programa para testar a classe.

class Viagem:
    def __init__(self):
        self.__d = 0
        self.__h = 0
        self.__m = 0
    def set_distancia (self, distancia):
        if distancia >= 0:
            self.__d = distancia
        else:
            raise ValueError("A distância não pode ser negativa")
    def get_distancia (self):
        return self.__d
    def set_tempo (self, tempo):
         t = tempo.split(":")
         self.__h = int(t[0])
         self.__m = int(t[1])
         if self.__h < 0 or self.__m < 0 or self.__h + self.__m == 0:
            raise ValueError("Valor do tempo informado é inválido")
    def get_tempo (self):
        return f"{self.__h}:{self.__m}" 
    def calc_velmed(self):
        return (self.__d/(self.__h + (self.__m/60)))

class UI:
    @staticmethod
    def main():
        c = Viagem() 
        c.set_distancia(float(input("Informe a distância em km: ")))
        c.set_tempo((input("Informe o tempo no formato 'h:m': ")))
        print(f"Sua velocidade média é de {c.calc_velmed()} km/h")

UI.main()
