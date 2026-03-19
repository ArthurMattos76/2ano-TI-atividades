funcao = "saldo_final(saldo, saque)"
def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    if saque > 1000:
        taxa = saque * 0.02
        return saldo - saque - taxa
    return saldo - saque
print("Caso contrário, sem taxa:")
print("retorne  o saldo restante:", saldo_final(1000, 500))
