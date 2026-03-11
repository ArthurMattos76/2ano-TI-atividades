total_depositos = 0.0
quantidade_transacoes = 0

while True:
    valor = float(input("Digite o valor do depósito (0 para encerrar): "))
    if valor == 0:
        break
    total_depositos += valor
    quantidade_transacoes += 1

print(f"Total de depósitos: R$ {total_depositos:.2f}")
print(f"Quantidade de transações: {quantidade_transacoes}")