def soma_segura(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError
        return a + b
    except TypeError:
        print("Entrada invalida")
        return 0

print(soma_segura(3, 7))         # Saída: 10
print(soma_segura(12, -4))       # Saída: 8
print(soma_segura(0, 0))         # Saída: 0
print(soma_segura("x", 2))       # Saída: Entrada invalida \n 0