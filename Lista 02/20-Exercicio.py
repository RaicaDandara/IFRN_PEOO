# Mostrar a sequência de números abaixo.

# Resultado: 
# 1
# 2 2
# 3 2
# 4 2 4
# 5 2 4
# 6 2 4 6
# ...
# 10 2 4 6 8 10


for n in range(1,11):
    for k in range(1, n+1):
        if k % 2 == 0:
            print(k, end=" ")
    print()
