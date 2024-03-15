# 2. Ler quatro valores inteiros, calcular e mostrar a média aritmética entre eles. Mostrar também os números menores e os números maiores ou iguais à média.
print("Digite quatro valores")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = (a, b, c, d)/4
print("Média =", m)
print("Números menores que a média")
if a < m:
    print(a)
if b < m:
    print(b)
if c < m:
    print(c)
if d < m:
    print(d)

print("Números maiores ou guais a média")
if a >= m:
    print(a)
if b >= m:
    print(b)
if c >= m:
    print(c)
if d >= m:
    print(d)