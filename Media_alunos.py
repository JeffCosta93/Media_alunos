def calcular_media(notas):

    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)


notas_alunos = []


while True:
    nota_input = input("Insira a nota do aluno (ou digite 'parar' para encerrar): ")

    if nota_input.lower() == 'parar':
        break


    if nota_input.replace('.', '', 1).isdigit():
       nota = float(nota_input)
       notas_alunos.append(nota)
    else:
         print("Entrada inválida. Por favor, insira um valor numérico.")


if notas_alunos:

    for i, notas in enumerate(notas_alunos, start=1):
        media = calcular_media([notas])
        print(f"Média do Aluno {i}: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
