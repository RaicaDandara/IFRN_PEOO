import json
from datetime import datetime


class Medicamento:
    def __init__(self, id_medicamento, nome, validade, preco):
        self.__id_medicamento = id_medicamento
        self.__nome = nome
        self.__validade = datetime.strptime(validade, "%d/%m/%Y")
        self.__preco = float(preco)

    def __str__(self):
        validade_str = self.__validade.strftime("%d/%m/%Y")
        return f"ID: {self.__id_medicamento}, Nome: {self.__nome}, Validade: {validade_str}, Preço: R$ {self.__preco:.2f}"

    def is_vencido(self):
        return self.__validade < datetime.now()

    # Métodos getters e setters
    def get_id(self):
        return self.__id_medicamento

    def set_nome(self, nome):
        if nome:
            self.__nome = nome

    def set_validade(self, validade):
        if validade:
            self.__validade = datetime.strptime(validade, "%d/%m/%Y")

    def set_preco(self, preco):
        if preco:
            self.__preco = float(preco)

    def to_dict(self):
        """Converte o objeto em um dicionário para serialização JSON."""
        return {
            "id_medicamento": self.__id_medicamento,
            "nome": self.__nome,
            "validade": self.__validade.strftime("%d/%m/%Y"),
            "preco": self.__preco
        }



class Medicamentos:
    lista = []

    @classmethod
    def inserir(cls, medicamento):
        cls.abrir()  # Carrega os medicamentos
        max_id = max((med.get_id() for med in cls.lista), default=0)
        # Configurando o ID do medicamento
        medicamento._Medicamento__id_medicamento = max_id + 1
        cls.lista.append(medicamento)
        cls.salvar()  # Salva a lista atualizada

    @classmethod
    def listar(cls):
        cls.abrir()  # Passando o arquivo correto
        return cls.lista

    @classmethod
    def listar_por_id(cls, id_medicamento):
        cls.abrir()  # Passando o arquivo correto
        for medicamento in cls.lista:
            if medicamento.get_id() == id_medicamento:
                return medicamento
        return None

    @classmethod
    def atualizar(cls, id_medicamento, nome, validade, preco):
        cls.abrir()  # Passando o arquivo correto
        medicamento = cls.listar_por_id(id_medicamento)
        if medicamento:
            medicamento.set_nome(nome)
            medicamento.set_validade(validade)
            medicamento.set_preco(preco)
            cls.salvar()
            return True
        return False

    @classmethod
    def excluir(cls, id_medicamento):
        cls.abrir()  # Passando o arquivo correto
        medicamento = cls.listar_por_id(id_medicamento)
        if medicamento:
            cls.lista.remove(medicamento)
            cls.salvar()
            return True
        return False

    @classmethod
    def vencidos(cls):
        cls.abrir()  # Passando o arquivo correto
        return [med for med in cls.lista if med.is_vencido()]

    @classmethod
    def salvar(cls):
        with open("farmacia.json", mode="w") as arquivo:
            json.dump(
                [med.to_dict() for med in cls.lista],  # Usando o método to_dict()
                arquivo,
                indent=4  # Adiciona formatação ao JSON
            )

    @classmethod
    def abrir(cls):
        cls.lista = []
        try:
            with open("farmacia.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                cls.lista = [
                    Medicamento(
                        d["id_medicamento"],
                        d["nome"],
                        d["validade"],
                        d["preco"]
                    )
                    for d in dados
                ]
        except FileNotFoundError:
            cls.lista = []


class UI:
    @staticmethod
    def menu():
        print("\nMenu:")
        print("1 - Listar medicamentos")
        print("2 - Inserir medicamento")
        print("3 - Atualizar medicamento")
        print("4 - Excluir medicamento")
        print("5 - Listar medicamentos vencidos")
        print("6 - Sair")

    @staticmethod
    def listar():
        medicamentos = Medicamentos.listar()
        if medicamentos:
            for med in medicamentos:
                print(med)
        else:
            print("Nenhum medicamento cadastrado.")

    @staticmethod
    def inserir():
        nome = input("Nome do medicamento: ")
        validade = input("Validade (dd/mm/yyyy): ")
        preco = input("Preço: ")
        try:
            medicamento = Medicamento(None, nome, validade, preco)
            Medicamentos.inserir(medicamento)
            print("\nMedicamento inserido com sucesso!")
        except ValueError as e:
            print(f"\nErro ao inserir medicamento: {e}")

    @staticmethod
    def atualizar():
        id_medicamento = int(input("ID do medicamento a atualizar: "))
        nome = input("Novo nome: ")
        validade = input("Nova validade (dd/mm/yyyy): ")
        preco = float(input("Novo preço: "))
        if Medicamentos.atualizar(id_medicamento, nome, validade, preco):
            print("Medicamento atualizado com sucesso!")
        else:
            print("Medicamento não encontrado.")

    @staticmethod
    def excluir():
        id_medicamento = int(input("ID do medicamento a excluir: "))
        if Medicamentos.excluir(id_medicamento):
            print("Medicamento excluído com sucesso!")
        else:
            print("Medicamento não encontrado.")

    @staticmethod
    def vencidos():
        vencidos = Medicamentos.vencidos()
        if vencidos:
            print("\nMedicamentos vencidos:")
            for med in vencidos:
                print(med)
        else:
            print("\nNenhum medicamento vencido.")

    @staticmethod
    def main():
        Medicamentos.abrir()  # Agora sem passar o nome do arquivo
        while True:
            UI.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                UI.listar()
            elif opcao == '2':
                UI.inserir()
            elif opcao == '3':
                UI.atualizar()
            elif opcao == '4':
                UI.excluir()
            elif opcao == '5':
                UI.vencidos()
            elif opcao == '6':
                Medicamentos.salvar()
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    UI.main()
