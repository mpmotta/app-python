# Captura o nome do aluno
nome = input("Insira o nome do aluno: ")

# Captura as 4 notas do aluno
notas = []
for i in range(4):
    nota = float(input(f"Insira a nota {i+1} do aluno: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / len(notas)

# Determina se o aluno está aprovado ou reprovado
if media >= 7:
    print(f"O(a) aluno(a) {nome} está aprovado(a) com média {media:.1f}.")
else:
    print(f"O(a) aluno(a) {nome} está reprovado(a) com média {media:.1f}.")
