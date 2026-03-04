nome1 = "ana"
nome2 = "joão"
nome3 = "maria"
nomes = [nome1, nome2, nome3]
print(nomes)

dados = [nome1, 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["Cachorro", "Gato"]
print("Original: ", lista)
lista.append("Coelho")
print("Atualizada: ", lista)

lista.insert(1, "Papagaio")
print("Atualizada: ", lista)

lista.extend(["Peixe", "Hamster"])
print("lista final: ", lista)