# 11. Ler uma string, calcular e mostrar a soma dos caracteres que são algarismos.
print("Digite um frase")
s = input()
total = 0
for x in s:
    if "0" <= x <= "9":
        total = total + x
print(total)
