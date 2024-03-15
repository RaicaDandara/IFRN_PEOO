#1. Ler dois valores inteiros e imprimir o maior deles, ou a mensagem "Números iguais", se forem iguais.
a = int(input())
b = int(input())
# solução 1 - usando max
if a == b:
    print("Os número sõ iguais")
else:
    print("Maior =", max(a,b))

# solução 2 - sem max
if a == b:
    print("Os número sõ iguais")
else:
    if a > b:
        print("Maior =", a)
    else:
        print("Maior =", b)