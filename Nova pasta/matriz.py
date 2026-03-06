#estruturas de dados onde uma lista é contida dentro de outra lista, permitindo representar tabelas. Serve para organizar grandes conjutas de dados.

matriz = [
    [1, 2, 3],
    [4, 5, 6],  
    [7, 8, 9]
]

print("Matriz completa:")
for linha in matriz:
    print(linha)

print(f"\n Elemento [1][2]: {matriz[1][2]}")  # Acessando o elemento na linha 1, coluna 2 (valor 6)
print(f"\n Elemento [0][0]: {matriz[0][0]}")  # Acessando o elemento na linha 0, coluna 0 (valor 1)
print(f"\n Elemento [2][1]: {matriz[2][1]}")  # Acessando o elemento na linha 2, coluna 1 (valor 8)
