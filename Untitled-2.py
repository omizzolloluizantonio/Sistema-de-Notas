def classificar():
    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            aluno, nota1, nota2, nota3 = linha.strip().split(";")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
media = (nota1 + nota2 + nota3) / 3