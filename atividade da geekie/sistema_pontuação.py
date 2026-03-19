pontos = int(input("Digite a quantidade de pontos: "))
tempo = int(input("Digite o tempo: "))
usuario = input("Digite o nome do usuário: ")

def pontuacao_total(pontos, tempo):
    if tempo < 30:
        bonus = 50
    elif tempo > 100:
        lost = 20
    else: pontos > 200
    while True:
        print(200)
