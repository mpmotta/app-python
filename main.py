# Captura o nome do aluno
nome = input("Insira o nome do aluno: ")

# Captura as 4 notas do aluno
notas = []
for i in range(4):
    while True:
        nota = float(input(f"Insira a nota {i+1} do aluno: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Por favor, insira um número entre 0 e 10.")

# Calcula a média das notas
media = sum(notas) / len(notas)

# Determina se o aluno está aprovado ou reprovado
if media >= 7:
    print(f"O aluno {nome} está aprovado com média {media:.1f}.")
else:
    print(f"O aluno {nome} está reprovado com média {media:.2f}.")
