from datetime import timedelta

class Cliente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__limite = 0.0

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            raise ValueError("Digite o nome do Cliente")

    def set_cpf(self, cpf):
        if cpf > 0:
            self.__cpf = cpf
        else:
            raise ValueError("Digite um cpf válido")

    def set_limite(self, limite):
        if limite >= 0:
            self.__limite = limite
        else:
            raise ValueError("O limite não pode ser 0")

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_limite(self):
        return self.__limite

    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__limite}"

class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__Clientes = []
        if nome == "":
            raise ValueError("Informe um nome para a Empresa")

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            raise ValueError("Digite um nome para sua Empresa")

    def get_nome(self):
        return self.__nome

    def inserir(self, m):  # insere um objeto música em um objeto Empresa
        if isinstance(m, Cliente):
            self.__Clientes.append(m)
        else:
            raise ValueError("O item inserido não é um cliente")

    def listar(self):
        return self.__Clientes[:]
    
    def Total(self):
        total = 0
        for cliente in self.__Clientes:
            total += cliente.get_limite()
        return total

    def __str__(self):
        return f"Empresa {self.__nome} tem {len(self.__Clientes)} clientes(s) - Total de crédito: {self.Total()}"

class UI:
    @staticmethod
    def menu():
        print("1-Nova Empresa, 2-Adicionar Cliente, 3-Listar Clientes, 4-Info, 5-Total de Crédito, 6-Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():
        print("Bem-vindo(a) ao IF Música")
        op = 0
        p = None
        while op != 6:
            op = UI.menu()
            if op == 1:
                p = UI.nova_Empresa()
            elif op == 2:
                UI.inserir_Cliente(p)
            elif op == 3:
                UI.listar_Cliente(p)
            elif op == 4:
                UI.info(p)
            elif op == 5:
                UI.Total(p)
        print("Bye")

    @staticmethod
    def nova_Empresa():
        nome = input("Informe o nome da Empresa: ")
        p = Empresa(nome)
        return p

    @staticmethod
    def inserir_Cliente(p):
        nome = input("Informe o nome do cliente: ")
        cpf = int(input("Informe o cpf: "))
        limite = int(input("Informe o limite de crédito do cliente: "))
        m = Cliente()
        m.set_nome(nome)
        m.set_cpf(cpf)
        m.set_limite(limite)
        p.inserir(m)
    @staticmethod
    def listar_Cliente(p):
        print("Clientes cadastrados na Empresa")
        for m in p.listar():
            print(m)
    @staticmethod
    def info(p):
        print(p)
    @staticmethod
    def Total(p):
        print(f"Total de crédito da Empresa '{p.get_nome()}': {p.Total()}")

UI.main()
