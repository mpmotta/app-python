# Captura o nome do aluno
nome = input("Insira o nome do aluno: ")

# Captura as 4 notas do aluno
notas = []
for i in range(4):
    nota = float(input(f"Insira a nota {i+1} do aluno: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / len(notas)

# Exibe o resultado
print(f"O aluno {nome} tem média {media:.2f}")
