# 12. Ler uma string com dois valores inteiros positivos entre um operador ( +, –, * ou / ) e calcular o resultado da operação matemática utilizando estes valores e o operador.
s = input()
lista = s.split("+") #Tentativa de separar
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a+b)
lista = s.split("-") #Tentativa de separar
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a-b)
lista = s.split("*") #Tentativa de separar
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a*b)
lista = s.split("/") #Tentativa de separar
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a/b)
