n = int(input("Digite quantos alunos tem: "))
alunosrec = 0
i = 0
while i < n:
    nota = int(input("Digite a nota :"))
    if nota >= 3 and nota <= 5:
        alunosrec = alunosrec + 1
    i = i + 1
print(alunosrec, "alunos ficaram de recuperação.")
