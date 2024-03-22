#1. Ler nome e matrícula de 1 aluno e mostrar nome, matrícula e ano de ingresso no IFRN 
# # Lembrando: 2024101111#### -> Ano = 2024, semestre = 1, curso = 01111, contador = ### 
print("Digite seu nome: ") 
nome = input() 
print("Digite sua matrícula: ") 
matri = input() 
print("O aluno(a)", nome, "cuja matrícula é", matri, "ingressou no IFRN no ano de", matri[0:4])

# ou

print("Digite seu nome: ") 
nome = input() 
print("Digite sua matrícula: ") 
matri = input() 
ano = int(matri[0:4])
print("O aluno(a)", nome, "cuja matrícula é", matri, "ingressou no IFRN no ano de", ano)
