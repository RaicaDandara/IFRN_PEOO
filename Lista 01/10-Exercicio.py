# 10. Ler uma data no formato "dd/mm/aaaa" e verificar se é uma data válida, considerando como válidos os anos entre 1900 e 2100, meses de 1 a 12 e dias de acordo com o mês.
print("Digite uma data no formato dd/mm/aaaa")
data = input()
dia, mes, ano = data.split("/")
d = int(dia)
m = int(mes)
a = int(ano)
maior = 31
if m == 4 or m == 6 or m == 9 or m == 11: 
    maior = 30
if m == 2:
    if a % 4 == 0 and a % 100 != 0 and a % 400 == 0:
        maior = 29
    else:
        maior = 28

if a >= 1900 and a<= 2100 and m>=1 and d>=1 and d<=maior:
    print("A data é válida")
else:
    print("A data é inválida")
