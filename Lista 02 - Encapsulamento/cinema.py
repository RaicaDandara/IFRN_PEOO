class Cinema:
    def __init__(self):
        self.__d = "nenhum"
        self.__h = 0
    def set_dia (self, dia):
        d = dia.split("-")
        self.__d = str(d[0])
    def get_dia (self):
        return self.__d
    def set_hora (self, sessão):
        if sessão <= 25 and sessão >= 0:
            self.__h = sessão
        else:
            raise ValueError("Insira uma sessão válida no formato 24h")
    def get_hora (self):
        return self.__h
    def calc_ingresso(self):
        if (self.__d == "segunda" or self.__d == "terça" or self.__d == "quinta") and self.__h <= 16:
            return ((16 + 0) * 1)
        elif (self.__d == "segunda" or self.__d == "terça" or self.__d == "quinta") and self.__h >= 17:
            return ((16 + 0) * 1.5)
        if self.__d == "quarta":
            return ("somente meia entrada")
        elif (self.__d == "sexta" or self.__d == "sábado" or self.__d == "domingo") and self.__h <= 16:
            return ((16 + 4) * 1)
        elif (self.__d == "sexta" or self.__d == "sábado" or self.__d == "domingo") and self.__h >= 17:
            return ((16 + 4) * 1.5)
    def calc_meia_entrada(self):
        if (self.__d == "segunda" or self.__d == "terça" or self.__d == "quinta") and self.__h <= 16:
            return ((16 + 0) * 0.5)
        elif (self.__d == "segunda" or self.__d == "terça" or self.__d == "quinta") and self.__h >= 17:
            return (((16 + 0) * 1.5) * 0.5)
        elif self.__d == "quarta":
            return ((16 + 0) * 0.5)
        elif (self.__d == "sexta" or self.__d == "sábado" or self.__d == "domingo") and self.__h <= 16:
            return ((16 + 4) * 0.5)
        elif (self.__d == "sexta" or self.__d == "sábado" or self.__d == "domingo") and self.__h >= 17:
            return (((16 + 4) * 1.5) * 0.5)

class UI:
    @staticmethod
    def main():
        f = Cinema()
        f.set_dia(input("Quando deseja ver o filme? "))
        f.set_hora(int(input("Em qual horário quer assistir? (formato 24h)")))

        print(f"Entrada inteira: {f.calc_ingresso()}")
        print(f"Meia entrada: {f.calc_meia_entrada()}")

UI.main()    
