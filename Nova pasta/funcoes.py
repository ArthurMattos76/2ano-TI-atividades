notas = [8.5, 7.0, 9.5, 6.0, 8.0]

print("Notas dos alunos:")

print("Menor: ", min(notas))
print("Maior: ", max(notas))
print("Soma: ", sum(notas))
print("Média: ", sum(notas) / len(notas))


nomes = ["Alice", "Bob", "Charlie", "David", "Eve"]

# apenas o elemento
print("usando FOR simples:")
for nome in nomes:
    print(F"Olá, {nome}!")

# indice do elemento
print("/n Usando enumerate:")
for indice, nome in enumerate(nomes):
    print(F"Posição {indice}: {nome}")