# quadrados de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print("Quadraddos: ", quadrados)

# numeros pares de 1 a 20
pares = [x for x in range(1, 21 ) if x % 2 == 0]
print("Números pares: ", pares)

# vogais de "PROGAMAÇÃO"
vogais = [letra for letra in "PROGAMAÇÃO" if letra.lower() in "aeiou"]
print("Vogais: ", vogais)
