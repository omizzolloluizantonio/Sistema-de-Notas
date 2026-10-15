def resultados_alunos():
    alunos=input("Digite o nome do(a) aluno(a): ")
    nota1=float(input("Digite a nota 1 do(a) aluno(a): "))
    nota2=float(input("Digite a nota 2 do(a) aluno(a): "))
    nota3=float(input("Digite a nota 3 do(a) aluno(a): "))

    with open("notas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{alunos};{nota1};{nota2};{nota3}\n")

    print("As notas foram registradas com sucesso!")


while True:
    resultados_alunos()
    continuar=input("Há mais notas para registrar? (S/N) ").upper()
    while continuar not in ["S", "N"]:
        print("Resposta inválida! Digite S ou N.")
        continuar = input("Há mais notas para registrar? (S/N): ").upper()
    if continuar.upper()== "N":
        print("Todas as notas foram registradas.")
        break

