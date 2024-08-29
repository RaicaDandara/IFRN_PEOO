# 3. Uma Conta Bancária

# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo 
# e métodos para realizar as operações de depósito e saque.

# Escrever um programa para testar a classe.

class Conta:
    def __init__(self):
        self.__titular = "x"
        self.__num = 0
        self.__saldo = 0
        self.__valor = 0
    def set_titular(self, pessoa):  
        self__titular = pessoa
    def get_titular(self):         
        return self.__titular
    def set_num(self, num):  
        if num >= 0: 
            self.__num = num
        else:
            raise ValueError("Seu número da conta está incorreto, ele não pode ser negativo")
    def get_num(self):         
        return self.__num
    def set_saldo(self, saldo):  
        if saldo >= 0: 
            self.__saldo = saldo
        else:
            raise ValueError("Você não pode abrir uma conta devendo ao banco")
    def get_saldo(self):         
        return self.__saldo
    def set_valor(self, valor):
        if valor >= 0: 
            self.__valor = valor
        else: 
            raise ValueError("Valor da base não pode ser negativo")
    def get_valor(self):        
        return self.__valor
    def deposito(self):
        return (self.__saldo + self.__valor)
    def saque(self):
        return (self.__saldo - self.__valor)
    
class UI:
    @staticmethod
    def main():
        c = Conta()
        c.set_titular(input("Quem é o titular da conta? "))
        c.set_num(int(input("Qual o número da conta? ")))
        c.set_saldo(float(input("Qual o saldo da sua conta? ")))
        operacao = int(input("Digite 1 para realizar um depósito e 2 para realizar um saque: "))
        if operacao == 1:
                c.set_valor(float(input("Quanto deseja depositar na sua conta? "))) 
                print(f"Seu novo saldo é {c.deposito()} reais")
        if operacao == 2: 
                c.set_valor(float(input("Quanto deseja sacar da sua conta? "))) 
                print(f"Seu novo saldo é {c.saque()} reais")

UI.main() 
