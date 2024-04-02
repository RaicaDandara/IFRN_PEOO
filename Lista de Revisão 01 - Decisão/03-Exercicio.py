#3. Ler quatro números inteiros, calcular a soma dos números pares e a soma dos números ímpares.
print("Digite qutro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)

totalpar = 0
totalimpar = 0
for x in lista:
    if x % 2 == 0:
        totalpar = totalpar + x
    else:
        totalimpar = totalimpar + x
print(totalpar, totalimpar)
