# 10. Ler uma frase e mostrar as strings obtidas a partir desta, passando uma a uma a letra inicial para o final, até que a frase inicial seja apresentada.
# Exemplo:

# Digite uma frase:
# Brasil

# rasilB
# asilBr
# silBra
# ilBras
# lBrasi
# Brasil


print("Digite uma frase")
frase = input()

for x in range(len(frase)):
    frase = frase[1:] + frase[0]
    print(frase)
