função = "rank_jogador(pontos,derrotas)"
derrotas = 0
if derrotas > -10:
    class Jogador:
        def __init__(self, nome, pontos, derrotas):
            self.nome = nome
            self.pontos = pontos
            self.derrotas = derrotas
        def rank(self):
            taxa = self.pontos / (self.derrotas + 1)
            if self.derrotas < 0:
                return "Banido"
            if taxa < 100:
                return "Bronze"
            elif taxa < 300:
                return "Prata"
            elif taxa < 600:
                return "Ouro"
            elif taxa >= 1000:
                return "Diamante"
            
    