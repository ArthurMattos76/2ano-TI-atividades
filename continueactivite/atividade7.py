Senha = input("Digite uma Senha: ")

tem_numero = any(char.isdigit() for char in Senha)

if len(Senha) >= 8 and tem_numero:
    print("Senha válida.")
else:
    print("Senha inválida.")