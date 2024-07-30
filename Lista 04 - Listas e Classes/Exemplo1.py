# Escrever a classe Bingo de acordo com o diagrama UML apresentado.
# A classe é utilizada para realizar um jogo de bingo.
# O método Iniciar inicia uma partida, definindo o número de bolas do jogo.
# O método Próximo sorteia uma bola, retornando o seu número (deve ser um valor entre um e o número de bolas ou menos um, caso todas as bolas já tenham sido sorteadas).
# O método Sorteados retorna uma lista com todas as bolas já sorteadas. Insira outros atributos e métodos nas classes, caso necessário.

# Diagrama:
# Bingo
# ----------------
# -numBolas: int
# ----------------
# + numBolas

import random
class Bingo:
    def __init__(self) -> None:
        self.__numBolas = 10
        self.__sorteados = []
    def iniciar(self, numBolas):          # set_num_bolas
        if numBolas > 0:
            self.__numBolas = numBolas
        else:
            raise ValueError("Número de bolas tem que ser positivo")
    def proximo(self):                    # Sorteia uma bola 
        if len(self.__sorteados) == self.__numBolas:
            return "Fim do Jogo"
        n = random.randint(1, self.__numBolas)
        # print("Dentro no método: ", n)
        while n in self.__sorteados:
            n = random.randint(1, self.__numBolas)
            # print("Dentro no método: ", n)
        self.__sorteados.append(n)
        # print(self.__sorteados)
        return n
    def sorteados(self):
        return sorted(self.__sorteados)
    def __str__(self) -> str:
        return f"Foram sorteadas {len(self.__sorteados)} do total de {self.__numBolas} bolar"

class UI:
    @staticmethod
    def menu():
        print("1-Iniciar Jogo, 2-Próximo, 3-Sorteados, 4-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        b = Bingo()
        print("Bem-vindo(a) ao IF Bingo")
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.iniciar_jogo(b)
            if op == 2: UI.proximo(b)
            if op == 3: UI.sorteados(b)
        print("Bye")
    @staticmethod
    def iniciar_jogo(b):
        n = int(input("Informe o número de bolas: "))
        b.iniciar(n)
    @staticmethod
    def proximo(b):
        print(b.proximo())
    @staticmethod
    def sorteados(b):        
        print(b.sorteados())
    def

UI.main()