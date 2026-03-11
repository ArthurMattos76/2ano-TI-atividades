aluno = {}

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['nota1'] = float(input("Digite a nota da prova 1: "))
aluno['nota2'] = float(input("Digite a nota da prova 2: "))

aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2

if aluno['media'] >= 7:
    situacao = "Aprovado"
elif 5 <= aluno['media'] < 7:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

print(f"Situação: {situacao}")