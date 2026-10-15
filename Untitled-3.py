nota_exame=float(input("Digite a nota que o aluno(a) obteve no exame: "))

with open("exames.txt", "r", encoding="utf-8") as exames:
    linhas = exames.readlines()

    for linha in linhas:
        aluno, media = linha.strip().split(";")

        print(f"Aluno(a): {aluno} | Média: {media}")

        nota_exame = float(input("Digite a nota do exame: "))
        