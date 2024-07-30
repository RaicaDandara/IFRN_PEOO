
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
        n = random.randint(1, self.__numBolas)
        print("Dentro no método: ", n)
        while n in self.__sorteados:
            n = random.randint(1, self.__numBolas)
        self.__sorteados.append(n)
        return n


b = Bingo()
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())