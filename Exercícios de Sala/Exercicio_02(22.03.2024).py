#2. Ler nome e matrícula de 10 alunos e mostrar nome, matrícula e ano de ingresso no IFRN de cada aluno
continuar = True
alunos = []
matriculas = []
anos = []
while continuar:
    print("Digite o nome do aluno: ")
    nome = input()
    alunos.append(nome)
    print("Digite a matrícula do aluno: ")
    matri = input()
    matriculas.append(matri)
    ano = matri[0:4]
    anos.append(ano)
    print("Deseja continuar? (s/n)")
    x = input()
    if x == "s":
        continuar = True
    else:
        continuar = False
n = 0
for x in alunos:
    print(x, matriculas[n], anos[n])
    n = n + 1

# ou 

n = []
m = []
for k in range(10):
    nome = input("Informe seu nome: ")
    matri = input("Informe sua matrícula: ")
    n.append(nome)
    m.append(matri)
for k in range(10):
    matri = m[k]
    ano = int(matri[0:4]) #ano = int(m[k][0:4])
    print(f"O aluno(a) {n[k]} cuja matrícula é {m[k]} ingressou no IFRN no ano de {ano}")
