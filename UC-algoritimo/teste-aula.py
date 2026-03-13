tentativas = 3

while tentativas > 0:
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    if senha == "676767" and usuario == "cityboy":
        print("Acesso concedido.")
        break
    elif tentativas > 2:
        print("Acesso negado, duas tentativas restantes.")
        tentativas -= 1
    elif tentativas > 1:
        print("Acesso negado, uma tentativa restante.") 
        tentativas -= 1
    elif tentativas == 1:
        print("Última tentativa.")
        tentativas -= 1

if tentativas == 0:
    print("Número de tentativas excedido.")