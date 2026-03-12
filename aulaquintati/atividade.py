def somarNumerosEProduto(a, b):
    soma = a + b
    produto = a * b
    return soma, produto

resultadoSoma, resultadoProduto = somarNumerosEProduto(5, 10)
print(f"A soma é: {resultadoSoma}")
print(f"O produto é: {resultadoProduto}")
