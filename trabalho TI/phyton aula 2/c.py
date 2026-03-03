usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "correntista" and senha == "123456":
    print("Seja bem-vindo ao nosso banco!")
elif usuario == "correntista" and senha != "123456":
    print("Senha incorreta! Você ainda tem 2 tentativas.")
else:
    print("Senha incorreta! Você ainda tem 1 tentativa")
    if usuario == "correntista" and senha != "123456":
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
   