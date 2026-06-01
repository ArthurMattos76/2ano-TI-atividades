GAMES = [
    "League of Legends",
    "Valorant",
    "Counter-Strike: Global Offensive",
    "Fortnite",
    "FIFA"
]

def mostrar_jogos():
    print("Jogos disponíveis:")
    for i, jogo in enumerate(GAMES, start=1):
        print(f"{i}. {jogo}")

def ler_entrada():
    nickname = input("Nickname: ").strip()
    mostrar_jogos()
    escolha = input("Escolha o número do jogo: ").strip()
    email = input("E-mail: ").strip()
    regras = input("Você leu e aceita as regras? (sim/não): ").strip().lower()
    return nickname, escolha, email, regras

def validar_inscricao(nickname, escolha, email, regras):
    if not nickname or not escolha or not email or not regras:
        return False
    if len(nickname) < 4:
        return False
    if not escolha.isdigit():
        return False
    idx = int(escolha) - 1
    if idx < 0 or idx >= len(GAMES):
        return False
    if email == "":
        return False
    if regras not in ("sim", "s", "yes", "y"):
        return False
    return True

def main():
    print("=== Sistema de Inscrição para Campeonato de Games ===")
    nickname, escolha, email, regras = ler_entrada()
    if validar_inscricao(nickname, escolha, email, regras):
        print("Inscrição realizada com sucesso!")
    else:
        print("Preencha todos os campos obrigatórios.")

if __name__ == "__main__":
    main()

def mostrar_jogos():
    print("Jogos disponíveis:")
    for i, jogo in enumerate(GAMES, start=1):
        print(f"{i}. {jogo}")

def ler_entrada():
    nickname = input("Nickname: ").strip()
    mostrar_jogos()
    escolha = input("Escolha o número do jogo: ").strip()
    email = input("E-mail: ").strip()
    regras = input("Você leu e aceita as regras? (sim/não): ").strip().lower()
    return nickname, escolha, email, regras

def validar_inscricao(nickname, escolha, email, regras):
    # Todos os campos são obrigatórios
    if not nickname or not escolha or not email or not regras:
        return False
    # Nickname deve possuir pelo menos 4 caracteres
    if len(nickname) < 4:
        return False
    # Jogo deve ser selecionado e válido
    if not escolha.isdigit():
        return False
    idx = int(escolha) - 1
    if idx < 0 or idx >= len(GAMES):
        return False
    # E-mail não pode estar vazio (validação mínima)
    if email == "":
        return False
    # Regras devem ser aceitas
    if regras not in ("sim", "s", "yes", "y"):
        return False
    return True

def main():
    print("=== Sistema de Inscrição para Campeonato de Games ===")
    nickname, escolha, email, regras = ler_entrada()
    if validar_inscricao(nickname, escolha, email, regras):
        print("Inscrição realizada com sucesso!")
    else:
        print("Preencha todos os campos obrigatórios.")

if __name__ == "__main__":
    main()