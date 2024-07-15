# 1. Círculo

# A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área 
# e sua circunferência.

#Escrever um programa para testar a classe.

class Circulo:
    def __init__(self):
        self.r = 0
        self.pi = 0
    def calc_area(self):
        return (self.r * self.pi**2)
    
x = Circulo()
x.r = float(input("digite o raio do círculo: "))
x.pi = 3.1415
print(x.calc_area())

# 2. Uma Viagem

# A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem
# realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de 
# acordo com a distância e o tempo gasto.

#Escrever um programa para testar a classe.

class Viagem:
    def __init__(self):
        self.d = 0
        self.h = 0
        self.m = 0
    def calc_velmed(self):
        return (self.d/(self.h + (self.m/60)))

v = Viagem()
v.d = float(input("Digite a distância percorrida: "))
v.h = float(input("Digite a quantidade de horas da viagem: "))
v.m = float(input("Digite a quantidade de minutos da viagem: "))
print(v.calc_velmed())

# 3. Uma Conta Bancária

# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo 
# e métodos para realizar as operações de depósito e saque.

# Escrever um programa para testar a classe.

class Conta:
    def __init__(self):
        self.titular = "x"
        self.num = 0
        self.saldo = 0
        self.valor = 0
    def deposito(self):
        return (self.saldo + self.valor)
    def saque(self):
        return (self.saldo - self.valor)
    
c = Conta()
c.titular = input("Quem é o titular da conta? ")
c.num = int(input("Qual o número da conta? "))
c.saldo = float(input("Qual o saldo da sua conta? "))
operacao = int(input("Digite 1 para realizar um depósito e 2 para realizar um saque: "))
if (operacao == 1):
    c.valor = float(input("Quanto deseja depositar? "))
    print(c.deposito())
elif (operacao == 2):
    c.valor = float(input("Quanto deseja sacar? "))
    print(c.saque())
else:
    print("Operação não reconhecida, tente novamente")
    
# 4. Uma Entrada de Cinema
# A classe deve ter atributos para armazenar o dia e o horário de uma sessão de cinema e métodos para 
# calcular o valor da entrada inteira e da meia-entrada.

# O valor das entradas deve ser calculado com base nas seguintes regras:
#   • Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.
#   • Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.
#   • Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
#   • Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.

# Escrever um programa para testar a classe.

class Cinema:
    def __init__(self):
        self.d = "nenhum"
        self.h = 0
        self.ingresso = 8
        self.variacao = 0
        self.acrescimo = 0
    def calc_ingresso(self):
        return ((self.ingresso + self.variacao) * self.acrescimo)
    
f = Cinema()
f.d = input("Quando deseja ver o filme? ")
f.h = int(input("Em qual horário quer assistir? "))

if (f.d == "segunda") or (f.d == "terça") or (f.d == "quinta"):
    if (f.h <= 17 and f.h != 0):
        f.variacao = 8
        f.acrescimo = 1
        print(f.calc_ingresso())
    else:
        f.variacao = 8
        f.acrescimo = 1.5
        print(f.calc_ingresso())
elif (f.d == "quarta"):
    f.variacao = 0
    f.acrescimo = 1
    print(f.calc_ingresso())

elif (f.d == "sexta") or (f.d == "sábado") or (f.d == "domingo"):
    if (f.h <= 17 and f.h != 0):
        f.variacao = 12
        f.acrescimo = 1
        print(f.calc_ingresso())
    else:
        f.variacao = 12 
        f.acrescimo = 1.5
        print(f.calc_ingresso())
