idade = input("Digite a idade do aluno: ")
idade = int(idade)
if idade < 12:
    categoria = "infantil"
elif idade < 18:
    categoria = "juvenil"
elif idade < 60:
    categoria = "adulta"
else:
    categoria = "sênior"

print("Categoria:", categoria)
print("Bem vindo a competição!")