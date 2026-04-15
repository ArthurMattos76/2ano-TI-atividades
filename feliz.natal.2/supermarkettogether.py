try:
    preco_produto1 = 5.99  # Exemplo: arroz
    preco_produto2 = 3.49  # Exemplo: feijão


    a = 2
    b = 3

    preco_produto1, preco_produto2 = preco_produto2, preco_produto1
    a, b = b, a

    total_produto1 = preco_produto1 * a
    total_produto2 = preco_produto2 * b

    total_geral = total_produto1 + total_produto2

    print(f"Total do produto 1: R$ {total_produto1:.2f}")
    print(f"Total do produto 2: R$ {total_produto2:.2f}")
    print(f"Total geral: R$ {total_geral:.2f}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")