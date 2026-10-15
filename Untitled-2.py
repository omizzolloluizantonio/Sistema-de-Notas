def classificar():
    with open("notas.txt", "a", encoding="utf-8") as arquivo:
        for linha in arquivo:
            aluno, nota1, nota2, nota3 = linha.strip().split(";")
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)
            media = (nota1 + nota2 + nota3) / 3

        if media >=7:
            with open("aprovados.txt", "a", encoding="utf-8") as aprovados:
                aprovados.write(f"{aluno};{media:.2f}\n")
        elif media <7 and media >=5:
            with open("exames.txt", "a", encoding="utf-8") as exames:
                exames.write(f"{aluno};{media:.2f}\n")
        else:
            with open("reprovados.txt", "a", encoding="utf-8") as reprovados:
                reprovados.write(f"{aluno};{media:.2f}\n")
                
        print(f"Aluno(a): {aluno} | Média: {media:.2f}")
classificar()


