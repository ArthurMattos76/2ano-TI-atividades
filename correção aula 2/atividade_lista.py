Compras = ["carne", "frango", "peixe", "vegetais", "frutas"]    
print("Original: ", Compras)
Compras.append("arroz")
print("Atualizada: ", Compras)

nova_item = input("Digite um item para adicionar à lista de compras: ")
Compras.append(nova_item)
print("lista de compras atualizada:")
print(Compras)