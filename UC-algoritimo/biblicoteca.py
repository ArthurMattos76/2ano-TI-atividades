lista = ["don quixote", "morro dos ventos uivantes", "crime e castigo", "o processo", "o estrangeiro"]


while True:
    print ("1. cadastrar livros")
    print ("2. listar livros")
    print ("3. emprestar livros")
    print ("4. devolver livros")
    print ("5. sair")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        livro = input("Digite o nome do livro que deseja adicionar:")
        lista.append(livro)
        print ("Livros disponíveis:", lista)
    elif opcao == 2:
        print ("Livros disponíveis:", lista)
    elif opcao == 3:
        emprestar = input("Digite o nome do livro que deseja pegar emprestado:")
        if emprestar in lista:
    lista.remove(emprestar)
    print(f"livro '{emprestar}' emprestado.")
    elif:
    print(f"livro '{emprestar}' não encontrado na lista.")
print("Livros disponíveis:", lista)
    elif opcao == 4:
        devolver = input("insira o nome do livro que deseja devolver:")

        if devolver in lista:
        print(f"livro '{devolver}' já está na lista.")
        elif devolver == emprestar:
        lista.append(devolver)
        print(f"livro '{devolver}' devolvido com sucesso.")
        else:
        print(f"livro '{devolver}' não existe.")
