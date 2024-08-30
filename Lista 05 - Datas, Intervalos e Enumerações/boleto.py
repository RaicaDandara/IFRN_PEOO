from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = "Em Aberto"
    PAGO_PARCIAL = "Pago Parcial"
    PAGO = "Pago"

class Boleto:
    def __init__(self, codbarras, data_emissao, data_vencimento, valor):
        self.__codbarras = codbarras
        self.__dateEmissao = datetime.strptime(data_emissao, '%d/%m/%Y')
        self.__dataVencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')
        self.__valorBoleto = valor
        self.__valorPago = 0.0
        self.__situacaoPagamento = Pagamento.EM_ABERTO
        self.__dataPagto = None
    def get_codbarras(self):
        return self.__codbarras
    def get_dateEmissao(self):
        return self.__dateEmissao.strftime('%d/%m/%Y')
    def set_dateEmissao(self, data_emissao):
        self.__dateEmissao = datetime.strptime(data_emissao, '%d/%m/%Y')
    def set_codbarras(self, codbarras):
        self.__codbarras = codbarras
    def get_dataVencimento(self):
        return self.__dataVencimento.strftime('%d/%m/%Y')
    def set_dataVencimento(self, data_vencimento):
        self.__dataVencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')
    def get_valorBoleto(self):
        return self.__valorBoleto
    def set_valorBoleto(self, valor):
        self.__valorBoleto = valor
    def get_dataPagto(self):
        if self.__dataPagto:
            return self.__dataPagto.strftime('%d/%m/%Y')
        else:
            return None

    def set_dataPagto(self, data_pago):
        self.__data_pago = datetime.strptime(data_pago, '%d/%m/%Y')
    
    def pagar(self, valor):
        self.__valorPago += valor
        if self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.PAGO_PARCIAL
        else:
            self.__situacaoPagamento = Pagamento.PAGO
    
    def situacao(self):
        return self.__situacaoPagamento.value
    
    def __str__(self):
        return (f"Boleto: {self.__codbarras}, Emissão: {self.get_dateEmissao()}, "
                f"Vencimento: {self.get_dataVencimento()}, Valor: {self.__valorBoleto}, "
                f"Valor Pago: {self.__valorPago}, Data Pago: {self.get_dataPagto()}, "
                f"Situação: {self.situacao()}")

class UI:
    __boletos = []  # Mover o atributo __boletos para ser um atributo de classe

    @staticmethod
    def criar_boleto():
        codigo_barras = input("Digite o código de barras do boleto: ")
        data_emissao = input("Digite a data de emissão (dd/mm/yyyy): ")
        data_vencimento = input("Digite a data de vencimento (dd/mm/yyyy): ")
        valor = float(input("Digite o valor do boleto: "))

        novo_boleto = Boleto(codigo_barras, data_emissao, data_vencimento, valor)
        UI.__boletos.append(novo_boleto)  # Adiciona o boleto criado à lista de boletos
        print("Boleto criado com sucesso!")

    @staticmethod
    def buscar_boleto(codigo_barras):
        for boleto in UI.__boletos:
            if boleto.get_codbarras() == codigo_barras:
                return boleto
        return None

    @staticmethod
    def pagar_boleto():
        codigo_barras = input("Digite o código de barras do boleto que deseja pagar: ")
        boleto = UI.buscar_boleto(codigo_barras)
        if boleto:
            valor_pagamento = float(input("Digite o valor a ser pago: "))
            data_pagamento = input("Digite a data de pagamento (dd/mm/yyyy): ")
            boleto.set_dataPagto(data_pagamento)
            boleto.pagar(valor_pagamento)
            print("Pagamento realizado com sucesso!")
        else:
            print("Boleto não encontrado.")

    @staticmethod
    def menu():
        print("\n===== Sistema de Gerenciamento de Boletos =====")
        print("1. Criar novo boleto")
        print("2. Pagar boleto")
        print("3. Listar todos os boletos")
        print("4. Exibir detalhes de um boleto")
        print("5. Sair")

        return int(input("Selecione uma opção: "))
    @staticmethod
    def exibir_boleto():
        codigo_barras = input("Digite o código de barras do boleto que deseja exibir: ")
        boleto = UI.buscar_boleto(codigo_barras)
        if boleto:
            print(boleto)
        else:
            print("Boleto não encontrado.")
    @staticmethod
    def listar_boletos():
        if UI.__boletos:
            for boleto in UI.__boletos:
                print(boleto)
        else:
            print("Nenhum boleto encontrado.")
    @staticmethod
    def main():
        op = -1
        while op != 5:
            op = UI.menu()
            if op == 1:
                UI.criar_boleto()
            elif op == 2:
                UI.pagar_boleto()
            elif op == 3:
                UI.listar_boletos()
            elif op == 4:
                UI.exibir_boleto()
            elif op != 5:
                print("Opção inválida. Tente novamente.")
        print("Saindo do sistema. Até logo!")


# Executa o sistema
UI.main()
