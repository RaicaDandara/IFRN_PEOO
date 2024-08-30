from datetime import datetime, date

class Paciente:
    def __init__(self, n: str, c: str, t: str, nasc: datetime):
        self.__nome = n
        self.__cpf = c
        self.__telefone = t
        self.__nascimento = nasc
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nascimento(nasc)
    
    def set_nome(self, n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError("Digite um nome para o paciente")
    
    def set_cpf(self, c):
        if c != "":
            self.__cpf = c
        else:
            raise ValueError("Digite um cpf para o paciente")
    
    def set_telefone(self, t):
        if t != "":
            self.__telefone = t
        else:
            raise ValueError("Digite o telefone para contado do paciente")
    
    def set_nascimento(self, nasc):
        try:
            data_nascimento = nasc
            data_hoje = datetime.now()
            if data_nascimento < data_hoje:
                self.__nascimento = data_nascimento
            else:
                raise ValueError("Insira uma data válida e anterior ao dia atual")
        except ValueError:
            raise ValueError("Formato de data inválido. Use o formato dd/mm/aaaa")
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_telefone(self):
        return self.__telefone
    
    def get_nascimento(self):
        return self.__nascimento
    
    def idade(self) -> str:
        hoje = datetime.now()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if meses < 0:
            anos -= 1
            meses += 12
        if hoje.day < self.__nascimento.day:
            meses -= 1
            if meses < 0:
                meses += 12
                anos -= 1
        
        return f"{anos} anos e {meses} meses"

    def __str__(self) -> str:
        return (f"Paciente {self.__nome}\n- CPF: {self.__cpf}\n- Telefone: {self.__telefone}\n- Data de Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}\n- Idade: {self.idade()}")

class UI:
    __pacientes = []

    @staticmethod
    def menu():
        print("1-Novo Paciente \n2-Listar Pacientes \n0-Fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        print("Bem-vindo(a) ao Sistema de Pacientes")
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1:
                UI.novo_paciente()
            elif op == 2:
                UI.listar_pacientes()
        print("Bye")
    
    @staticmethod
    def novo_paciente():
        nome = input("Digite o nome do paciente: ")
        cpf = input("Digite o CPF do paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        nascimento_str = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
        nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
        paciente = Paciente(nome, cpf, telefone, nascimento)
        UI.__pacientes.append(paciente)
    
    @staticmethod
    def listar_pacientes():
        if UI.__pacientes:
            print("\nLISTA DE PACIENTES:")
            for paciente in UI.__pacientes:
                print(paciente)
                print("-" * 40)
        else:
            print("Nenhum paciente cadastrado.")

UI.main()
