def divisao(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Não divida por zero!"