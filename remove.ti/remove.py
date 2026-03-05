nomes = ["João", "Maria", "José", "Ana", "Carlos"]
print("Nomes: ", nomes)

# Removendo um nome específico
nomes.remove("José")
print("Lista atualizada: ", nomes)

removido = nomes.pop(1)  # Remove o nome na posição 1 (Maria)
print(f"Nome removido: {removido}")
print("Após pop(): ", nomes)

del nomes[0]  # Remove o nome na posição 0 (João)
print("Após del nome [0] ", nomes)

# Clear remove todos os elementos da lista
nomes.clear()
print("Lista atualizada: ", nomes)

