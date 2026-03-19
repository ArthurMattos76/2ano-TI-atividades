usuario = input("Digite o nome do usuário: ")
print ("admin:", "admin")
senha = input("Digite a senha: ")
print ("senha:", "1234")
tentativa = 3

def autenticar(usuario, senha):
    if usuario == "admin" and senha == "1234":
        print("Acesso total.")
        return True
    elif tentativa > 3:
        print("Bloqueado.")
        return False
    elif usuario == "admin":
        print("Senha incorreta:")
        return False
    else:
        print("Usuário inválido.")
        return False 
    