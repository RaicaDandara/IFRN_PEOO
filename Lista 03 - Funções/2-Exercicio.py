# 2. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o primeiro nome da pessoa. [com split()]
nome = input("Digite seu nome completo: ")
p = nome.split()
print("Bem-vindo ao Python,", p[0])

# 2. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o primeiro nome da pessoa. Sem usar split()
nome = input("Digite seu nome completo: ")
k = nome.index(" ")
print("Bem-vindo ao Python,", nome[0:k])
